"""A Python library for reading / writing EPUB files."""

from __future__ import annotations

__all__ = []

from io import BufferedIOBase
from os import PathLike, fsdecode
from pathlib import Path
from typing import IO, overload


class EPUBFile:
    """EPUB File object."""

    @overload
    def __init__(self) -> None:
        """Create an empty EPUB file object."""

    @overload
    def __init__(self, file: str | bytes | PathLike | IO[bytes]) -> None:
        """Create an EPUB file object from the speciied file."""

    def __init__(
        self,
        file: str | bytes | PathLike | IO[bytes] | None = None,
    ) -> None:
        """Create an EPUB file object."""
        match file:
            case str() | PathLike():
                self.filename = Path(file)
            case bytes():
                self.filename = file.decode()
            case PathLike():
                self.filename = fsdecode(file)
            case BufferedIOBase():
                pass
            case None:
                self.filename = None
            case _:
                msg = f"Unexpected type {type(file)!r}"
                raise TypeError(msg)

    path: Path | None
    """Path object of the EPUB file."""

    @property
    def filename(self) -> str | None:
        """File name of the EPUB file."""
        return None if self.path is None else str(self.path)

    @filename.setter
    def filename(self, value: str | None) -> None:
        """Set the file name of the EPUB file."""
        self.path = None if value is None else Path(value)
