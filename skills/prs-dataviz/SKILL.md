---
name: prs-dataviz
description: Use this skill when creating publication-quality figures for medical journals, exporting figures as TIFF/CMYK at 300+ DPI, using medical color palettes, adding scale bars, or formatting statistical annotations. Triggers on "journal figure", "PRS figure", "medical figure", "TIFF export", "CMYK", "300 DPI", "publication figure", "scale bar", "significance brackets".
---

# PRS Data Visualization

Create publication-quality figures meeting plastic surgery journal submission requirements. Uses the prs-dataviz package for journal-compliant figure export with medical-focused color palettes and accessibility-first design.

## Installation

```bash
uv pip install prs-dataviz
```

## When to Use

Use this skill when creating figures for:
- PRS (Plastic and Reconstructive Surgery)
- JPRAS
- Annals of Plastic Surgery
- Journal of Craniofacial Surgery
- Any medical journal requiring 300+ DPI figures

## Export Requirements by Journal

| Journal | Format | DPI | Color Mode | Max Size |
|---------|--------|-----|------------|----------|
| PRS | TIFF | 300+ | CMYK | 7" x 9.5" |
| JPRAS | TIFF/EPS/PDF | 300+ | CMYK | 170mm x 240mm |
| Annals | TIFF | 300+ | CMYK | 7" x 9" |

## Key Capabilities

### Journal-Compliant Export

```python
from prs_dataviz import export_figure

export_figure(
    fig,
    "Figure 1.tiff",
    dpi=300,
    color_mode="cmyk",    # Auto-converts RGB to CMYK
    max_width_inches=7,
    max_height_inches=9.5,
)
```

### Medical Color Palettes

- **Clinical Blue** — standard medical/surgical palette
- **Tissue Tone** — skin and tissue representation
- **Outcome Gradient** — poor-to-excellent outcome visualization
- **Complication Severity** — minor to major complication coding

### Specialized Layouts

- **Before/After** — side-by-side clinical photo comparison
- **Multi-View** — anterior/lateral/oblique views
- **Time Series** — outcome measurements over follow-up periods
- **Flowchart** — CONSORT/STROBE patient flow diagrams

### Accessibility (Cara Thompson's 10-Step Methodology)

1. Colorblind-safe palettes (tested with deuteranopia, protanopia, tritanopia simulations)
2. Sufficient contrast ratios (WCAG AA minimum)
3. Pattern fills as backup for color coding
4. Clear, readable font sizes at print scale
5. Alt-text generation for figure legends

### Scale Bar Automation

```python
from prs_dataviz import add_scale_bar

add_scale_bar(ax, length_mm=10, location="lower right")
```

### Statistical Formatting

```python
from prs_dataviz import format_p_value, add_significance_brackets

format_p_value(0.0023)  # "p = 0.002"
format_p_value(0.00004) # "p < 0.001"
add_significance_brackets(ax, pairs=[(0, 1), (1, 2)], p_values=[0.03, 0.001])
```

## Integration with flowmpl

prs-dataviz can layer on top of flowmpl's design system:

```python
from flowmpl import apply_style, COLORS
from prs_dataviz import export_figure

apply_style()  # Base design tokens
# Create figure using flowmpl charts...
export_figure(fig, "Figure 1.tiff", dpi=300, color_mode="cmyk")
```
