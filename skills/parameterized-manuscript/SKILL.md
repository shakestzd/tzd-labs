---
name: parameterized-manuscript
description: Use this skill when setting up or reviewing a manuscript project to ensure all numbers from data, figures, and tables are parameterized — never hardcoded in prose. Covers the Stats dataclass pattern, template placeholders, sync pipeline, and semantic validation. Triggers on "parameterize numbers", "stats dataclass", "hardcoded numbers", "sync sections", "data-driven manuscript", "validate prose", "manuscript numbers".
---

# Parameterized Manuscript Pattern

Every number in manuscript prose must trace to a computed value in a Stats dataclass. No hardcoded numbers in .qmd files. This prevents stale values, inconsistency between text and tables/figures, and makes data updates propagate automatically.

## Architecture

```
Source data (CSV, JSON, analysis outputs)
  ↓
stats.py          ← Stats dataclass: single source of truth
  ↓
sync_sections.py  ← Replaces <<VAR>> placeholders with computed values
  ↓
_sections/*.qmd   ← Rendered prose (literal values from stats)
  ↓
validate_prose.py ← Checks arithmetic + semantic consistency
  ↓
quarto render     ← Final manuscript output
```

## Step 1: Create stats.py

Define a `Stats` frozen dataclass with a `from_data()` classmethod that computes all values from source data.

```python
"""Single source of truth for all manuscript numbers."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"


@dataclass(frozen=True)
class Stats:
    # ── Demographics ──
    n_total: int
    n_female: int
    n_male: int
    pct_female: str          # pre-formatted: "52.3"
    mean_age: str            # pre-formatted: "45.2"
    age_range: str           # pre-formatted: "18–72"

    # ── Primary outcome ──
    outcome_rate: str
    or_primary: str          # odds ratio
    or_primary_ci: str       # "1.05–5.70"
    or_primary_p: str        # "0.038"

    # ── Figure/table numbering (reorderable) ──
    fig_flowchart: int = 0
    fig_primary: int = 0
    tbl_demographics: int = 0
    tbl_outcomes: int = 0

    # ── Word variants (for sentence starts) ──
    n_total_word: str = ""
    n_total_word_cap: str = ""

    @classmethod
    def from_data(cls) -> Stats:
        df = pd.read_csv(DATA_DIR / "study_data.csv")

        n_total = len(df)
        n_female = (df["sex"] == "F").sum()

        # ── Figure/table numbering ──
        # Change order here → all prose references update automatically
        _fig_order = ["fig_flowchart", "fig_primary"]
        _tbl_order = ["tbl_demographics", "tbl_outcomes"]
        fig_nums = {name: i for i, name in enumerate(_fig_order, 1)}
        tbl_nums = {name: i for i, name in enumerate(_tbl_order, 1)}

        return cls(
            n_total=n_total,
            n_female=n_female,
            n_male=n_total - n_female,
            pct_female=f"{n_female / n_total * 100:.1f}",
            mean_age=f"{df['age'].mean():.1f}",
            age_range=f"{df['age'].min()}–{df['age'].max()}",
            outcome_rate=f"{df['outcome'].mean() * 100:.1f}",
            # Regression results from analysis script
            or_primary="2.45",
            or_primary_ci="1.05–5.70",
            or_primary_p="0.038",
            # Numbering
            **fig_nums,
            **tbl_nums,
            # Word variants
            n_total_word=_num_to_word(n_total),
            n_total_word_cap=_num_to_word(n_total).capitalize(),
        )


def _num_to_word(n: int) -> str:
    """Convert small integers to words for sentence starts."""
    words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty",
    }
    return words.get(n, str(n))


# Module-level singleton — computed once on import
S = Stats.from_data()
```

### Key principles

- **Pre-format values** in the dataclass (`pct_female="52.3"` not `0.523`). Templates should not contain formatting logic.
- **Figure/table numbering via ordered lists**. Change the order in `_fig_order` → all `Figure N` references renumber.
- **Word variants** for sentence-start rules (`n_total_word_cap="One hundred eighty-three"` → "One hundred eighty-three patients...").
- **Frozen dataclass** prevents accidental mutation.
- **Hardcoded regression results are annotated** with comments like `# from analysis script output`.

## Step 2: Create template files

Create `_section_templates/*.qmd.tmpl` with `<<VAR>>` placeholders:

```markdown
<!-- _section_templates/_abstract.qmd.tmpl -->
**Background:** ...

**Methods:** A retrospective review of <<n_total>> patients treated
between <<study_start_year>> and <<study_end_year>> was performed.

**Results:** The overall rate was <<outcome_rate>>% (<<n_outcome>>/<<n_total>>).
On multivariable analysis, the primary predictor was significant
(OR = <<or_primary>>, 95% CI [<<or_primary_ci>>], p = <<or_primary_p>>).

**Conclusions:** ...
```

