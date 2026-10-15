"""Real Git history tests: update detection must preserve local work."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("upstream_status", Path(__file__).parents[1] / "scripts/upstream_status.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class UpdateStatusTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.upstream = root / "source"
        self.work = root / "work"
        self.origin = root / "personal.git"
        self.run_git("init", "-b", "main", str(self.upstream))
        self.configure(self.upstream)
        self.commit(self.upstream, "baseline.txt", "baseline")
        self.run_git("clone", "--bare", str(self.upstream), str(self.origin))
        self.run_git("clone", str(self.origin), str(self.work))
        self.configure(self.work)
        self.run_git("-C", str(self.work), "remote", "add", "upstream", str(self.upstream))

    def run_git(self, *args):
        return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout.strip()

    def configure(self, path):
        self.run_git("-C", str(path), "config", "user.name", "History Test")
        self.run_git("-C", str(path), "config", "user.email", "test@example.invalid")

    def commit(self, path, filename, content):
        (path / filename).write_text(content, encoding="utf-8")
        self.run_git("-C", str(path), "add", "--", filename)
        self.run_git("-C", str(path), "commit", "-m", content)

    def test_synchronized_history(self):
        result = module.collect(self.work, fetch=True)
        for key in ("upstream_updates", "personal_only_commits", "local_unpushed_commits", "personal_remote_updates"):
            self.assertEqual(result[key], 0)

    def test_diverged_updates_preserve_uncommitted_work(self):
        self.commit(self.work, "personal.txt", "personal feature")
        self.commit(self.upstream, "new.txt", "upstream feature")
        (self.work / "notes.txt").write_text("unfinished work", encoding="utf-8")
        before = self.run_git("-C", str(self.work), "rev-parse", "HEAD")
        result = module.collect(self.work, fetch=True)
        self.assertEqual(result["upstream_updates"], 1)
        self.assertEqual(result["personal_only_commits"], 1)
        self.assertEqual(result["local_unpushed_commits"], 1)
        self.assertTrue(result["working_tree_dirty"])
        self.assertEqual(self.run_git("-C", str(self.work), "rev-parse", "HEAD"), before)
        self.assertEqual((self.work / "notes.txt").read_text(), "unfinished work")

    def test_merge_and_push_clear_pending_updates(self):
        self.commit(self.work, "personal.txt", "personal feature")
        self.commit(self.upstream, "new.txt", "upstream feature")
        module.collect(self.work, fetch=True)
        self.run_git("-C", str(self.work), "merge", "--no-edit", "upstream/main")
        self.run_git("-C", str(self.work), "push", "origin", "main")
        result = module.collect(self.work, fetch=True)
        self.assertEqual(result["upstream_updates"], 0)
        self.assertEqual(result["local_unpushed_commits"], 0)
        self.assertGreater(result["personal_only_commits"], 0)
        self.assertTrue((self.work / "personal.txt").exists())
        self.assertTrue((self.work / "new.txt").exists())

    def test_personal_remote_changes_are_reported(self):
        other = Path(self.temp.name) / "other"
        self.run_git("clone", str(self.origin), str(other))
        self.configure(other)
        self.commit(other, "remote.txt", "personal remote feature")
        self.run_git("-C", str(other), "push", "origin", "main")
        result = module.collect(self.work, fetch=True)
        self.assertEqual(result["personal_remote_updates"], 1)
        self.assertFalse((self.work / "remote.txt").exists())


if __name__ == "__main__":
    unittest.main()
