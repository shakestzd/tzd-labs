---
name: flowmpl-flow-diagram
description: Use this skill when creating flow diagrams, causal chains, decision trees, process flows, or entity relationship diagrams using flowmpl's flow_diagram() function. Provides detailed API reference for nodes, edges, routing heuristics, and face overrides. Triggers on "flow diagram", "causal chain", "process flow", "decision tree", "entity diagram", "flow_diagram()", "node and edge".
---

# flowmpl flow_diagram() — Quick Reference

`flow_diagram()` renders labeled rounded-box nodes connected by auto-routed arrows.
Use it for causal chains, decision trees, process flows, and SPV/entity diagrams.

---

## Import

```python
from src.plotting import COLORS, CONTEXT, FONTS, FIGSIZE, flow_diagram
# or, if using flowmpl directly:
from flowmpl import COLORS, CONTEXT, FONTS, FIGSIZE, flow_diagram
```

In Systems notebooks use `src.plotting`. The shim re-exports everything from `flowmpl`.

---

## Signature

```python
fig = flow_diagram(
    nodes: dict[str, tuple[str, float, float, str, str]],
    edges: list[dict],
    *,
    figsize: tuple[float, float] = (18, 6),
    xlim: tuple[float, float] | None = None,
    ylim: tuple[float, float] | None = None,
    font_size: int | None = None,         # node label size; default 10
    edge_font_size: int | None = None,    # edge label size; default 9
    pad: float = 0.2,                     # space around text inside box
    box_pad: float = 0.1,                 # FancyBboxPatch rounding
    corner_radius: float = 0.4,           # elbow corner rounding (data units)
    legend_handles: list | None = None,
    legend_ncol: int | None = None,
    max_autoscale: float | None = 1.5,    # max vertical stretch factor
) -> plt.Figure
```

---

## Node Format

```python
nodes = {
    "key": (label, cx, cy, fill_color, text_color),
}
```

| Field | Type | Notes |
|-------|------|-------|
| `key` | str | Any identifier — used in edge `src`/`dst` |
| `label` | str | Box text; use `\n` for multi-line |
| `cx`, `cy` | float | Centre in abstract data units (renderer scales to fit) |
| `fill_color` | str | Hex color or COLORS token |
| `text_color` | str | Hex color — use `"#ffffff"` on dark fills |

**Color conventions:**
- Accent/focal node → `COLORS["accent"]` fill, `"#ffffff"` text
- Positive/confirmed → `COLORS["positive"]` fill, `"#ffffff"` text
- Neutral/speculative → `COLORS["neutral"]` fill, `COLORS["text_dark"]` text
- Context/background → `CONTEXT` fill, `COLORS["text_dark"]` text
- Negative/risk → `COLORS["negative"]` fill, `"#ffffff"` text

---

## Edge Format

```python
edges = [
    {"src": "a", "dst": "b"},                              # basic arrow
    {"src": "a", "dst": "b", "label": "12–18 mo"},         # with label
    {"src": "a", "dst": "b", "dashed": True},              # dashed line
    {"src": "a", "dst": "b", "color": COLORS["negative"]}, # custom color
    {"src": "a", "dst": "b", "curve": 0.3},                # arc (+ = left bow)
    {"src": "a", "dst": "b", "exit": "top",   "entry": "left"},  # face override
    {"src": "a", "dst": "b", "exit": "bottom", "entry": "left"}, # face override
]
```

| Key | Type | Default | Notes |
|-----|------|---------|-------|
| `src`, `dst` | str | required | Node keys |
| `label` | str | — | Edge label at midpoint |
| `dashed` | bool | `False` | Dashed linestyle |
| `curve` | float | `0` | `arc3` bow radius; positive = left of direction |
| `color` | str | `COLORS["muted"]` | Arrow and label color |
| `exit` | `"top"/"bottom"/"left"/"right"` | auto | Force which face the arrow exits |
| `entry` | `"top"/"bottom"/"left"/"right"` | auto | Force which face the arrow arrives at |

---

## Routing Heuristic

The auto-router uses the vector from src center → dst center (`vx`, `vy`):

| Condition | Route | Faces used |
|-----------|-------|------------|
| `\|vy\| < 0.25 * \|vx\|` | Near-horizontal → straight | Exit/enter left or right |
| `\|vx\| < 0.25 * \|vy\|` | Near-vertical → straight | Exit/enter top or bottom |
| `\|vy\| < 0.75 * \|vx\|` | Primarily-horizontal → elbow | Exit top/bottom, enter left/right |
| else | Primarily-vertical → elbow | Exit left/right, enter top/bottom |

**When the heuristic fails:** when the angle is near-diagonal (≈45°), or when multiple
edges exit from the same face and overlap. Use explicit `exit`/`entry` to fix.

---

## Face Override Rule

Use `exit`/`entry` whenever:

1. **Multiple edges share a source face** — they will overlap without overrides.
   The fix: send each edge out a different face.
2. **Near-diagonal vectors** misclassify as the wrong heuristic branch.
3. **T-layout**: one straight edge (no override) + two diagonal edges (need overrides).

**Example — T-layout (one root → three destinations):**
```python
nodes = {
    "r": ("Root",   1.0, 1.5, COLORS["accent"],   "#ffffff"),
    "a": ("Top",    4.5, 3.0, COLORS["positive"], "#ffffff"),
    "m": ("Middle", 4.5, 1.5, COLORS["neutral"],  COLORS["text_dark"]),
    "b": ("Bottom", 4.5, 0.0, CONTEXT,            COLORS["text_dark"]),
}
edges = [
    {"src": "r", "dst": "a", "exit": "top",    "entry": "left"},  # exits r's TOP
    {"src": "r", "dst": "m"},                                       # straight, no override
    {"src": "r", "dst": "b", "exit": "bottom", "entry": "left"},  # exits r's BOTTOM
]
```

