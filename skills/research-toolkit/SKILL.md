---
name: research-toolkit
description: Use this skill to find the right tool for a research task across the TZD Labs ecosystem. Maps research needs (visualization, manuscript writing, data extraction, systematic review, analysis) to specific tools, packages, and agents. Triggers on "what tool should I use", "how do I do X", "research workflow", "which agent", "find the right tool", "project index".
---

# Research Toolkit

Unified index of all research tools, libraries, and capabilities available across the TZD Labs ecosystem. Use this skill to find the right tool for a research task.

## Tool Index

### Data Visualization

| Tool | What It Does | Install / Location |
|------|-------------|-------------------|
| **flowmpl** | Matplotlib design system — charts, flow diagrams, concept frames, AI illustrations | `uv pip install flowmpl[all]` |
| **prs-dataviz** | Journal-compliant medical figures (300+ DPI, CMYK, TIFF) | `uv pip install prs-dataviz` |
| **dubois-style** | W.E.B. Du Bois-inspired matplotlib palettes (7 color schemes) | `uv pip install dubois-style` |
| **infographic-generator** | Modular infographic generation (Typst rendering, AI images) | `/Users/shakes/DevProjects/infographic-generator` |

### Manuscript Pipeline

| Tool | What It Does | Install / Location |
|------|-------------|-------------------|
| **quartopress** | Quarto manuscript scaffolding, PRS table builder, build pipeline | `uv pip install quartopress` |
| **plastic-surgery-research** | PRS manuscript writing guidance + dataviz best practices | Claude plugin at `/Users/shakes/DevProjects/plastic-surgery-research` |

### Data Extraction & Processing

| Tool | What It Does | Install / Location |
|------|-------------|-------------------|
| **ai-structured-data-extractor** | Systematic literature review — PRISMA screening, citation extraction | `/Users/shakes/DevProjects/ai-structured-data-extractor` |
| **markdown-table-extractor** | Extract and transform tables from markdown documents | `/Users/shakes/DevProjects/markdown_table_extractor` |
| **pdf-extractor** (agent) | Mistral OCR for PDFs — regulatory filings, financial reports, utility orders | Built-in tzd-labs agent |
| **paperquizr** | Interactive paper reader with gated quiz stages and concept mapping | `/Users/shakes/DevProjects/paperquizr` |

### Interactive Notebooks

| Tool | What It Does | Install / Location |
|------|-------------|-------------------|
| **marimo** | Reactive Python notebooks — charts, data analysis, interactive UI | `uv pip install marimo` |
| **Observable Framework** | D3.js-based web publication — scroll-driven charts, responsive design | Integrated via observable-converter agent |

### Analysis & Research

| Tool | What It Does | Install / Location |
|------|-------------|-------------------|
| **causal-compass** | Causal inference methodology and analysis | `/Users/shakes/DevProjects/causal-compass` |
| **SystemDynamics** | System dynamics modeling and simulation | `/Users/shakes/DevProjects/SystemDynamics` |
| **van-research** | Parameterized financial analysis with Quarto reports | `/Users/shakes/DevProjects/van_research` |

### Document Collaboration

| Tool | What It Does | Install / Location |
|------|-------------|-------------------|
| **docucolab** | Document collaboration platform | `/Users/shakes/DevProjects/docucolab` |
| **docucolab-parallel-docx** | Parallel DOCX document processing | `/Users/shakes/DevProjects/docucolab-parallel-docx` |
| **docucolab-parallel-pptx** | Parallel PPTX presentation processing | `/Users/shakes/DevProjects/docucolab-parallel-pptx` |

### Education

| Tool | What It Does | Install / Location |
|------|-------------|-------------------|
| **survival-guide** | USMLE Step 1 study material with OCR extraction | `/Users/shakes/DevProjects/survival_guide` |
| **NotebookLM prompts** | Generate Audio Overview prompts for educational chapters | Built-in tzd-labs agent + command |

## Task-to-Tool Routing

### "I need to create a publication figure"
1. Use **flowmpl** for the chart (`annotated_series`, `stacked_bar`, `waterfall_chart`, `flow_diagram`)
2. Apply **prs-dataviz** for journal-compliant export (TIFF, 300 DPI, CMYK)
3. Use **dubois-style** if you want historically-inspired aesthetics

### "I need to write a manuscript"
1. Scaffold with **quartopress** (`quartopress-init`)
2. Configure journal with `/set-journal`
3. Build tables with **table-builder** agent
4. Create figures with **flowmpl** + **prs-dataviz**
5. Fix AI tells with `/fix-ai-tells`
6. Check compliance with **journal-compliance** skill
7. Build upload package with `/build-manuscript`

### "I need to do a systematic review"
1. Set up screening database with **ai-structured-data-extractor**
2. Extract data from PDFs with **pdf-extractor** agent
3. Extract tables with **markdown-table-extractor**
4. Analyze with **marimo** notebooks
5. Visualize with **flowmpl** (PRISMA flowchart via `flow_diagram`)
6. Write up with **quartopress**

### "I need to analyze infrastructure data"
1. Research with **researcher** agent (finds primary data sources)
2. Extract from PDFs with **pdf-extractor** agent
3. Analyze in **marimo** notebooks
4. Visualize with **flowmpl** design system
5. Write with **accountability-cascade** prose style
6. Review with **critic** + **fact-checker** agents
7. Publish via **Observable Framework** (observable-converter agent)

### "I need to review my writing"
1. **prose-reviewer** agent — structural narration quality (show vs tell)
2. **ai-tell-fixer** agent — detect and fix AI writing markers
3. **critic** agent — intellectual rigor, logic, evidence quality
4. **writer** agent — transform into accessible publication-ready narrative
5. **swd-reviewer** agent — chart/visualization quality (Storytelling with Data)
6. **fact-checker** agent — verify every claim, number, citation

### "I need to create a presentation or infographic"
1. Use **infographic-generator** for standalone infographics
2. Use **flowmpl** concept frames for whiteboard-style explainers
3. Use **docucolab-parallel-pptx** for PowerPoint processing
