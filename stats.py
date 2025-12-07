"""Generate simple runtime and lint stats for tutorials and LeetCode solutions."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from collections.abc import Iterable
from pathlib import Path
from time import perf_counter
from typing import NamedTuple


class RunStats(NamedTuple):
    files: int
    lines: int
    runtime: float
    errors: int
    ruff: str
    black: str
    pre_commit: str
    pytest: str


BASE_DIR = Path(__file__).resolve().parent

CATEGORIES = {
    "Tutorial": BASE_DIR / "tutorial",
    "LeetCode": BASE_DIR / "leetcode",
}


def python_files(root: Path) -> list[Path]:
    return [path for path in root.rglob("*.py") if path.name != "__init__.py"]


def count_lines(paths: Iterable[Path]) -> int:
    return sum(path.read_text(encoding="utf-8").count("\n") + 1 for path in paths)


def run_scripts(paths: Iterable[Path]) -> tuple[int, float]:
    errors = 0
    runtime = 0.0

    for path in paths:
        start = perf_counter()
        result = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
        runtime += perf_counter() - start
        if result.returncode != 0:
            errors += 1

    return errors, runtime


def optional_ruff(root: Path) -> str:
    if shutil.which("ruff") is None:
        return "skipped"

    result = subprocess.run(
        ["ruff", "check", str(root), "--exit-zero", "--statistics"],
        capture_output=True,
        text=True,
        check=False,
    )
    count = 0
    for line in result.stdout.splitlines():
        if line.startswith("Found "):
            try:
                count = int(line.split()[1])
            except (IndexError, ValueError):
                count = 0
            break
    if result.returncode != 0:
        return "fail"
    return str(count)


def optional_black(root: Path) -> str:
    if shutil.which("black") is None:
        return "skipped"

    result = subprocess.run(
        ["black", "--check", str(root)],
        capture_output=True,
        text=True,
        check=False,
    )
    paths: set[str] = set()
    summary_count = 0
    fail_count = 0

    for line in (result.stdout + result.stderr).splitlines():
        if line.startswith("would reformat") or line.startswith("would format"):
            parts = line.split(maxsplit=2)
            if len(parts) >= 3:
                paths.add(parts[2].strip())
            continue

        match = re.search(r"(\d+) file(?:s)? would (?:be )?reformatted", line)
        if match:
            summary_count = max(summary_count, int(match.group(1)))

        match = re.search(r"(\d+) file(?:s)? would fail to reformat", line)
        if match:
            fail_count = max(fail_count, int(match.group(1)))

    count = max(len(paths), summary_count, fail_count)
    if count:
        return str(count)
    if result.returncode != 0:
        return "fail"
    return "0"


def gather_stats(root: Path, pre_commit: str, pytest: str) -> RunStats:
    files = python_files(root)
    errors, runtime = run_scripts(files)

    return RunStats(
        files=len(files),
        lines=count_lines(files),
        runtime=runtime,
        errors=errors,
        ruff=optional_ruff(root),
        black=optional_black(root),
        pre_commit=pre_commit,
        pytest=pytest,
    )


def print_block(name: str, stats: RunStats) -> None:
    print(name)
    print(f"files: {stats.files}")
    print(f"lines: {stats.lines}")
    print(f"runtime: {stats.runtime:.2f} sec")
    print(f"errors: {stats.errors}")
    print(f"black: {stats.black}")
    print(f"ruff: {stats.ruff}")
    print(f"pre-commit: {stats.pre_commit}")
    print(f"pytest: {stats.pytest}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pre-commit",
        default="",
        help="Optional pre-commit notes or status to include in the summary.",
    )
    parser.add_argument(
        "--pytest",
        default="",
        help="Optional pytest notes or status to include in the summary.",
    )
    args = parser.parse_args()

    tutorial_stats = gather_stats(CATEGORIES["Tutorial"], args.pre_commit, args.pytest)
    leetcode_stats = gather_stats(CATEGORIES["LeetCode"], args.pre_commit, args.pytest)

    print_block("Tutorial", tutorial_stats)
    print()
    print_block("LeetCode", leetcode_stats)


if __name__ == "__main__":
    main()