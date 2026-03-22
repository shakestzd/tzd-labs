#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "mistralai>=1.0",
# ]
# ///
"""
pdf_ocr.py — Extract text from PDFs using Mistral OCR.

Usage:
    uv run python scripts/pdf_ocr.py path/to/file.pdf
    uv run python scripts/pdf_ocr.py path/to/file.pdf --output path/to/output.md
    uv run python scripts/pdf_ocr.py path/to/file.pdf --json

Output: Markdown text to stdout (and optionally to --output file).
The .md file is saved alongside the PDF by default if --output is not specified.

Reads MISTRAL_API_KEY from environment or .env file in the working directory.
"""

import argparse
import json
import os
import sys
from pathlib import Path


def load_env(path: Path) -> None:
    """Load key=value pairs from a .env file into os.environ."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def get_api_key() -> str:
    # Try current dir .env, then common project roots
    for candidate in [
        Path.cwd() / ".env",
        Path(__file__).parent.parent / ".env",
        Path.home() / "DevProjects" / "Systems" / ".env",
    ]:
        load_env(candidate)

    key = os.environ.get("MISTRAL_API_KEY", "")
    if not key:
        print("ERROR: MISTRAL_API_KEY not found in environment or .env", file=sys.stderr)
        sys.exit(1)
    return key


def ocr_pdf(pdf_path: Path, api_key: str, include_images: bool = False) -> str:
    """Upload a PDF to Mistral OCR and return the extracted markdown text."""
    from mistralai import Mistral, DocumentURLChunk

    client = Mistral(api_key=api_key)

    print(f"Uploading {pdf_path.name} ({pdf_path.stat().st_size // 1024}KB)...", file=sys.stderr)
    uploaded = client.files.upload(
        file={"file_name": pdf_path.stem, "content": pdf_path.read_bytes()},
        purpose="ocr",
    )

    signed_url = client.files.get_signed_url(file_id=uploaded.id, expiry=1)

    print("Running OCR...", file=sys.stderr)
    response = client.ocr.process(
        document=DocumentURLChunk(document_url=signed_url.url),
        model="mistral-ocr-latest",
        include_image_base64=include_images,
    )

    # Clean up the uploaded file
    try:
        client.files.delete(file_id=uploaded.id)
    except Exception:
        pass

    pages = []
    for i, page in enumerate(response.pages, 1):
        pages.append(f"<!-- Page {i} -->\n{page.markdown}")

    return "\n\n".join(pages)


def ocr_pdf_as_dict(pdf_path: Path, api_key: str) -> dict:
    """Return structured OCR output as a dict (page-by-page)."""
    from mistralai import Mistral, DocumentURLChunk

    client = Mistral(api_key=api_key)

    uploaded = client.files.upload(
        file={"file_name": pdf_path.stem, "content": pdf_path.read_bytes()},
        purpose="ocr",
    )
    signed_url = client.files.get_signed_url(file_id=uploaded.id, expiry=1)
    response = client.ocr.process(
        document=DocumentURLChunk(document_url=signed_url.url),
        model="mistral-ocr-latest",
        include_image_base64=False,
    )

    try:
        client.files.delete(file_id=uploaded.id)
    except Exception:
        pass

    return {
        "file": str(pdf_path),
        "pages": [
            {"page": i + 1, "markdown": p.markdown}
            for i, p in enumerate(response.pages)
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from a PDF using Mistral OCR")
    parser.add_argument("pdf", help="Path to PDF file")
    parser.add_argument("--output", "-o", help="Output file path (default: <pdf>.md alongside input)")
    parser.add_argument("--json", action="store_true", help="Output structured JSON instead of markdown")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout only, no file written")
    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    if not pdf_path.exists():
        print(f"ERROR: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)
    if pdf_path.suffix.lower() != ".pdf":
        print(f"WARNING: File does not have .pdf extension: {pdf_path}", file=sys.stderr)

    api_key = get_api_key()

    if args.json:
        result = json.dumps(ocr_pdf_as_dict(pdf_path, api_key), indent=2)
        print(result)
        if not args.stdout:
            out = Path(args.output) if args.output else pdf_path.with_suffix(".ocr.json")
            out.write_text(result)
            print(f"Saved: {out}", file=sys.stderr)
    else:
        markdown = ocr_pdf(pdf_path, api_key)
        print(markdown)
        if not args.stdout:
            out = Path(args.output) if args.output else pdf_path.with_suffix(".md")
            out.write_text(markdown)
            print(f"Saved: {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
