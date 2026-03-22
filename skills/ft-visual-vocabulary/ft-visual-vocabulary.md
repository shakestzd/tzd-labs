# FT Visual Vocabulary — Chart Selection Reference

Based on the Financial Times Visual Vocabulary by the FT Graphics team.
Source: https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary
Interactive version: https://ft-interactive.github.io/visual-vocabulary/

Use this as a decision framework: identify the **relationship type** in your data first,
then select a chart type from the matching category.

---

## The Nine Categories

### 1. Deviation
**Use when:** Emphasizing variations (+/-) from a fixed reference point — zero, a
target, a historical average, or a policy threshold.

| Chart type | When to prefer |
|:-----------|:---------------|
| Diverging bar | Comparing categories above/below a baseline |
| Surplus/deficit filled line | Time series where direction flips matter |
| Spine chart | Two-sided comparison (e.g., male/female, before/after) |
| Diverging stacked bar | Survey responses (agree/neutral/disagree) |

**Project applications:** FERC cost allocation (over/under socialization); PE fund
returns vs. regulated asset base returns; ratepayer bill impact (+/-).

**D3 reference:** https://observablehq.com/@d3/diverging-bar-chart

---

### 2. Correlation
**Use when:** Showing the relationship between two or more quantitative variables,
especially when the relationship itself is the story (not individual values).

| Chart type | When to prefer |
|:-----------|:---------------|
| Scatter plot | Two variables, individual points matter |
| Bubble chart | Three variables (x, y, size) |
| Connected scatter | Two variables over time (path tells the story) |
| XY heatmap | Two categorical + one quantitative variable |
| Column + line | Two different-scale variables over same time axis |

**Project applications:** Asset lifetime vs. demand visibility (the thesis-matrix
story — a scatter IS the right type here); capex vs. revenue growth; employment
concentration vs. poverty rate (DD-004 bimodal scatter).

**D3 reference:** https://observablehq.com/@d3/bubble-chart/2

**Warning:** Correlation charts are misread as causation. Always annotate the
relationship explicitly.

---

### 3. Ranking
**Use when:** An item's position in an ordered list matters more than its absolute
value. The reader should be asking "which is biggest/fastest/most?"

| Chart type | When to prefer |
|:-----------|:---------------|
| Bar / column (sorted) | Simple one-time ranking |
| Lollipop | Clean ranking with many items |
| Slope chart | Ranking that changes between two points in time |
| Bump chart | Rank changes across multiple time periods |
| Ordered bubble | Ranking with a second dimension (size) |

**Project applications:** States by data center employment (DD-003); companies by
capex share; utilities by rate base growth; PJM zones by 2030 demand growth.

**D3 reference:** https://observablehq.com/@d3/slope-chart/3

---

### 4. Distribution
**Use when:** The shape of the data — how values are spread, clustered, or skewed —
is the insight. Individual data points or summary statistics alone miss the story.

| Chart type | When to prefer |
|:-----------|:---------------|
| Histogram | Binned distribution of a continuous variable |
| Dot strip / beeswarm | Individual points, avoids binning artifacts |
| Box plot | Comparing distributions across categories |
| Violin plot | Distribution + density together |
| Population pyramid | Two-group age/time distribution |
| Cumulative curve | Threshold questions ("what % is below X?") |

**Project applications:** Data center investment per job distribution (DD-004);
interconnection queue project size distribution; wage distribution across occupations.

**D3 reference:** https://observablehq.com/@d3/beeswarm/2

---

### 5. Change Over Time
**Use when:** Trends, cycles, or temporal patterns are the story. The x-axis is
always time.

| Chart type | When to prefer |
|:-----------|:---------------|
| Line | Continuous trend; multiple series for comparison |
| Column | Discrete time periods; magnitude matters |
| Area / streamgraph | Cumulative or part-of-whole over time |
| Slope chart | Change between just two time points |
| Fan chart | Forecast uncertainty (confidence intervals) |
| Calendar heatmap | Daily/weekly patterns |
| Candlestick | Price volatility (OHLC) |

**Project applications:** AI capex trajectory (DD-001); employment index by sector
(DD-003); interconnection queue growth (DD-001-conversion); PJM zone demand
forecasts (DD-004).

**D3 reference:** https://observablehq.com/@d3/line-chart/2

**Warning:** Don't use area charts when series overlap and negatives aren't possible —
lines are cleaner. Streamgraphs obscure individual series; only use for 3-4 categories.

---

### 6. Magnitude
**Use when:** Comparing the size of things where absolute scale matters more than
ranking. The reader should feel the difference in size.

| Chart type | When to prefer |
|:-----------|:---------------|
| Bar / column | Single series, clear comparison |
| Paired bar | Two values per category |
| Isotype / pictogram | When raw numbers need humanizing scale |
| Marimekko / mosaic | Two-dimensional part-of-whole with variable widths |
| Lollipop | Many categories, clean alternative to bars |
| Bullet gauge | Performance against a target |

**Project applications:** Capex by company (DD-001 stacked bars); GW additions by
type; capital intensity comparisons (DD-004 capital-intensity.js); investment
announcements (DD-004 Indiana stat cards).

