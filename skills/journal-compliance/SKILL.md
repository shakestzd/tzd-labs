---
name: journal-compliance
description: Use this skill when verifying a manuscript meets journal-specific submission requirements before upload, checking a revision addresses reviewer concerns, or validating formatting after structural changes. Triggers on "check compliance", "journal requirements", "submission checklist", "PRS requirements", "JPRAS requirements", "ready to submit".
---

# Journal Compliance Check

Verify a manuscript meets journal-specific submission requirements before upload.

## When to Use

Use this skill when:
- Final review before submitting to a journal portal
- Checking a revision addresses all editor/reviewer concerns
- Validating formatting after structural changes

## Compliance Checklist

### Structure
- [ ] Title page: title, authors with degrees, affiliations, corresponding author, COI statement, running head, word counts, keywords
- [ ] Abstract: structured (Background/Methods/Results/Conclusions), within word limit
- [ ] Introduction: 2-3 paragraphs, no subheadings, ends with study objectives
- [ ] Methods: appropriate subheadings (Study Design, Outcome Measures, Statistical Analysis)
- [ ] Results: primary outcome first, secondary outcomes, efficiency data
- [ ] Discussion: flowing prose without subheadings (except CONCLUSIONS)
- [ ] References: journal citation style applied
- [ ] Figure legends: after references, one per figure
- [ ] SDC legends: after figure legends, one per SDC item

### Word Counts
- [ ] Body text (Introduction through Conclusions) within journal limit
- [ ] Abstract within journal limit
- [ ] Counts on title page match actual counts

### Tables
- [ ] Numbered in order of first reference in text
- [ ] Each table as separate .docx file
- [ ] Three-line border format (top thick, header underline, bottom thick)
- [ ] No internal gridlines or shading
- [ ] Title/caption on each table

### Figures
- [ ] Numbered in order of first reference in text
- [ ] Resolution >= 300 DPI
- [ ] TIFF format (or journal-accepted format)
- [ ] Named as "Figure N.tiff"

### Cross-References
- [ ] Every table/figure referenced at least once in text
- [ ] References match actual numbering (no stale numbers)
- [ ] No unresolved Quarto references (?@tbl-, ?@fig-)

### Terminology
- [ ] Consistent terminology throughout
- [ ] No AI writing tells (em-dashes, "Furthermore", "Moreover", "delve", etc.)

### Supplemental Digital Content
- [ ] Within journal SDC limits (items, word count)
- [ ] Each SDC item has a legend
- [ ] SDC formatted as tables where possible

### Reviewer Response (for revisions)
- [ ] Every reviewer concern addressed with specific manuscript location
- [ ] Response letter maps each concern to the fix
- [ ] No stale references to removed content

## Journal-Specific Requirements

### PRS (Plastic and Reconstructive Surgery)
| Requirement | Specification |
|-------------|---------------|
| Body word limit | 3,000 (+ 500 extension) |
| Abstract | 250 words, structured |
| Max figures + tables | 20 pieces |
| Figure format | 300 DPI, TIFF |
| SDC text limit | 500 words |
| SDC items limit | 10 |
| Reference style | AMA |
| Tables | Separate .docx files |

### JPRAS (Journal of Plastic, Reconstructive & Aesthetic Surgery)
| Requirement | Specification |
|-------------|---------------|
| Body word limit | No strict limit (varies by article type) |
| Abstract | 250 words, unstructured |
| Figure format | 300 DPI, TIFF/EPS/PDF |
| Reference style | Vancouver (numbered) |
| Tables | Embedded in single manuscript file |

### Annals of Plastic Surgery
| Requirement | Specification |
|-------------|---------------|
| Body word limit | 3,000 |
| Abstract | 200 words, unstructured |
| Figure format | 300 DPI, TIFF |
| Reference style | AMA |
| Tables | Embedded in manuscript |
