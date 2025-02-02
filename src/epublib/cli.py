"""A CLI interface module for EPUBLib."""

from __future__ import annotations

__all__ = ["main"]

import sys
from argparse import ArgumentParser
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def main(args: Sequence[str] | None = None) -> None:
    """Run EPUBLib as a CLI interface."""
    parser = ArgumentParser("EPUBLib")
    parser.parse_args(args)
    sys.exit(0)


if __name__ == "__main__":
    main()
