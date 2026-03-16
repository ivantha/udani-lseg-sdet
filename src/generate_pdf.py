"""Generate a professionally styled PDF interview guide from Markdown sources."""

import re
from datetime import date
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter
from weasyprint import HTML

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
STYLE_CSS = Path(__file__).resolve().parent / "style.css"
OUTPUT_DIR = ROOT / "output"
OUTPUT_PDF = OUTPUT_DIR / "interview_guide.pdf"

# ---------------------------------------------------------------------------
# Document structure: (relative path under content/, display title)
# ---------------------------------------------------------------------------
CHAPTERS = [
    ("job_description.md", "Job Description"),
    ("interviewer_amy_lee.md", "Interviewer: Amy Lee"),
    ("interviewer_andy_purtell.md", "Interviewer: Andy Purtell"),
    ("interview_guide_udani.md", "Personalised Interview Guide"),
    ("interview_prep/00_README.md", "Question Bank Index"),
    ("interview_prep/01_testing_fundamentals.md", "Testing Fundamentals"),
    ("interview_prep/02_test_automation_and_programming.md", "Test Automation & Programming"),
    ("interview_prep/03_performance_testing.md", "Performance Testing"),
    ("interview_prep/04_infrastructure_cloud_networking.md", "Infrastructure, Cloud & Networking"),
    ("interview_prep/05_financial_domain.md", "Financial Domain"),
    ("interview_prep/06_devops_and_sdlc.md", "DevOps & SDLC"),
    ("interview_prep/07_defect_management.md", "Defect Management"),
    ("interview_prep/08_leadership_and_soft_skills.md", "Leadership & Soft Skills"),
    ("interview_prep/09_scenario_based.md", "Scenario-Based Questions"),
    ("interview_prep/10_personal_and_career.md", "Personal & Career"),
    ("interview_prep/11_ai_and_modern_qa.md", "AI & Modern QA"),
    ("interview_prep/12_security_testing.md", "Security Testing"),
    ("interview_prep/13_general_sdet_questions.md", "General SDET Questions"),
    ("interview_prep/14_aws_cloud_guide.md", "AWS Cloud Guide"),
    ("interview_prep/15_devops_questions.md", "DevOps Questions"),
]

# ---------------------------------------------------------------------------
# Markdown extensions
# ---------------------------------------------------------------------------
MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "codehilite",
    "sane_lists",
    "smarty",
    "toc",
]

MD_EXTENSION_CONFIGS = {
    "codehilite": {
        "css_class": "highlight",
        "guess_lang": True,
        "noclasses": False,  # Use CSS classes (Pygments stylesheet)
    },
}


def _add_wide_table_class(html: str) -> str:
    """Add 'wide-table' class to tables with more than 3 columns."""

    def _replace(match: re.Match) -> str:
        thead = match.group(0)
        col_count = thead.count("<th")
        if col_count > 3:
            return match.group(0).replace("<table", '<table class="wide-table"', 1)
        return match.group(0)

    # Match from <table to end of </thead>
    pattern = re.compile(r"<table.*?</thead>", re.DOTALL)
    return pattern.sub(_replace, html)


def convert_markdown(file_path: Path) -> str:
    """Read a Markdown file and return HTML."""
    text = file_path.read_text(encoding="utf-8")
    html = markdown.markdown(
        text,
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS,
    )
    return _add_wide_table_class(html)


def build_cover_page() -> str:
    """Return HTML for the cover page."""
    today = date.today().strftime("%B %d, %Y")
    return f"""\
<div class="cover-page">
    <div class="logo-bar"></div>
    <h1>Interview Guide</h1>
    <p class="subtitle">Associate Lead SDET — LSEG (London Stock Exchange Group)</p>
    <p class="candidate">Prepared for Udani Weerasinghe</p>
    <p class="date">{today}</p>
    <div class="logo-bar-bottom"></div>
</div>
"""


def build_toc(chapters: list[tuple[str, str]]) -> str:
    """Return HTML for the table of contents."""
    items = []
    for idx, (_, title) in enumerate(chapters, start=1):
        items.append(f'    <li><a href="#ch-{idx}">{idx}. {title}</a></li>')
    entries = "\n".join(items)
    return f"""\
<div class="toc">
    <h2>Table of Contents</h2>
    <ol>
{entries}
    </ol>
</div>
"""


def build_chapter_html(idx: int, title: str, body_html: str) -> str:
    """Wrap converted Markdown in a chapter section."""
    return f"""\
<section class="chapter" id="ch-{idx}">
    <h1>{title}</h1>
    {body_html}
</section>
"""


def strip_first_heading(html: str) -> str:
    """Remove the first <h1> from the body HTML to avoid duplicate titles.

    Since we inject our own <h1> via build_chapter_html, we strip the first
    heading from the Markdown-converted HTML if it exists.
    """
    return re.sub(r"<h1[^>]*>.*?</h1>", "", html, count=1, flags=re.DOTALL)


def assemble_document(chapters_html: list[str], cover: str, toc: str) -> str:
    """Build the full HTML document."""
    style_css = STYLE_CSS.read_text(encoding="utf-8")
    pygments_css = HtmlFormatter(style="default").get_style_defs(".highlight")

    body = "\n".join(chapters_html)

    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>LSEG Interview Guide</title>
    <style>
{style_css}

/* Pygments syntax highlighting */
{pygments_css}
    </style>
</head>
<body>
{cover}
{toc}
{body}
</body>
</html>
"""


def main() -> None:
    """Entry point: convert all chapters and generate the PDF."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Build cover + TOC
    cover = build_cover_page()
    toc = build_toc(CHAPTERS)

    # Convert each chapter
    chapters_html = []
    for idx, (rel_path, title) in enumerate(CHAPTERS, start=1):
        file_path = CONTENT_DIR / rel_path
        if not file_path.exists():
            print(f"WARNING: {file_path} not found, skipping.")
            continue
        print(f"  [{idx:2d}/{len(CHAPTERS)}] {title}")
        body = convert_markdown(file_path)
        body = strip_first_heading(body)
        chapters_html.append(build_chapter_html(idx, title, body))

    # Assemble full HTML
    full_html = assemble_document(chapters_html, cover, toc)

    # Write HTML for debugging (optional)
    debug_html = OUTPUT_DIR / "interview_guide.html"
    debug_html.write_text(full_html, encoding="utf-8")
    print(f"\n  HTML written to {debug_html}")

    # Render PDF
    print(f"  Rendering PDF...")
    HTML(string=full_html, base_url=str(ROOT)).write_pdf(str(OUTPUT_PDF))
    print(f"  PDF written to {OUTPUT_PDF}")

    # Report size
    size_mb = OUTPUT_PDF.stat().st_size / (1024 * 1024)
    print(f"  Size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
