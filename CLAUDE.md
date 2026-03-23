# TZD Labs — Research & Publication Hub

This is the entry point for all research, analysis, visualization, and publication workflows across TZD Labs projects.

## Quick Start

**What do you need?**

| Task | Start Here |
|------|-----------|
| Create a chart or figure | `flowmpl-design-system` skill or `flowmpl-flow-diagram` skill |
| Write a manuscript | `manuscript-setup` skill, then `/build-manuscript` |
| Fix AI writing | `/fix-ai-tells` command |
| Review writing quality | `prose-reviewer`, `critic`, or `writer` agent |
| Verify facts/data | `fact-checker` or `researcher` agent |
| Extract data from PDF | `pdf-extractor` agent |
| Create journal-ready figures | `prs-dataviz` skill |
| Find the right tool | `research-toolkit` skill |

## Agents (14)

### Writing & Review Pipeline
| Agent | Purpose | Trigger |
|-------|---------|---------|
| **critic** | Peer review for analytical rigor, logic, evidence quality | "review this for rigor", "check the logic" |
| **writer** | Transform analysis into accessible publication-ready narrative | "rewrite for publication", "make this readable" |
| **prose-reviewer** | Structural narration quality (show vs tell framework) | "review the prose", "check narrative quality" |
| **ai-tell-fixer** | Detect and fix AI writing markers in manuscripts | "fix AI tells", "scan for AI writing" |
| **manuscript-reviewer** | Verify manuscript meets journal requirements | "check PRS compliance", "review against reviewer comments" |

### Data & Verification
| Agent | Purpose | Trigger |
|-------|---------|---------|
| **researcher** | Find primary data sources, validate empirical claims | "find data on X", "validate this claim" |
| **fact-checker** | Verify every factual claim, number, citation | "verify the claims", "check these numbers" |
| **notebook-qa** | Verify data integrity in marimo notebooks | "run QA on the notebook" |

### Visualization & Publication
| Agent | Purpose | Trigger |
|-------|---------|---------|
| **swd-reviewer** | Review charts for Storytelling with Data compliance | "review this chart", "check visualization quality" |
| **observable-converter** | Convert marimo charts to Observable Framework articles | "convert to Observable" |
| **marimo-editor** | Make code changes to marimo notebooks | "update the notebook code" |
| **table-builder** | Generate PRS-formatted Word tables from CSV data | "build Table 1 from CSV" |

### Extraction & Generation
| Agent | Purpose | Trigger |
|-------|---------|---------|
| **pdf-extractor** | Extract structured data from PDFs using Mistral OCR | "extract data from this PDF" |
| **notebooklm-prompt-generator** | Generate NotebookLM Audio Overview prompts | "generate NotebookLM prompt for chapter X" |

## Skills (12)

### Visualization
- **flowmpl-design-system** — Full flowmpl API: charts, palettes, helpers, concept frames, illustrations, maps
- **flowmpl-flow-diagram** — Detailed flow_diagram() reference: nodes, edges, routing, face overrides
- **swd-chart-guide** — Storytelling with Data chart selection and decluttering methodology
- **ft-visual-vocabulary** — Financial Times chart selection framework (9 categories)
- **prs-dataviz** — Journal-compliant medical figure export (300+ DPI, CMYK, TIFF)

### Writing & Publication
- **accountability-cascade** — Default prose style: named actors, active verbs, chain-of-causation structure
- **manuscript-setup** — Scaffold Quarto manuscript projects with quartopress
- **journal-compliance** — Journal-specific submission requirement checklists
- **build-upload** — Build pipeline for generating complete upload packages
- **parameterized-manuscript** — Stats dataclass pattern: no hardcoded numbers in prose, template sync, validation
- **observable-scroll-annotations** — SVG-native scroll annotations for Observable Framework charts

### Reference
- **research-toolkit** — Unified index of all DevProjects tools and task-to-tool routing
- **step1-notebooklm-guide** — USMLE Step 1 domain knowledge for NotebookLM prompts

## Commands (5)

| Command | Purpose |
|---------|---------|
| `/generate-notebooklm-prompt` | Generate NotebookLM Audio Overview prompt for a chapter |
| `/build-manuscript` | Build complete journal upload package from source files |
| `/fix-ai-tells` | Scan and fix AI writing tells across all .qmd files |
| `/fix-manuscript` | Detect and fix rendering issues (double titles, stale refs, terminology, hardcoded numbers) |
| `/set-journal` | Configure manuscript for specific journal template (PRS, JPRAS, Annals) |

## Cross-Project Integration

This plugin integrates capabilities from across the DevProjects ecosystem:

| Package | Capability | Status |
|---------|-----------|--------|
| [flowmpl](https://github.com/shakestzd/flowmpl) | Design system, charts, flow diagrams, concept frames | `uv pip install flowmpl[all]` |
| [quartopress](https://github.com/shakestzd/quartopress) | Manuscript pipeline, table builder, journal templates | `uv pip install quartopress` |
| prs-dataviz | Medical figure export (CMYK, TIFF, 300 DPI) | `uv pip install prs-dataviz` |
| dubois-style | W.E.B. Du Bois-inspired matplotlib palettes | `uv pip install dubois-style` |
| ai-structured-data-extractor | Systematic literature review infrastructure | Local project |
| plastic-surgery-research | PRS manuscript writing + dataviz guidance | Claude plugin |

## Workflow Patterns

### Publication Pipeline (typical sequence)
1. `manuscript-setup` skill → scaffold project
2. `/set-journal prs` → configure for target journal
3. `table-builder` agent → generate tables from CSV
4. flowmpl + prs-dataviz → create figures
5. `ai-tell-fixer` agent → clean AI writing markers
6. `manuscript-reviewer` agent → check compliance
7. `/build-manuscript` → generate upload package

### Research & Analysis Pipeline
1. `researcher` agent → find primary data sources
2. `pdf-extractor` agent → extract from regulatory filings
3. `marimo-editor` agent → build analysis notebooks
4. `notebook-qa` agent → verify data integrity
5. `critic` + `fact-checker` agents → review rigor and accuracy
6. `writer` agent → polish for publication
7. `observable-converter` agent → publish to web

## Python Execution

Always use `uv` for Python operations:
```bash
uv run python script.py     # Run scripts
uv run pytest               # Run tests
uv pip install package      # Install packages
```
