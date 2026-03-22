---
name: swd-chart-guide
description: Storytelling with Data chart guidance. Use when choosing chart types, evaluating whether a chart communicates clearly, reviewing data visualizations for SWD compliance, proposing chart alternatives, or when the user asks "what chart should I use", "is this chart working", "how do I improve this chart", "show me a makeover example", or describes a visualization problem.
argument-hint: "[chart type, anti-pattern, or description of visualization problem]"
---

Storytelling with Data (SWD) chart selection and decluttering guidance from Cole Nussbaumer Knaflic.

## Core SWD Principles

**The one insight rule:** Every chart communicates exactly one thing. If you can't state the insight as a single declarative sentence, the chart is trying to do too much.

**The 5-second test:** A reader with no context identifies the main point within five seconds. If they can't, the visual hierarchy is wrong.

**Color = meaning, not decoration:** Start with gray for everything. Add color only to the element that carries the story. Never use color for categories unless each color encodes a specific meaning.

**Declutter ruthlessly:**
- Remove gridlines (or make them barely visible)
- Remove chart borders
- Remove unnecessary tick marks
- Move the legend into the chart as direct labels
- Never use 3D effects, shadows, or gradients
- Never use pie charts with more than 2-3 slices

**Prose coherence:** The title above the chart IS the insight sentence. If the title says "Revenue over time" but the point is "Revenue fell 40% after the policy change", the title is wrong. Titles should be declarative, not descriptive.

## When to Use Which Chart

See [chart-index.md](chart-index.md) for the full guide:
- When to use each chart type
- Common mistakes for each type
- Path to the full SWD guide for each chart

Quick reference:

| Use case | Chart type |
|:---------|:-----------|
| Comparing categories at one point in time | Horizontal bar (sorted by value) |
| Showing change over time | Line chart |
| Showing composition / part of whole | Stacked bar (max 3-4 categories), or waffle |
| Comparing two groups across attributes | Dot plot or slopegraph |
| Showing before/after or two time points | Slopegraph |
| Distribution of a continuous variable | Histogram or dot strip |
| Relationship between two variables | Scatterplot |
| Sequential additions/subtractions | Waterfall chart |
| Flow between states | Sankey diagram |

**Never use** (and what to use instead):
- Pie chart with 4+ slices → horizontal bar sorted by value
- 3D bar or 3D pie → flat equivalent
- Dual y-axis → two separate charts or index to a common baseline
- Spider/radar chart → small multiples or dot plot
- Bubble chart for 3+ series → small multiples

## Before/After Makeover Examples

See [makeover-index.md](makeover-index.md) for the full index.

When a chart has a specific problem, find the matching makeover example to show the before/after transformation. The index maps anti-patterns to real SWD makeovers.

Key examples:
- **Pie chart → bar chart:** `pie-chart-makeover`, `alternatives-to-pies`
- **Cluttered line chart → focused:** `declutter-graphics`, `trade-forecast-makeover`
- **Bars vs. lines decision:** `bars-vs-lines`
- **Dot plot vs. slopegraph vs. bar:** `dot-plot-vs-slopegraph-vs-bar`
- **Stacked area → focused:** `multitudes-of-makeovers`, `combo-chart-makeover`
- **Diverging bar problems:** `diverging-bar-makeover`

## Full Reference Files

All content is hosted as public GitHub Gists. Use WebFetch to load any file on demand.

**Chart guides gist** (20 files):
`https://gist.github.com/shakestzd/ecf5012aec9466110ca39371b9a527c7`

Raw URL pattern: `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/<filename>`

**Makeover examples gist** (15 articles + YAML index):
`https://gist.github.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87`

Raw URL pattern: `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/<filename>`

Load any specific file on demand using WebFetch when deeper guidance is needed.
