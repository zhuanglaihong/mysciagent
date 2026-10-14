#!/usr/bin/env python3
"""Clone owned component repositories or check their local readiness. Never pulls/resets existing repos."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, encoding="utf-8", errors="replace",
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"}, timeout=180,
    )


def canonical(url: str) -> str:
    return url.strip().removesuffix(".git").replace("git@github.com:", "https://github.com/").lower()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Read-only readiness check")
    parser.add_argument("--directory", type=Path, default=ROOT.parent, help="Parent of sibling repositories")
    parser.add_argument("--json", action="store_true", help="Machine-readable report")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "repositories.json").read_text(encoding="utf-8"))
    results = []
    for repo in manifest["components"]:
        row = {"name": repo["name"], "status": repo["status"], "required": repo["required_for_default_stack"]}
        if repo["status"] == "source_unavailable":
            row["detail"] = repo["note"]
            results.append(row)
            continue
        path = args.directory / repo["name"]
        if not path.exists() and not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            cloned = git("clone", repo["owned_url"], str(path))
            if cloned.returncode:
                row.update(status="clone_failed", detail=cloned.stderr.strip())
                results.append(row)
                continue
        if not path.exists():
            row.update(status="missing", detail=str(path))
        else:
            top = git("-C", str(path), "rev-parse", "--show-toplevel")
            if top.returncode or Path(top.stdout.strip()).resolve() != path.resolve():
                row.update(status="not_repository", detail="Existing directory preserved")
            else:
                head = git("-C", str(path), "rev-parse", "HEAD")
                remote = git("-C", str(path), "remote", "get-url", "origin")
                row["head"] = head.stdout.strip()
                row["origin"] = remote.stdout.strip()
                row["owned_origin"] = canonical(row["origin"]) == canonical(repo["owned_url"])
                required_sha = repo.get("required_runtime_commit")
                if required_sha and row["head"] != required_sha:
                    row.update(status="version_mismatch", detail="Inherited runtime requires " + required_sha)
                elif not row["owned_origin"]:
                    row.update(status="origin_mismatch", detail="Existing upstream checkout preserved; clone the owned copy into a separate directory")
                else:
                    row["status"] = "ready_source"
        results.append(row)
    blockers = [r["name"] for r in results if r["required"] and r["status"] != "ready_source"]
    report = {"scope": "source readiness only; no runtime or credentials validated", "results": results, "default_stack_blockers": blockers}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for row in results:
            print(f'{row["name"]}: {row["status"]} {row.get("detail", "")}')
        print("Default-stack source blockers: " + (", ".join(blockers) or "none"))
    return 1 if blockers else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print(f"Repository operation failed: {exc}", file=sys.stderr)
        sys.exit(2)
