---
name: manuscript-setup
description: Use this skill when starting a new manuscript project, adding quartopress build pipeline to an existing project, converting a draft into a structured Quarto project, or setting up table/figure generation. Triggers on "scaffold manuscript", "set up manuscript", "new manuscript project", "quartopress init", "create manuscript structure".
---

# Manuscript Setup

Scaffold a new or augment an existing Quarto-based manuscript project for journal submission using the quartopress pipeline.

## When to Use

Use this skill when:
- Starting a new manuscript project from scratch
- Adding quartopress build pipeline to an existing project
- Converting an existing draft into a structured Quarto project
- Setting up table/figure generation in a project that already has .qmd files

## Prerequisites

Install quartopress: `uv pip install quartopress`

## New vs. Existing Projects

**New project:** `quartopress-init ./my-manuscript --title "My Study"`
Creates the full directory structure, all section templates, build scripts, and bibliography files.

**Existing project:** `quartopress-init .`
Detects what's already present (.qmd sections, .bib files, build scripts, table builder) and adds only what's missing. Never overwrites existing files unless `--force` is used.

## Project Structure

The scaffold creates:

```
manuscript-project/
├── manuscript/
│   ├── manuscript.qmd              # Master Quarto file (includes all sections)
│   ├── _sections/
│   │   ├── _title_page.qmd         # Title, authors, affiliations
│   │   ├── _abstract.qmd           # Structured abstract
│   │   ├── _introduction.qmd       # Background, gap, objectives
│   │   ├── _methods.qmd            # Study design, measures, analysis
│   │   ├── _results.qmd            # Primary and secondary outcomes
│   │   └── _discussion.qmd         # Interpretation, limitations, conclusions
│   ├── _templates/
│   │   └── journal-reference.docx  # Journal Word template (controls formatting)
│   ├── references.bib              # BibTeX bibliography
│   └── citation-style.csl          # Citation style (AMA, Vancouver, etc.)
├── data/
│   ├── tables/                     # CSV source files for tables
│   └── figures/                    # Data files for figure generation
├── scripts/
│   ├── build_tables.py             # Declarative table definitions
│   └── build_upload.py             # Master build script
├── output/                         # Generated submission files
└── review/                         # Reviewer feedback and responses
```

## Setup Steps

1. Run `quartopress-init` with appropriate flags
2. Configure the master Quarto file (`reference-doc`, `bibliography`, `csl`)
3. Create section files from templates
4. Set up the build pipeline (table definitions, figure copy paths, cross-reference map)
5. Configure for target journal using `/set-journal`

## Journal Configurations

| Journal | Word Limit | Abstract | Figures | Tables | Reference Style |
|---------|-----------|----------|---------|--------|-----------------|
| PRS | 3,000 (+500 ext) | 250, structured | 300 DPI TIFF | Separate .docx | AMA |
| JPRAS | 4,000 | 250, structured | 300 DPI TIFF/EPS | Separate .docx | Vancouver |
| Ann Plast Surg | 3,000 | 200, unstructured | 300 DPI TIFF | Embedded | AMA |

## Key Principles

1. **Sections as separate files** — enables parallel editing and targeted AI review
2. **Tables from data** — CSV is the source of truth; `.docx` is generated output
3. **Figures from code** — data-driven, reproducible, never hardcoded
4. **One build command** — `uv run python scripts/build_upload.py` generates everything
5. **Cross-references resolved at build time** — Quarto handles citations; build script handles table/figure numbering
