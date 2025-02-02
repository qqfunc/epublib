"""EPUB reading test."""

from __future__ import annotations

__all__ = []

from pathlib import Path

from epublib import EPUBFile


def test_epub_str() -> None:
    """Read an EPUB file."""
    path = Path(__file__) / "examples" / "example1.epub"
    epub = EPUBFile(str(path))
    assert epub.path == path
    assert epub.filename == str(path)
