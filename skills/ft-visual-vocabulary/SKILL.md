---
name: ft-visual-vocabulary
description: FT Visual Vocabulary chart selection guide. Use when choosing chart types, evaluating whether a chart type matches the data relationship, proposing visualization alternatives, or when the user asks "what chart should I use", "is this the right chart", "what's a better way to show this", or describes a data relationship and needs a visualization recommendation.
argument-hint: "[data relationship or current chart type]"
---

Use the FT Visual Vocabulary framework to select the right chart type.

**Step 1: Identify the data relationship category**

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

**Step 2: Choose a chart type from the matching category**

See [ft-visual-vocabulary.md](ft-visual-vocabulary.md) for the full reference with chart options per category, when to prefer each, D3/Observable links, and project-specific examples.

**Step 3: Flag common mismatches**

- 2x2 quadrant used for correlation → scatter plot with actual coordinates is clearer
- Pie chart with 4+ slices → horizontal bar, sorted by value
- Dual y-axes → two separate small multiples
- Stacked bar with 5+ categories → focus top 2-3, group rest as "other"
- Spaghetti line (8+ series) → slope chart or small multiples
- Bar chart used for geographic data → choropleth or bubble map
- Table used for comparison → bar chart

When responding: state the identified category, recommend the chart type, and briefly explain why it serves the story better than alternatives.
