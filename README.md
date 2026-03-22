# TZD Labs

A Claude Code plugin providing a complete research and publication pipeline — from data extraction through analysis, visualization, writing, peer review, and journal submission.

## What It Does

TZD Labs is a curated collection of **14 specialized agents**, **12 knowledge skills**, and **5 slash commands** that cover the full research lifecycle:

**Extract** data from PDFs, regulatory filings, and academic papers
**Analyze** in reactive marimo notebooks with verified data integrity
**Visualize** with publication-ready charts, flow diagrams, and medical figures
**Write** with accountability-cascade prose style and AI-tell detection
**Review** through parallel peer review agents (critic, fact-checker, prose-reviewer)
**Publish** to journals (Quarto + quartopress pipeline) or the web (Observable Framework)

## Installation

```bash
# Clone the plugin
git clone https://github.com/shakestzd/tzd-labs.git

# Install as a Claude Code plugin
claude --plugin-dir /path/to/tzd-labs
```

### Recommended packages

```bash
# Core visualization
uv pip install flowmpl[all]

# Manuscript pipeline
uv pip install quartopress

# Medical figure export
uv pip install prs-dataviz

# Elegant visualization palettes
uv pip install dubois-style
```

## Agents

### Writing & Review
| Agent | What It Does |
|-------|-------------|
| `critic` | Peer review for analytical rigor, logic, and evidence quality |
| `writer` | Transform analysis into accessible, publication-ready narrative |
| `prose-reviewer` | Structural narration quality assessment (show vs tell) |
| `ai-tell-fixer` | Detect and fix AI writing markers (overused words, em-dashes, generic transitions) |
| `manuscript-reviewer` | Verify manuscript sections against journal requirements and reviewer comments |

### Data & Verification
| Agent | What It Does |
|-------|-------------|
| `researcher` | Find primary data sources, validate empirical claims against government databases and filings |
| `fact-checker` | Verify every factual claim, number, date, and citation before publication |
| `notebook-qa` | Verify data integrity in marimo notebooks — catches hardcoded values, stale prose, chart/data mismatches |

### Visualization & Publication
| Agent | What It Does |
|-------|-------------|
| `swd-reviewer` | Review charts for Storytelling with Data compliance and FT Visual Vocabulary alignment |
| `observable-converter` | Convert marimo charts to Observable Framework scroll-driven articles |
| `marimo-editor` | Make code changes to marimo notebooks following design system conventions |
| `table-builder` | Generate PRS-formatted Word tables from CSV data with three-line borders |

### Extraction & Generation
| Agent | What It Does |
|-------|-------------|
| `pdf-extractor` | Extract structured data from PDFs using Mistral OCR |
| `notebooklm-prompt-generator` | Generate NotebookLM Audio Overview prompts for educational chapters |

## Skills

### Visualization
- **flowmpl-design-system** — Complete flowmpl API reference (charts, palettes, concept frames, illustrations, maps)
- **flowmpl-flow-diagram** — Detailed flow_diagram() reference with routing heuristics and face overrides
- **swd-chart-guide** — Storytelling with Data chart selection, decluttering, and makeover methodology
- **ft-visual-vocabulary** — Financial Times chart selection framework across 9 data relationship categories
- **prs-dataviz** — Journal-compliant medical figure export (300+ DPI, CMYK, accessibility-first)

### Writing & Publication
- **accountability-cascade** — Prose style that traces actor decisions through chains of consequence
- **manuscript-setup** — Scaffold Quarto manuscript projects with quartopress
- **journal-compliance** — Journal-specific submission checklists (PRS, JPRAS, Annals)
- **build-upload** — Build pipeline for generating complete journal upload packages
- **observable-scroll-annotations** — SVG-native scroll annotation patterns for D3 charts

### Reference
- **research-toolkit** — Unified index mapping research tasks to the right tools
- **step1-notebooklm-guide** — USMLE Step 1 domain knowledge for podcast prompt generation

## Commands

| Command | Purpose |
|---------|---------|
| `/build-manuscript` | Build the complete journal upload package |
| `/fix-ai-tells` | Scan and fix AI writing tells across manuscript files |
| `/fix-manuscript` | Fix rendering issues (double titles, stale cross-refs, terminology) |
| `/set-journal <prs\|jpras\|annals>` | Configure manuscript for a specific journal's template |
| `/generate-notebooklm-prompt` | Generate a NotebookLM Audio Overview prompt for a chapter |

## Integrated Packages

TZD Labs brings together several specialized packages:

| Package | Purpose | Install |
|---------|---------|---------|
| [flowmpl](https://github.com/shakestzd/flowmpl) | Matplotlib design system and flow diagram renderer | `uv pip install flowmpl[all]` |
| [quartopress](https://github.com/shakestzd/quartopress) | Quarto manuscript pipeline and PRS table builder | `uv pip install quartopress` |
| prs-dataviz | Medical figure export (CMYK, TIFF, 300 DPI) | `uv pip install prs-dataviz` |
| dubois-style | W.E.B. Du Bois-inspired matplotlib palettes | `uv pip install dubois-style` |

## Example Workflows

### Write and submit a journal paper

```
1. /set-journal prs                    # Configure for PRS
2. [write sections in _sections/*.qmd]
3. /fix-ai-tells                       # Clean AI markers
4. [launch manuscript-reviewer agent]  # Check compliance
5. /build-manuscript                   # Generate upload package
```

### Analyze infrastructure data

```
1. [launch researcher agent]           # Find primary data sources
2. [launch pdf-extractor agent]        # Extract from filings
3. [build marimo notebook]             # Interactive analysis
4. [launch notebook-qa agent]          # Verify data integrity
5. [launch critic + fact-checker]      # Parallel review
6. [launch writer agent]              # Polish narrative
```

## Author

**Thandolwethu Zwelakhe Dlamini**

## License

MIT
