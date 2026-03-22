# SWD Chart Guide Index

Each entry: when to use, key rules, common mistakes, and path to the full guide.

---

## Bar Chart
**Use when:** Comparing categorical data or data sorted into groups at one point in time.

**Key rules:**
- Horizontal bars are preferred for long category names
- Always start at zero baseline — never truncate
- Sort by value (descending) unless there is a natural order
- Use vertical bars (column charts) only for time series with few data points

**Common mistakes:** Alphabetical sort, truncated y-axis, too many clustered series, 3D effects.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/bar-chart.md`

---

## Stacked Bar Chart
**Use when:** Showing composition (part-of-whole) across multiple categories, or how composition changes over time.

**Key rules:**
- Maximum 3-4 categories; beyond that, readers can't compare non-baseline segments
- 100% stacked bar is better for relative proportions (survey data, before/after)
- The bottom segment is the only one with a shared baseline — make it the most important

**Common mistakes:** Too many stacked categories, rainbow colors, no clear baseline segment.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/stacked-bar-chart.md`

---

## Line Graph
**Use when:** Showing continuous change over time; the connection between data points implies continuity.

**Key rules:**
- Only use lines for continuous data (time series); don't connect categorical data
- Annotate the line directly; avoid separate legends
- Highlight one line in accent color, gray all others
- Use area fill sparingly (only when cumulative total matters)

**Common mistakes:** Too many series (spaghetti), connecting categorical data with lines, dual y-axes.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/line-graph.md`

---

## Area Graph
**Use when:** Showing cumulative totals or emphasizing volume over time; when the area under the line matters.

**Key rules:**
- Use only when cumulative quantity is meaningful — not just as a "decorated line chart"
- Never overlap more than 2-3 series
- Stacked area requires careful color and a clear total

**Common mistakes:** Using area chart when a line chart would be cleaner, stacking 5+ series.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/area-graph.md`

---

## Scatterplot
**Use when:** Showing the relationship between two continuous variables; correlation is the story.

**Key rules:**
- Label outliers or interesting points directly
- Add a reference line (regression line or diagonal) only when it helps the reader
- Color-encode a third variable sparingly

**Common mistakes:** Too many data points without clustering, unlabeled outliers, no reference lines.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/scatterplot.md`

---

## Dot Plot (Cleveland)
**Use when:** Comparing two or more groups across multiple attributes; alternative to clustered bars.

**Key rules:**
- Sort rows by one group's values (usually the focal group)
- Connect dots with a line to show the gap — the gap IS the story
- Use for comparisons that would require too many clustered bar groups

**Common mistakes:** Not sorting, too many categories, unclear which group is which.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/dot-plot.md`

---

## Slopegraph
**Use when:** Showing change between two (or a few) discrete time points; the slope IS the story.

**Key rules:**
- Two columns only: left (before) and right (after)
- Sort by final value or by slope magnitude
- Label both endpoints directly; no legend needed
- Best for 5-15 series; beyond that, too cluttered

**Common mistakes:** Using for more than 2-3 time points (use a line chart instead), crowded labels.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/slopegraph.md`

---

## Pie Chart
**Use when:** Showing part-of-whole with 2-3 segments where proportions are stark and well-known.

**Key rules:**
- Never use with more than 3 slices
- Never use when exact values matter — readers can't judge angles accurately
- Consider bar charts, 100% stacked bars, or slopegraphs as almost always better alternatives

**Common mistakes:** Too many slices, exploded 3D pie, multiple pies for comparison (use slopegraph).

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/pie-chart.md`

---

## Bubble Chart
**Use when:** Showing a third variable through size in a scatter context; three simultaneous dimensions.

**Key rules:**
- Label key bubbles directly
- Size encodes area, not radius — make sure tool uses area scaling
- Don't use when two dimensions (a scatter) would suffice

**Common mistakes:** Too many unlabeled bubbles, radius instead of area scaling, using when scatter is cleaner.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/bubble-chart.md`

---

## Waterfall Chart
**Use when:** Showing sequential additions and subtractions leading to a final total; bridges from start to end.

**Key rules:**
- First bar = starting value; last bar = ending value; middle bars = incremental changes
- Color-code increases (positive) vs. decreases (negative) consistently
- Label each bar with the change amount

**Common mistakes:** Too many small incremental bars, unclear direction (which are adds vs. subtracts).

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/waterfall-chart.md`

---

## Treemap
**Use when:** Showing hierarchical part-of-whole where nested structure matters; space-efficient.

**Key rules:**
- Only use when the hierarchy (parent-child) is meaningful
- Label only the largest cells; small cells should be unlabeled
- A bar chart almost always communicates magnitude comparisons more clearly

**Common mistakes:** Using when a bar chart would be simpler, too many small cells, colorful without meaning.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/treemap.md`

---

## Sankey Diagram
**Use when:** Showing how volume flows through a system across stages; the transformation is the story.

**Key rules:**
- Flow width encodes quantity — make sure all quantities sum correctly
- Label the major flows directly
- Don't use for more than 3-4 stages; it becomes unreadable

**Common mistakes:** Too many stages, unlabeled flows, using when a simpler bar chart would show the same.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/sankey-diagram.md`

---

## Boxplot
**Use when:** Comparing distributions across multiple groups; showing median, spread, and outliers simultaneously.

**Key rules:**
- Label what each box element represents (median, IQR, whiskers, outliers) — most audiences don't know
- Consider violin plots for showing the full distribution shape
- Only use when the distribution shape (not just the mean) matters

**Common mistakes:** Using with audiences unfamiliar with box plots, not explaining the elements.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/boxplot.md`

---

## Unit / Square Area Chart
**Use when:** Showing part-of-whole with humanizing effect; each unit represents a real person or thing.

**Key rules:**
- Best for proportions that have human meaning (1 in 5 people...)
- Keep total units manageable (≤100 for a waffle chart)
- Arrange in a regular grid, not random scatter

**Common mistakes:** Too many units, random arrangement, using when a simple percentage would suffice.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/unit-chart.md`

---

## Bullet Graph
**Use when:** Showing performance against a target, replacing speedometer/gauge charts.

**Key rules:**
- Always include: actual value (bar), target (reference line), and qualitative ranges (background)
- Much more space-efficient than gauge charts
- Great for dashboards

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/bullet-graph.md`

---

## Table
**Use when:** The audience needs to look up individual values; exact numbers matter more than patterns.

**Key rules:**
- Tables are for reading, not for spotting trends — if the reader should see a trend, use a chart
- Heatmap tables (with color encoding) can bridge between tables and charts
- Minimize borders and gridlines; use whitespace to separate rows

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/table.md`

---

## Spider / Radar Chart
**Use when:** Almost never. Radar charts are difficult to read accurately.

**Why to avoid:** Readers can't compare areas accurately; the shape is dominated by the polygon geometry, not data values. A dot plot or small multiples almost always communicates the same data more clearly.

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/spider-chart.md`

---

## Gantt Chart
**Use when:** Showing project timelines, scheduling, or duration across categories.

**Key rules:**
- Best for showing when things happen and how long they last
- Sort by start date or by category
- Add milestones as vertical reference lines

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/gantt-chart.md`

---

## Flowchart
**Use when:** Showing a process, decision tree, or workflow — not for quantitative data.

**Key rules:**
- Keep it simple; complex flowcharts are better as prose or tables
- Only use for processes that have genuine branching or decisions

**Full guide:** `https://gist.githubusercontent.com/shakestzd/ecf5012aec9466110ca39371b9a527c7/raw/flowchart.md`