### Placeholder rules

- `<<var_name>>` matches a Stats dataclass attribute exactly
- No formatting in templates — values are pre-formatted in stats.py
- Figure/table references: `Figure <<fig_flowchart>>`, `Table <<tbl_demographics>>`
- Sentence-start numbers: `<<n_total_word_cap>> patients were included`

## Step 3: Create sync_sections.py

```python
"""Replace <<VAR>> placeholders in templates with computed stats."""
from pathlib import Path
import re
from stats import S

TEMPLATE_DIR = Path("_section_templates")
OUTPUT_DIR = Path("_sections")


def sync() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    unresolved = []

    for tmpl in sorted(TEMPLATE_DIR.glob("*.qmd.tmpl")):
        text = tmpl.read_text()
        out_name = tmpl.stem  # removes .tmpl, keeps .qmd

        def replacer(m: re.Match) -> str:
            var = m.group(1)
            if hasattr(S, var):
                return str(getattr(S, var))
            unresolved.append((tmpl.name, var))
            return m.group(0)  # leave unresolved

        rendered = re.sub(r"<<(\w+)>>", replacer, text)
        (OUTPUT_DIR / out_name).write_text(rendered)
        print(f"  {tmpl.name} → {out_name}")

    if unresolved:
        print("\nWARNING: Unresolved placeholders:")
        for fname, var in unresolved:
            print(f"  {fname}: <<{var}>> not found in Stats")
        raise SystemExit(1)

    print(f"\nSynced {len(list(TEMPLATE_DIR.glob('*.qmd.tmpl')))} templates.")


if __name__ == "__main__":
    sync()
```

## Step 4: Create validate_prose.py

```python
"""Validate rendered prose against computed stats."""
from pathlib import Path
import re
from stats import S

SECTIONS_DIR = Path("_sections")


def validate() -> list[str]:
    errors = []

    # ── 1. Check for unresolved placeholders ──
    for qmd in SECTIONS_DIR.glob("*.qmd"):
        text = qmd.read_text()
        remaining = re.findall(r"<<\w+>>", text)
        if remaining:
            errors.append(f"{qmd.name}: unresolved placeholders: {remaining}")

    # ── 2. Arithmetic consistency ──
    if S.n_female + S.n_male != S.n_total:
        errors.append(
            f"n_female ({S.n_female}) + n_male ({S.n_male}) "
            f"!= n_total ({S.n_total})"
        )

    # ── 3. Prose quality: sentence-start numbers ──
    for qmd in SECTIONS_DIR.glob("*.qmd"):
        for i, line in enumerate(qmd.read_text().splitlines(), 1):
            # Check for bare digits at sentence start
            if re.match(r"^[0-9]", line.strip()):
                errors.append(
                    f"{qmd.name}:{i}: Sentence starts with digit — "
                    f"spell out or restructure"
                )

    # ── 4. Plural consistency ──
    for qmd in SECTIONS_DIR.glob("*.qmd"):
        text = qmd.read_text()
        # "1 patients" or "1 themes" (singular count + plural noun)
        if re.search(r"\b1 (patients|themes|models|transcripts|items)\b", text):
            errors.append(f"{qmd.name}: '1 <plural>' — use singular noun")

    # ── 5. Add domain-specific semantic checks here ──
    # Example: if prose claims A > B, verify stat_A > stat_B

    return errors


if __name__ == "__main__":
    errs = validate()
    if errs:
        print("VALIDATION ERRORS:")
        for e in errs:
            print(f"  ✗ {e}")
        raise SystemExit(1)
    else:
        print("✓ All validation checks passed.")
```

## Step 5: Wire into the build pipeline

Update `build_upload.py`:

```python
def main():
    # 0. Sync templates → rendered sections
    sync_sections()      # <<VAR>> → literal values

    # 1. Validate prose
    validate_prose()     # arithmetic + semantic checks

    # 2. Render manuscript
    build_manuscript()   # quarto render

    # 3. Build tables
    build_all_tables()

    # 4. Copy figures
    copy_figures()
```

## Checklist: Is My Manuscript Properly Parameterized?

- [ ] Every number in prose exists as a Stats attribute
- [ ] Templates use `<<var_name>>` — no literal numbers
- [ ] `sync_sections.py` runs without unresolved placeholders
- [ ] `validate_prose.py` passes all checks
- [ ] Figure/table numbering uses ordered lists in stats.py
- [ ] Sentence-start numbers have word variants (`<<n_word_cap>>`)
- [ ] Percentages are pre-formatted in stats.py
- [ ] Regression results are annotated with source comments
- [ ] No manual edits to `_sections/*.qmd` — always edit templates