Without overrides: all three arrows exit r's right face and overlap.
With overrides: each arrow exits a different face — no overlap.

---

## Design Token Quick Reference

```python
# Colors — semantic roles
COLORS["accent"]      # primary story color (dark teal)
COLORS["positive"]    # genuinely good/confirmed
COLORS["negative"]    # genuinely bad/risk
COLORS["neutral"]     # speculative, neither confirmed nor denied
COLORS["muted"]       # secondary, supporting
COLORS["reference"]   # reference lines and guides
COLORS["background"]  # figure background
COLORS["text_dark"]   # dark text (on light fills)
COLORS["text_light"]  # light text (on dark fills)

# SWD gray — non-focus elements
CONTEXT               # "#c0c0c0" — use for context/background nodes

# Fonts
FONTS["title"]        # 16
FONTS["subtitle"]     # 14
FONTS["axis_label"]   # 12
FONTS["annotation"]   # 11  ← flow node labels use this - 2 (= 9 default)
FONTS["legend"]       # 10
FONTS["tick_label"]   # 10
FONTS["caption"]      # 9
FONTS["small"]        # 8
FONTS["value_label"]  # 9

# Figure sizes
FIGSIZE["standard"]   # (10, 5)
FIGSIZE["wide"]       # (14, 5)
FIGSIZE["tall"]       # (8, 10)
FIGSIZE["map"]        # (12, 7)
```

---

## Display in Marimo

```python
@app.cell
def _(COLORS, CONTEXT, flow_diagram, mo, save_fig):
    fig = flow_diagram(
        nodes={...},
        edges=[...],
        figsize=(18, 6),
    )
    save_fig(fig, "dd001_my_diagram.png")
    return (fig,)

@app.cell
def _(mo):
    mo.image("notebooks/images/dd001_my_diagram.png")
```

---

## Common Patterns

### Linear chain (pipeline steps)

```python
fig = flow_diagram(
    nodes={
        "announce": ("Announce",  1.0, 0.0, CONTEXT,            COLORS["text_dark"]),
        "permit":   ("Permit",    3.5, 0.0, COLORS["neutral"],  COLORS["text_dark"]),
        "procure":  ("Procure",   6.0, 0.0, COLORS["neutral"],  COLORS["text_dark"]),
        "build":    ("Build",     8.5, 0.0, COLORS["positive"], "#ffffff"),
        "operate":  ("Operate",  11.0, 0.0, COLORS["accent"],   "#ffffff"),
    },
    edges=[
        {"src": "announce", "dst": "permit",  "label": "6–12 mo"},
        {"src": "permit",   "dst": "procure", "label": "12–18 mo"},
        {"src": "procure",  "dst": "build",   "label": "18–36 mo"},
        {"src": "build",    "dst": "operate", "label": "24–36 mo"},
    ],
    figsize=(18, 4),
)
```

### Decision fork (single source → multiple outcomes)

```python
fig = flow_diagram(
    nodes={
        "q":    ("Demand\nMaterializes?", 1.0, 1.0, COLORS["accent"],   "#ffffff"),
        "yes":  ("Revenue\nJustified",    4.5, 2.5, COLORS["positive"], "#ffffff"),
        "part": ("Partial\nReturn",       4.5, 1.0, COLORS["neutral"],  COLORS["text_dark"]),
        "no":   ("Stranded\nAsset",       4.5, -0.5, COLORS["negative"], "#ffffff"),
    },
    edges=[
        {"src": "q", "dst": "yes",  "label": "high elasticity", "exit": "top",    "entry": "left"},
        {"src": "q", "dst": "part", "label": "moderate"},
        {"src": "q", "dst": "no",   "label": "low elasticity",  "exit": "bottom", "entry": "left"},
    ],
)
```

### Entity chain with dashed liability link

```python
fig = flow_diagram(
    nodes={
        "tech":    ("Tech Giant\n(tenant)",      1.0, 1.0, CONTEXT,            COLORS["text_dark"]),
        "spv":     ("SPV\n(landlord)",           4.0, 1.0, COLORS["neutral"],  COLORS["text_dark"]),
        "credit":  ("Private Credit\n(lender)",  7.0, 1.0, COLORS["negative"], "#ffffff"),
        "pension": ("Pension Fund\n(LP)",        7.0, -0.5, COLORS["negative"], "#ffffff"),
    },
    edges=[
        {"src": "tech",   "dst": "spv",    "label": "3–5 yr lease"},
        {"src": "spv",    "dst": "credit",  "label": "10 yr loan @ 10%+"},
        {"src": "credit", "dst": "pension", "label": "LP exposure", "dashed": True,
         "exit": "bottom", "entry": "top"},
    ],
)
```

---

## Sizing Tips

- `figsize=(18, 6)` works for 4–6 horizontally arranged nodes
- `figsize=(14, 8)` for taller layouts with 3 vertical tiers
- `figsize=(10, 10)` for dense 2D grids
- For tight layouts reduce `pad=0.15` and `box_pad=0.08`
- `max_autoscale=1.5` prevents explosive vertical spread (default); set `None` to disable

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Arrows overlap at source | Add `exit` overrides: `"top"`, `"bottom"`, etc. |
| Arrows overlap at destination | Add `entry` overrides |
| Elbow goes the wrong way | Flip `exit` / `entry` values |
| Labels clip at edges | Increase `figsize` or reduce `pad` |
| Vertical layout too spread out | Lower `max_autoscale` (e.g. `1.2`) |
| Vertical layout too cramped | Increase `max_autoscale` or adjust `cy` values |
| Straight line when elbow expected | Use `curve=0.3` for an arc, or set explicit faces |
