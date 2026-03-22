---
name: flowmpl-design-system
description: Use this skill when creating charts, applying the flowmpl design system, using concept frames, generating AI illustrations, working with palettes, or needing the full flowmpl API reference beyond flow diagrams. Triggers on "create a chart", "flowmpl chart", "design system", "concept frame", "AI illustration", "flowmpl palettes", "stacked bar", "waterfall chart", "annotated series", "flowmpl colors".
---

# flowmpl Design System

Complete reference for flowmpl — the matplotlib design system and visualization toolkit for analytical publications. Covers charts, palettes, helpers, concept frames, illustrations, icons, and maps. For detailed flow diagram documentation, see the `flowmpl-flow-diagram` skill.

## Installation

```bash
uv pip install flowmpl          # Core (design tokens + flow diagrams)
uv pip install flowmpl[charts]  # + pandas chart functions
uv pip install flowmpl[maps]    # + US scatter map (geopandas)
uv pip install flowmpl[icons]   # + icon fetching (pyconify)
uv pip install flowmpl[gemini]  # + AI illustrations (Gemini 3 Pro Image)
uv pip install flowmpl[all]     # Everything
```

## Design Tokens

Apply the design system globally:

```python
from flowmpl import apply_style, COLORS, CONTEXT, FONTS, FIGSIZE
apply_style()  # Sets matplotlib rcParams
```

### Colors (Semantic Roles)

| Token | Role | Use |
|-------|------|-----|
| `COLORS["accent"]` | Primary story color | Focal elements, key data series |
| `COLORS["positive"]` | Good / confirmed | Growth, success, verified |
| `COLORS["negative"]` | Bad / risk | Decline, failure, danger |
| `COLORS["neutral"]` | Neither good nor bad | Speculative, pending |
| `COLORS["muted"]` | Secondary / supporting | Background data, annotations |
| `COLORS["reference"]` | Reference lines | Benchmarks, thresholds |
| `COLORS["text_dark"]` | Dark text | Labels on light backgrounds |
| `COLORS["text_light"]` | Light text | Labels on dark fills |
| `COLORS["background"]` | Figure background | Canvas |
| `COLORS["grid"]` | Grid lines | Subtle grid |
| `CONTEXT` | SWD gray | Non-focus elements (gray-out pattern) |

### Site Identity Tokens

For web publication consistency: `PAPER`, `INK`, `INK_MID`, `INK_LIGHT`, `RULE` — map 1:1 to CSS custom properties.

### Palettes

```python
from flowmpl import CATEGORICAL, COMPANY_COLORS, FUEL_COLORS, company_color, fuel_color

CATEGORICAL           # 8-color Paul Tol colorblind-safe palette
COMPANY_COLORS        # Dict: MSFT, AMZN, GOOGL, NVDA, TSLA, META, AAPL, ORCL
FUEL_COLORS           # Dict: solar, wind, gas, nuclear, hydro, coal, oil, battery, other
company_color("NVDA") # Get company color by ticker
fuel_color("solar")   # Get fuel type color
```

## Chart Functions

All chart functions return `matplotlib.Figure` objects. Require `flowmpl[charts]`.

### annotated_series() — Time series with annotations

```python
from flowmpl import annotated_series
fig = annotated_series(
    df, x="date", y="value",
    annotations=[{"x": "2024-01", "text": "Event", "color": COLORS["accent"]}],
    fill_between=True,
)
```

### stacked_bar() — Categorical breakdowns

```python
from flowmpl import stacked_bar
fig = stacked_bar(df, x="category", columns=["A", "B", "C"], colors=[...])
```

### waterfall_chart() — Cost allocation / flow breakdowns

```python
from flowmpl import waterfall_chart
fig = waterfall_chart(labels=["Start", "+Revenue", "-Costs", "End"], values=[100, 50, -30, 120])
```

### horizontal_bar_ranking() — Ranked bars with highlights

```python
from flowmpl import horizontal_bar_ranking
fig = horizontal_bar_ranking(df, label_col="name", value_col="score", highlight=["Top Item"])
```

### multi_panel() — Multiple subplots from single DataFrame

```python
from flowmpl import multi_panel
fig = multi_panel(df, x="date", y_columns=["metric_a", "metric_b", "metric_c"])
```

## Helper Functions

### SWD Gray-Out Pattern

```python
from flowmpl import focus_colors
colors = focus_colors(
    labels=["A", "B", "C", "D"],
    focus=["B"],           # Items to highlight
    focus_color=COLORS["accent"],
)
# Returns: {A: gray, B: accent, C: gray, D: gray}
```

### Annotations and Formatting

```python
from flowmpl import chart_title, annotate_point, reference_line, legend_below, add_rule, add_source, add_brand_mark

chart_title(ax, "Main insight as title")           # Left-aligned insight title
annotate_point(ax, x, y, "Label", color=...)        # Arrow + text annotation
reference_line(ax, y=50, label="Benchmark")          # Labeled reference line
legend_below(ax, ncol=3)                             # Legend below axes
add_rule(fig)                                         # Horizontal rule below title
add_source(fig, "Source: EIA")                        # Source attribution
add_brand_mark(fig, "TZD Labs")                       # Brand mark
```

## Concept Frames (Whiteboard Explainers)

Visual explainer frames for educational content — combine programmatic layout with PNG sketch assets.

```python
from flowmpl import (
    section_intro_frame,   # Yellow bg, large number, white card + icons
    concept_frame,         # White bg, center card + surrounding icons + dashed arrows
    comparison_frame,      # Split-screen (promise/reality, left/right)
    cascade_frame,         # Horizontal step sequence
    data_moment_frame,     # Oversized stat callout + icon pairs
    rhetorical_frame,      # Question/answer reveal
    chart_scene_frame,     # Chart with contextual annotations
)
```

### Example: Section Intro

```python
fig = section_intro_frame(
    section_number=3,
    title="Energy Infrastructure",
    subtitle="Grid modernization and capacity expansion",
    icons=["lightning.png", "factory.png", "pipeline.png"],
)
```

## AI-Generated Illustrations

Compose AI-generated sketches with programmatic layout. Requires `flowmpl[gemini]`.

```python
from flowmpl import generate_illustration, generate_illustrations, remove_background, annotate_illustration

# Generate single sketch (no text in image to avoid typos)
img = generate_illustration(
    prompt="watercolor sketch of a power transformer",
    style="editorial ink wash",
)

# Batch generate
images = generate_illustrations(prompts=[...], style="editorial ink wash")

# Post-process
img = remove_background(img)
fig = annotate_illustration(img, annotations=[{"text": "Label", "xy": (0.5, 0.1)}])
```

## Icons and Maps

```python
from flowmpl import fetch_icon, load_icon, us_scatter_map

# Icons (requires flowmpl[icons])
icon = fetch_icon("mdi:lightning-bolt", color=COLORS["accent"])
icon = load_icon("path/to/icon.png")

# US scatter map (requires flowmpl[maps])
fig = us_scatter_map(df, lat="latitude", lon="longitude", size="capacity_mw")
```

## Integration with Marimo Notebooks

```python
import marimo as mo
from flowmpl import apply_style, COLORS, CONTEXT, FIGSIZE, annotated_series

apply_style()

@app.cell
def _(df, COLORS, annotated_series, mo):
    fig = annotated_series(df, x="date", y="value")
    fig.savefig("output.png", dpi=150, bbox_inches="tight")
    return mo.image("output.png")
```
