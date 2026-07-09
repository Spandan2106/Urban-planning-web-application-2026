"""File-system utilities used by uploads and exports."""

from __future__ import annotations

from pathlib import Path


def ensure_directory(path: Path) -> Path:
    """Create a directory when it does not exist and return it."""

    path.mkdir(parents=True, exist_ok=True)
    return path


def safe_filename(filename: str) -> str:
    """Return a conservative filename with unsafe characters replaced."""

    clean = "".join(char if char.isalnum() or char in "._-" else "_" for char in filename)
    return clean or "graph.txt"


def write_uploaded_file(content: bytes, target: Path) -> Path:
    """Persist uploaded bytes to disk and return the target path."""

    ensure_directory(target.parent)
    target.write_bytes(content)
    return target
