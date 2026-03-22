# SWD Makeover Examples Index

Maps common anti-patterns and chart problems to real SWD before/after makeover articles.
Full YAML index: `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/before-after-mapping.yaml`

---

## By Anti-Pattern

### Pie charts with too many slices
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/alternatives-to-pies.md`
**And:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/pie-chart-makeover.md`

Before: multiple pie charts comparing two time periods; hard to compare slices across pies.
After: 100% stacked horizontal bar, simple bar, slopegraph — four alternatives demonstrated.
Key lesson: Almost any pie chart can be replaced with a horizontal bar sorted by value.

---

### Cluttered chart (gridlines, borders, legend, no takeaway)
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/declutter-graphics.md`
**And:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/before-after-example.md`

Before: line chart with legend far from data, background shading, gridlines, borders, similar colors.
After: same data, direct labels, removed background clutter, distinct colors, labeled endpoints.
Key lesson: Remove everything that doesn't serve the story. What's left is the story.

---

### Lines vs. bars — wrong type for the data
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/bars-vs-lines.md`

Scenario 1 — bars beat lines: categorical data (makeup usage by type) visualized as a line chart. Problem: lines imply continuity between categories. Fix: horizontal bar chart.
Scenario 2 — lines beat bars: production data over time shown as bars. Fix: line chart with range shows trend clearly.
Key lesson: Lines encode continuous change. Bars encode discrete comparisons. Match the chart type to the data structure.

---

### When "novel" charts lose to the bar chart
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/dot-plot-vs-slopegraph-vs-bar.md`

Original: connected scatterplot comparing two companies across brand attributes. Nobody could read it.
Alternatives explored: dot plot, slopegraph, and (reluctantly) a bar chart.
Result: the "boring old bar chart" won — the audience preferred it over both novel alternatives.
Key lesson: Simple often beats complex. The chart type that your audience can read immediately is the right choice.

---

### Too many series / spaghetti line chart
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/trade-forecast-makeover.md`

Before: 15 individual country export/import lines in one chart. Unreadable.
After: gray shaded range (showing the spread) with one highlighted series; insight-driven title; annotations.
Key lesson: When you have many series, consider whether you need all of them. Use gray ranges for the distribution; highlight the one series that tells the story.

---

### Diverging bar chart scope creep
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/diverging-bar-makeover.md`

Before: diverging horizontal bars comparing hotel room bookings across 4 years and multiple cities. Impossible to compare.
After: combination of chart types, each making one specific point. Line chart for trend, bar for composition, slopegraph for year-over-year change.
Key lesson: One chart, one insight. If you need to make three points, use three charts.

---

### Combo chart / dual-axis confusion
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/combo-chart-makeover.md`

Before: line chart with data markers, unclear acronyms, tiny font.
After: line-area combination chart that uses the filled area to emphasize the gap between two series.
Key lesson: A combo chart is only justified when the relationship between two series IS the story — not just because you have two series.

---

### Stacked area chart obscuring individual series
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/multitudes-of-makeovers.md`

Original prompt: confusing stacked area chart with 5 subscription categories. 67 community makeovers.
Community approaches: bar charts, horizontal bars, small multiples, line charts.
Key lesson: When individual series trends matter, don't stack. Use small multiples or a focused line chart with the rest grayed out.

---

### Chart that needs a slopegraph
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/slopegraph-visualization.md`

Before: multiple bar charts for market share by state across two years. Hard to see change.
After: slopegraph — left axis is 2010, right axis is 2017. Slope of each line shows change direction and magnitude immediately.
Key lesson: When you need to show change between two points for many categories, a slopegraph beats paired bars.

---

### 3D charts, default colors, cluttered labels
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/income-expenses-makeover.md`

Before: six 3D bar charts with rotation, gridlines, default rainbow colors, no clear takeaway.
After: flat horizontal bar chart with intentional colors, active title stating the insight.
Key lesson: Remove every default tool setting. 3D never helps. Active titles that state the conclusion are always better than descriptive labels.

---

### Super Bowl ads — rainbow stacked bars
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/super-bowl-makeover.md`

Before: rainbow-colored stacked bar chart, alphabetical sort, diagonal labels.
After: small multiples area chart, each industry on its own panel, sorted by meaningful order.
Key lesson: When you have many categories over time, small multiples are almost always better than a combined chart. Each panel is simple; together they tell the full story.

---

## Community Challenge Examples (Many before/after pairs)

### 96 makeovers from the same starting dual pie chart
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/swdchallenge-makeover-sept2018.md`

Starting point: dual pie chart showing regional tourism GDP share in 2000 vs. 2016.
Community solutions: ~50% used slopegraphs, ~50% used dot plots, bars, diverging bars, bullet bars.
Useful for: seeing many different valid approaches to the same problem.

### 45 community makeovers from "your choice"
**Read:** `https://gist.githubusercontent.com/shakestzd/a4b156c29d82030236b40c1b6e02cf87/raw/swdchallenge-makeover-recap-july2018.md`

Various starting charts. Common transformations: pie → bar, bubble → bar, connected scatter → dot plot.
Useful for: seeing a broad variety of real-world before/after transformations.
