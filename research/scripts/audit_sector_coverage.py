"""Create a transparent coverage matrix for the existing analysis-sector tree.

The audit measures documentation signals only. It never labels a sector as verified
because the presence of files or links does not prove that individual claims are current.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ANALYSIS_ROOT = ROOT / "ibb-business-database/التحليلات"
OUTPUT_PATH = ROOT / "research/sector-coverage-matrix.csv"
URL_PATTERN = re.compile(r"https?://[^\s)\]>]+")
SOURCE_HEADING = re.compile(r"^#{1,4}\s+.*(?:المصادر|مراجع|Sources|References)", re.MULTILINE)
ESTIMATE_PATTERN = re.compile(r"تقدير|تقديري|افتراضي|مسح ميداني", re.IGNORECASE)


def relative_sector_path(markdown_file: Path) -> str:
    return str(markdown_file.parent.relative_to(ANALYSIS_ROOT)).replace("\\", "/")


def main() -> None:
    rows: list[dict[str, object]] = []
    for sector_dir in sorted(path for path in ANALYSIS_ROOT.iterdir() if path.is_dir()):
        markdown_files = sorted(sector_dir.rglob("*.md"))
        source_headings = 0
        urls = 0
        estimate_signals = 0
        words = 0
        for markdown_file in markdown_files:
            text = markdown_file.read_text(encoding="utf-8", errors="replace")
            source_headings += len(SOURCE_HEADING.findall(text))
            urls += len(URL_PATTERN.findall(text))
            estimate_signals += len(ESTIMATE_PATTERN.findall(text))
            words += len(text.split())

        if urls == 0:
            readiness = "needs_sources"
        elif estimate_signals > 0:
            readiness = "needs_claim_review"
        else:
            readiness = "needs_verification"

        rows.append(
            {
                "sector": sector_dir.name,
                "markdown_files": len(markdown_files),
                "source_sections": source_headings,
                "url_mentions": urls,
                "estimate_signals": estimate_signals,
                "word_count": words,
                "documentation_readiness": readiness,
            }
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(rows[0]) if rows else [])
        writer.writeheader()
        writer.writerows(rows)

    summary: dict[str, int] = {}
    for row in rows:
        readiness = str(row["documentation_readiness"])
        summary[readiness] = summary.get(readiness, 0) + 1
    print(f"sectors={len(rows)}")
    print(f"markdown_files={sum(int(row['markdown_files']) for row in rows)}")
    print(f"readiness={summary}")
    print(f"output={OUTPUT_PATH}")


if __name__ == "__main__":
    main()
