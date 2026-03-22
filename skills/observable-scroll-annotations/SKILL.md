---
name: observable-scroll-annotations
description: SVG-native scroll annotation pattern for Observable Framework scroll charts. Use when adding step-by-step explanatory text to animated D3 charts, reviewing charts for annotation responsiveness, or converting CSS overlay callouts to responsive SVG-native annotations. Trigger when the user asks "add callouts to chart", "make annotations responsive", "annotations overlap on mobile", "callout text over data", or needs to wire explanatory text to scroll steps.
argument-hint: "[chart file path, chart name, or 'audit' to review all charts]"
---

# Observable Scroll Annotations — SVG-Native Pattern

## The Problem

Observable Framework scroll charts use `mountScrollChart()` to drive step-by-step animations. Each step needs accompanying explanatory text. The naive approach — a CSS `position: { top, left, maxWidth }` overlay object — fails at responsive widths:

- CSS `%` positions are relative to the container, but the SVG scales uniformly inside it
- CSS `ch` maxWidth is relative to font size (fixed pixels), not chart proportions
- On mobile the callout shifts off the chart; on wide screens it overlaps data
- There is no reliable way to make CSS positions track D3 scale positions

**The correct approach:** Place annotations *inside* the SVG using D3 scale functions. Positions are computed from the same `x()`, `y()`, `rowY()` functions as the data — so they scale identically to everything else.

---

## When to Use Which Pattern

### Pattern A — STEP_ANNOTS (static bottom-margin text)

Use when the chart has a clear strip below the data (above the legend/source line) and the annotation does not need to track specific data elements.

Already implemented in: `off-balance.js` (`stepAnnot`), `capex-history.js`.

```javascript
// Static text element anchored below data, above legend
const stepAnnot = svg.append("text")
  .attr("x", ml).attr("y", H - mb + 32)
  .attr("fill", INK).attr("font-size", "11")
  .attr("font-style", "italic").attr("opacity", 0);

// In update(step):
if (step >= 0 && step < STEP_ANNOTS.length) {
  stepAnnot.text(STEP_ANNOTS[step]).transition().duration(350).attr("opacity", 0.85);
} else {
  stepAnnot.interrupt().attr("opacity", 0);
}
```

### Pattern B — SVG-native dynamic annotation (preferred for data-tracking text)

Use when the annotation must point at or sit beside a specific data element (a bar, a dot, a line), or when the chart lacks a clear bottom margin strip.

The complete pattern — documented below — is what `scenarios.js` uses.

---

## Full Implementation Template

### 1. Compute anchor from D3 scale

```javascript
// After drawing all data elements, before the step-control function:

// Find the x position of the data element you want to annotate
// e.g., the rightmost bar group, the capex dot, the leftmost line endpoint
const anchorDataX = someScale(someValue);  // responsive — same scale as data

// Annotation starts 16-22 SVG units to the right of the anchor
const annotX = anchorDataX + 20;

// Available width to the right margin
const annotW = W - mr - annotX - 6;

// Font size in SVG units (scales with the viewBox → scales with viewport)
const annotFS  = 11;
const annotLH  = 15.5;  // line height in SVG units
```

> **Key insight:** `W` is the SVG viewBox width (e.g., `Math.min(640, clientWidth - 40)`).
> SVG coordinates scale proportionally to the rendered size. `annotFS = 11` SVG units
> renders differently at 320px vs 640px rendered width, but so does the data — they
> move together.

### 2. Per-step Y position

```javascript
// Map each step to a Y anchor using the same layout function as the data
// e.g., rowY(i) for a horizontal dumbbell, y(value) for a vertical bar
function annotY(step) {
  return [
    rowY(0) + 6,   // step 0: top row
    rowY(1) + 6,   // step 1: middle row
    rowY(2) + 6,   // step 2: bottom row
  ][step] ?? rowY(0) + 6;
}
```

### 3. Step annotation texts

```javascript
const ANNOT_TEXTS = [
  "First step explanation.",
  "Second step explanation.",
  "Third step explanation — can reference stats: " + someValue.toFixed(0) + "B.",
];
```

### 4. SVG elements

```javascript
// Vertical rule (visual connector between annotation and data)
const annotRule = svg.append("line")
  .attr("stroke", ACCENT).attr("stroke-width", 1)
  .attr("opacity", 0).style("pointer-events", "none");

// Text container (tspans added dynamically for word-wrap)
const annotText = svg.append("text")
  .attr("font-family", "'DM Sans', sans-serif")
  .attr("font-size", String(annotFS))
  .attr("fill", INK)
  .attr("opacity", 0).style("pointer-events", "none");
```

### 5. showAnnot() — the word-wrap function

