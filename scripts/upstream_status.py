#!/usr/bin/env python3
"""Compare personal and upstream history without merging or editing the working tree."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=60,
    )
    if proc.returncode:
        raise RuntimeError(f"git {' '.join(args[:2])} failed; check repository, remotes and authentication")
    return proc.stdout.strip()


def collect(repo: Path, fetch: bool = False, limit: int = 5) -> dict:
    limit = max(1, min(limit, 20))
    git(repo, "rev-parse", "--show-toplevel")
    remotes = set(git(repo, "remote").splitlines())
    if not {"origin", "upstream"} <= remotes:
        raise RuntimeError("Both origin (personal repository) and upstream (myopenclaw) must be configured")
    if fetch:
        # Fetch named branches only. Never pull, reset, checkout, push, or auto-merge.
        for remote in ("upstream", "origin"):
            git(repo, "fetch", remote, f"+refs/heads/main:refs/remotes/{remote}/main")
    upstream = "upstream/main"
    origin = "origin/main"
    for ref in (upstream, origin):
        git(repo, "rev-parse", "--verify", ref)
    git(repo, "merge-base", "HEAD", upstream)

    def count(range_: str) -> int:
        return int(git(repo, "rev-list", "--count", range_))

    def commits(range_: str) -> list[dict]:
        output = git(repo, "log", f"--max-count={limit}", "--format=%h%x09%s", range_)
        return [dict(zip(("sha", "subject"), line.split("\t", 1))) for line in output.splitlines()]

    incoming = count("HEAD.." + upstream)
    personal = count(upstream + "..HEAD")
    unpushed = count(origin + "..HEAD")
    origin_incoming = count("HEAD.." + origin)
    dirty = bool(git(repo, "status", "--porcelain"))
    return {
        "comparison": "current HEAD against main branches",
        "references": "fetched" if fetch else "cached; use --fetch to check remote updates",
        "head": git(repo, "rev-parse", "--short", "HEAD"),
        "upstream_head": git(repo, "rev-parse", "--short", upstream),
        "upstream_updates": incoming,
        "personal_only_commits": personal,
        "local_unpushed_commits": unpushed,
        "personal_remote_updates": origin_incoming,
        "working_tree_dirty": dirty,
        "upstream_commits": commits("HEAD.." + upstream),
        "personal_commits": commits(upstream + "..HEAD"),
        "next_action": (
            "Save current work, then review updates on a sync branch" if dirty
            else "Review upstream updates on a sync branch" if incoming
            else "Review personal remote changes" if origin_incoming
            else "Push reviewed local commits" if unpushed
            else "No pending remote updates or local pushes"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="Refresh origin/main and upstream/main metadata")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--repo", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        data = collect(args.repo, args.fetch, args.limit)
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f"Update check failed: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(f"References: {data['references']}")
        print(f"Upstream updates not integrated: {data['upstream_updates']}")
        print(f"Personal-only commits: {data['personal_only_commits']}")
        print(f"Local commits not pushed: {data['local_unpushed_commits']}")
        print(f"Personal remote updates not integrated: {data['personal_remote_updates']}")
        print(f"Working tree has changes: {data['working_tree_dirty']}")
        for item in data["upstream_commits"]:
            print(f"  upstream {item['sha']} {item['subject']}")
        print("Next: " + data["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
