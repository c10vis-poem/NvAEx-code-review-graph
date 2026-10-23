"""collect_all_files applies ignore rules before touching the filesystem.

Origin: building a graph of an Obsidian vault crashed on a very long filename
under an ignored ``Drive_sync/`` folder, because the directory-walk fallback
stat()ed every path before the ignore rules ran. An OSError on one path must
also be logged and skipped, not abort the build.
"""

import logging
from pathlib import Path
from unittest.mock import patch

from code_review_graph.incremental import collect_all_files

_REAL_IS_FILE = Path.is_file


def _raise_on_poison(self: Path) -> bool:
    if "poison" in self.name:
        raise OSError(36, "File name too long")
    return _REAL_IS_FILE(self)


def _repo(tmp_path: Path) -> Path:
    (tmp_path / ".code-review-graphignore").write_text("Drive_sync/**\n")
    (tmp_path / "Drive_sync").mkdir()
    (tmp_path / "Drive_sync" / "poison.py").write_text("x = 1\n")
    (tmp_path / "ok.py").write_text("x = 1\n")
    return tmp_path


def test_ignored_path_is_not_stat_ed(tmp_path):
    repo = _repo(tmp_path)
    with patch.object(Path, "is_file", _raise_on_poison):
        assert collect_all_files(repo) == ["ok.py"]


def test_oserror_on_one_file_is_logged_and_skipped(tmp_path, caplog):
    repo = _repo(tmp_path)
    (repo / "poison.py").write_text("x = 1\n")
    with patch.object(Path, "is_file", _raise_on_poison):
        with caplog.at_level(logging.WARNING):
            assert collect_all_files(repo) == ["ok.py"]
    assert "poison.py" in caplog.text