```javascript
function showAnnot(step) {
  // Suppress on mobile — chart rows are too compressed for inline text
  if (W < 440 || step < 0 || step >= ANNOT_TEXTS.length) {
    annotText.interrupt().attr("opacity", 0);
    annotRule.interrupt().attr("opacity", 0);
    return;
  }

  const text = ANNOT_TEXTS[step];
  const y0   = annotY(step);

  // Clear previous tspans
  annotText.selectAll("*").remove();

  // Word-wrap using getComputedTextLength()
  // getComputedTextLength() measures the actual rendered width of the tspan
  // at the current viewport size — this is what makes it truly responsive
  const words = text.split(/\s+/);
  let line = [], lineNum = 0;
  let tspan = annotText.append("tspan")
    .attr("x", annotX).attr("y", y0);

  for (const word of words) {
    line.push(word);
    tspan.text(line.join(" "));
    if (tspan.node().getComputedTextLength() > annotW && line.length > 1) {
      line.pop();
      tspan.text(line.join(" "));
      line = [word];
      lineNum++;
      tspan = annotText.append("tspan")
        .attr("x", annotX).attr("dy", String(annotLH))
        .text(word);
    }
  }

  // Size the vertical rule to match the text block height
  const totalH = lineNum * annotLH + annotFS;
  annotRule
    .attr("x1", annotX - 8).attr("x2", annotX - 8)
    .attr("y1", y0 - annotFS + 2).attr("y2", y0 + totalH - annotFS + 6);

  // Fade in with slight delay (let data animation start first)
  annotText.interrupt().attr("opacity", 0)
    .transition().delay(250).duration(320).attr("opacity", 1);
  annotRule.interrupt().attr("opacity", 0)
    .transition().delay(250).duration(320).attr("opacity", 0.9);
}
```

### 6. Wire into update(step)

```javascript
function update(step) {
  // ... all your existing data transitions ...

  // Always call showAnnot at the end
  showAnnot(step);
}
```

### 7. Update the article markdown

When a chart handles its own annotations, suppress the CSS overlay in `mountScrollChart`:

```javascript
// dd001.md (or any article .md file)
display(mountScrollChart(myChart.node, myChart.update, [
  {}, {}, {}, {}, {}   // empty objects — no CSS callout config needed
], { callout: "none" }));
```

The `callout: "none"` option tells `animate.js` to skip creating the overlay div entirely.

---

## Audit Checklist — Converting Existing Charts

For each scroll chart in `observable/src/`:

1. **Identify current annotation approach:**
   - Has `position: { top, left, maxWidth }` objects → needs conversion to SVG-native
   - Has `STEP_ANNOTS` + static `stepAnnot` text → already Pattern A, acceptable
   - Has `showAnnot()` function → already Pattern B, done

2. **Find the clear zone** in the chart where annotation can sit without overlapping data:
   - To the right of the leftmost/narrowest data element
   - Below the last data row if there's margin space
   - At a consistent Y level tracked by the step

3. **Compute `annotX` from D3 scales**, not from hardcoded pixel offsets.

4. **Test at 320px, 480px, and 640px** rendered widths. At 320px (`W < 440`) the annotation should be hidden; the article prose below the chart provides context.

5. **Update the article .md** to use `callout: "none"` for that chart's `mountScrollChart` call.

---

## Charts by Status (as of March 2026)

| Chart | File | Annotation status |
|:------|:-----|:-----------------|
| Valuation scroll | `valuation.js` | CSS callout — needs audit |
| Capex history | `capex-history.js` | Pattern A (STEP_ANNOTS) ✅ |
| Stacked capex | `stacked-capex.js` | CSS callout — needs audit |
| Off-balance | `off-balance.js` | Pattern A (STEP_ANNOTS) ✅ |
| Revenue ratio | `revenue-ratio.js` | CSS callout — needs audit |
| Revenue gap | `revenue-gap.js` | CSS callout — needs audit |
| Guidance | `guidance.js` | CSS callout — needs audit |
| Scenarios | `scenarios.js` | Pattern B (SVG-native) ✅ |
| Employment index | `employment-index.js` | CSS callout — needs audit |
| Wage slopes | `wage-slopes.js` | CSS callout — needs audit |
| DC map | `dc-map.js` | CSS callout — needs audit |
| Labor feedback | `labor-feedback.js` | CSS callout — needs audit |

---

## Key Files

- `observable/src/js/animate.js` — `mountScrollChart()`, callout modes, `pickCalloutPosition()`
- `observable/src/js/charts/scenarios.js` — reference implementation of Pattern B
- `observable/src/js/design.js` — `INK`, `ACCENT`, `INK_LIGHT` color tokens

---

## Common Mistakes

**`annotX` too close to data:** Leave at least 16 SVG units of gap. The vertical rule needs room.

**`annotW` computed before `W` is set:** Always compute `annotW` after the `const W = ...` line.

**Forgetting `annotText.selectAll("*").remove()`:** Without this, each step appends new tspans on top of old ones — text stacks up.

**Not setting `pointer-events: none`:** The annotation overlaps the chart area. Without this, it blocks mouse events on the bars/dots/lines beneath it.

**Using `annotFS` in CSS px units:** `font-size` on an SVG `<text>` element is in SVG user units, which scale with the viewBox. Do not use `"11px"` — use `"11"`.