**D3 reference:** https://observablehq.com/@d3/bar-chart/2

---

### 7. Part-to-Whole
**Use when:** Showing how a single entity is broken down into its component parts.
Proportions are the story, not absolute magnitudes.

| Chart type | When to prefer |
|:-----------|:---------------|
| Stacked bar | Multiple categories over time or across groups |
| Waffle / unit chart | Proportions that need humanizing; each unit = 1 entity |
| Treemap | Many nested categories; screen space is limited |
| Waterfall | Sequential additions/subtractions to a running total |
| Pie / donut | ONLY for 2-3 categories where proportions are stark |
| Venn | Overlap / intersection between two groups |

**Project applications:** SPV ownership structure (DD-001-risk spv-chain); capex
share by company; liability exposure by bearer type; grid cost socialization split.

**Warning:** Avoid pie charts with more than 3 slices — use a horizontal bar instead.
Stacked bars with 5+ categories become unreadable for non-bottom layers.

---

### 8. Spatial
**Use when:** Location matters more than any other variable. The geographic pattern
IS the insight, not just context.

| Chart type | When to prefer |
|:-----------|:---------------|
| Choropleth | Continuous values by area (employment, rates) |
| Dot density | Individual counts placed by location |
| Graduated symbol / bubble map | Point data with a size dimension |
| Flow map | Movement between locations (capital, people) |
| Isopleth / contour | Continuous gradient across geography |

**Project applications:** Data center locations by operator (DD-003/DD-004 dc-map.js);
state employment by NAICS code; Virginia county cost geography (DD-004 virginia-map.js);
utility territory overlays.

**D3 reference:** https://observablehq.com/@d3/choropleth/2
TopoJSON: https://github.com/topojson/us-atlas

**Warning:** Use spatial only when geography IS the story. If you can convey the same
insight with a bar chart, prefer the bar chart — maps hide absolute differences.

---

### 9. Flow
**Use when:** Showing volumes or intensity of movement between two or more states,
conditions, or entities. The transformation itself is the story.

| Chart type | When to prefer |
|:-----------|:---------------|
| Sankey / alluvial | Volume flow through sequential stages |
| Chord diagram | Bidirectional flows between entities |
| Network / node-link | Relationships without clear direction |
| Waterfall | Sequential additions/subtractions (also Part-to-Whole) |

**Project applications:** Capital flow (COMMIT → CONVERT → LAND → DISTRIBUTE);
SPV ownership chain (DD-001-risk spv-chain.js); PE fund → HoldCo → Utility →
Ratepayer (DD-004 ownership-flow.js); CoreWeave → OpenAI → Microsoft dependency chain.

**D3 reference (Sankey):** https://observablehq.com/@d3/sankey/2

---

## Quick Decision Tree

```
What relationship am I showing?

├── Comparing to a reference/baseline?          → DEVIATION
│     e.g., above/below zero, target, average
│
├── Relationship between two variables?          → CORRELATION
│     e.g., lifetime vs demand visibility
│
├── Which is biggest / ranked?                   → RANKING
│     e.g., top states by employment
│
├── How is data spread / shaped?                 → DISTRIBUTION
│     e.g., project size distribution
│
├── How does something change over time?         → CHANGE OVER TIME
│     e.g., capex trajectory, employment index
│
├── How big is something (absolute size)?        → MAGNITUDE
│     e.g., capex by company, GW additions
│
├── What fraction / what's it made of?           → PART-TO-WHOLE
│     e.g., capex share, SPV ownership
│
├── Where is it located?                         → SPATIAL
│     e.g., data center map, utility territory
│
└── How does something flow / transform?         → FLOW
      e.g., capital chain, PE → utility → ratepayer
```

---

## Design Integration (Project-Specific)

### Observable design tokens for each category

| Category | Primary token | Secondary |
|:---------|:-------------|:----------|
| Deviation (positive) | `POSITIVE` (`#4a7c59`) | `CONTEXT` |
| Deviation (negative) | `NEGATIVE` (`#b84c2a`) | `CONTEXT` |
| Correlation — risk zone | `NEGATIVE` | `POSITIVE` for safe zone |
| Ranking — focus entity | `ACCENT` | `CONTEXT` for others |
| Distribution — highlight | `ACCENT` | `CONTEXT` |
| Change over time — focus series | `ACCENT` or company color | `CONTEXT` |
| Magnitude — comparison | `ACCENT` for story bar | `CONTEXT` for reference |
| Part-to-whole — story segment | `ACCENT` | `CONTEXT` |
| Spatial — story region | `ACCENT` | `CONTEXT` choropleth base |
| Flow — story path | `ACCENT` | `CONTEXT` background flows |

### Common anti-patterns to avoid

- Using a pie chart when there are more than 3 slices → use horizontal bars
- Using a 2x2 quadrant grid when a scatter with actual coordinates is clearer
- Using a line chart for categorical data (no inherent order) → use bars
- Using dual y-axes instead of two separate small multiples
- Stacked bars with 5+ categories where non-bottom layers are unreadable
- Choropleth when a bar chart would show the same ranking more clearly
