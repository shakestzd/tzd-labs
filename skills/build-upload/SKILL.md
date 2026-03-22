---
name: build-upload
description: Use this skill when ready to compile a manuscript for journal submission, rebuilding after edits, or preparing a revision package. Triggers on "build upload package", "compile manuscript", "generate submission files", "rebuild manuscript", "prepare revision".
---

# Build Upload Package

Generate a complete journal upload package from Quarto manuscript sources and data files.

## When to Use

Use this skill when:
- Ready to compile the manuscript for submission
- Rebuilding after edits to any section, table data, or figure
- Preparing a revision package with response to reviewers

## Build Pipeline

```
Source Files                    Build Steps                     Output Files
-----                           -----                           -----
_sections/*.qmd    --+
references.bib     --+---> Quarto render ------------------>   Manuscript.docx
citation-style.csl --+     (cross-refs + citations resolved)

data/tables/*.csv  -------> build_tables.py ----------------->  Table 1-N.docx
                            (quartopress.table_builder)

data/figures/*     -------> figure scripts ------------------>  Figure 1-N.tiff

legends text       -------> appended to Manuscript.docx --->   (in manuscript)

response letter    -------> python-docx --------------------->  Response.docx
```

## Build Script Structure

The master `build_upload.py` follows this pattern:

```python
def main():
    setup_output_dir()

    # 1. Render manuscript (Quarto)
    build_manuscript()    # Assembles sections, replaces cross-refs, renders .docx

    # 2. Build tables (quartopress.table_builder)
    build_all_tables()    # Each table from CSV/data -> .docx with three-line borders

    # 3. Copy figures
    copy_figures()        # TIFF files to output with submission naming

    # 4. Response to editor/reviewers
    build_response()      # Markdown -> .docx
```

## Cross-Reference Handling

Since tables and figures are separate files (not embedded), Quarto cross-references (`@tbl-`, `@fig-`) won't resolve. The build script handles this:

```python
_CROSS_REF_MAP = {
    "@tbl-characteristics": "Table 1",
    "@tbl-specs": "Table 2",
    "@fig-workflow": "Figure 1",
    "@fig-metrics": "Figure 2",
}
```

**Numbering rule:** Tables and figures are numbered in order of first reference in manuscript text.

## Validation Checklist

After building, verify:
- [ ] Word count on title page matches actual body text count
- [ ] Abstract word count accurate and under limit
- [ ] All tables present and numbered correctly
- [ ] All figures present as TIFF files
- [ ] Figure/table references in text match file numbering
- [ ] Legends present after references
- [ ] No stale cross-references (`?@tbl-`, `?@fig-`)
- [ ] No AI writing tells (run `/fix-ai-tells`)

## Quick Commands

```bash
# Full rebuild
uv run python scripts/build_upload.py

# Tables only
uv run python scripts/build_tables.py
```
