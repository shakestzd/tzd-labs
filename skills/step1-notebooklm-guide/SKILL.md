---
name: step1-notebooklm-guide
description: USMLE Step 1 domain knowledge for generating NotebookLM podcast prompts. Contains the proven prompt template, chapter-to-vignette mapping, high-yield topic patterns, and pedagogical strategies that produce 100% source coverage in NotebookLM's Audio Overview. Load this skill when generating prompts for any Survivor's Guide to USMLE Step 1 chapter.
argument-hint: "[chapter number or name to generate a prompt for]"
---

# USMLE Step 1 NotebookLM Prompt Guide

This skill contains domain-specific knowledge for generating NotebookLM Audio Overview prompts for the **Survivor's Guide to USMLE Step 1, 6th Edition**. It encodes lessons learned from generating and testing prompts for Chapters 1 and 18, where coverage was measured by transcribing the generated podcast and comparing it against the source material.

## Source Material Structure

The textbook has 23 chapters (00-22):

| # | Chapter | Key Domain |
|---|---------|-----------|
| 00 | Front Matter | — |
| 01 | General Principles | Autonomic pharmacology, PK/PD, drug reactions, CYP450 |
| 02 | Shock and Its Management | Hemodynamics, shock types, fluid resuscitation |
| 03 | Endocrinology | Hormones, thyroid, adrenal, pituitary, diabetes |
| 04 | Reproductive System and OBGYN | Reproduction, pregnancy, contraception |
| 05 | Renal System | Nephron physiology, acid-base, electrolytes, diuretics |
| 06 | Gastroenterology | GI tract, liver, pancreas, biliary |
| 07 | Respiratory System | Lung mechanics, obstructive vs restrictive, gas exchange |
| 08 | Cardiology | Heart physiology, arrhythmias, valvular disease, HF |
| 09 | Genetics and Nutrition | Inheritance patterns, vitamins, minerals |
| 10 | Rheumatology and Dermatology | Autoimmune, connective tissue, skin |
| 11 | Neurology | CNS, PNS, cranial nerves, stroke, demyelinating |
| 12 | Psychiatry | Mood, psychotic, anxiety disorders, pharmacotherapy |
| 13 | Social Sciences and Ethics | Bioethics, epidemiology concepts |
| 14 | Biostatistics | Sensitivity, specificity, study design, bias |
| 15 | Infectious Disease | Bacteria, viruses, fungi, parasites, antibiotics |
| 16 | Biochemistry | Metabolic pathways, enzyme deficiencies, storage diseases |
| 17 | Hematology, Oncology and Immunology | Blood cells, clotting, cancers, immune system |
| 18 | Pathology | Cell injury, necrosis, inflammation, calcification |
| 19 | Poisoning and Miscellaneous Management | Toxicology, antidotes |
| 20 | Clinical Vignettes and Management | Pattern-recognition vignettes by system |
| 21 | Principles of Management | Imaging, procedures, cancer management |
| 22 | Test Taking Skills | Exam strategy |

## Supplementary Sources

Chapters 20, 21, and 22 are NOT standalone podcast chapters — they are **supplementary material** to enrich all other chapters:

- **Chapter 20 (Clinical Vignettes)**: Short clinical scenarios with classic presentations → use to teach chapter concepts in Step 1 question stem language
- **Chapter 21 (Principles of Management)**: When to order what test, imaging types, management protocols → use to add management context to chapter topics
- **Chapter 22 (Test Taking Skills)**: Exam strategy → not used in prompts

### Chapter-to-Vignette Mapping

When generating a prompt for chapter N, extract vignettes from chapters 20/21 that match chapter N's topics. Key mappings:

| Chapter | Relevant Vignettes From Ch 20 |
|---------|------------------------------|
| 01 General Principles | Parkinson's, Wilson's, Pheochromocytoma, MG, Delirium, Thyroid Storm |
| 02 Shock | Cardiac tamponade, aortic dissection, MI presentations |
| 03 Endocrinology | DKA, thyroid storm, Cushing's, Addison's, PCOS, pheochromocytoma |
| 04 Reproductive | Abruptio placenta, placenta previa, ectopic, testicular torsion |
| 05 Renal | Kidney stones, RCC, UTI, incontinence types, electrolyte disorders |
| 06 GI | GERD, IBD, appendicitis, intussusception, liver disease |
| 07 Respiratory | Asthma, COPD, PE, pneumonia, lung cancer, CF |
| 08 Cardiology | MI, pericarditis, tamponade, HF, murmurs, HOCM |
| 09 Genetics | Marfan, Ehlers-Danlos, precocious puberty |
| 10 Rheumatology | RA, SLE, gout, Sjogren's, dermatomyositis, AS |
| 11 Neurology | MS, ALS, Parkinson's, Alzheimer's, headaches |
| 12 Psychiatry | Bipolar, MDD, delirium, schizophrenia |
| 15 Infectious Disease | Classic clues for infections (Ch 20 has a dedicated section) |
| 17 Hematology | Anemias, DIC, ITP/TTP, transfusion reactions, lymphomas |
| 18 Pathology | (Self-contained; vignettes embedded in source) |

## Proven Prompt Template

This opening block MUST appear at the start of every prompt:

```
USMLE Step 1 review podcast for a med student in dedicated study mode. The PRIMARY source is the {Chapter Name} chapter — cover EVERY topic in it, skip nothing, including all tables and drug lists. The clinical vignettes file is supplementary: use those vignettes to TEACH the chapter concepts in Step 1 question stem language, not as extra content. Use Socratic back-and-forth: one host quizzes, the other answers. Compare confusable pairs side-by-side. Flag commonly tested tricky concepts and classic board traps. After every 3-4 topics, do a 30-second rapid-fire recap of key takeaways.

COVER ALL CHAPTER TOPICS IN THIS ORDER:
```

## High-Yield Patterns to Encode in Every Prompt

### 1. Confusable Pairs
Step 1 loves testing distinctions. Always identify and request side-by-side comparison for pairs like:
- Hypertrophy vs Hyperplasia
- Reversible vs Irreversible injury
- Apoptosis vs Necrosis
- Red vs Pale infarcts
- Competitive vs Non-competitive inhibitors
- First-order vs Zero-order kinetics
- Type A vs Type B drug reactions
- Caseating vs Non-caseating granulomas
- Dystrophic vs Metastatic calcification
- Sensitivity vs Specificity

### 2. Classic Board Traps
Flag with "Trap:" in the prompt:
- Dysplasia is pre-neoplastic but STILL reversible
- Brain does NOT undergo coagulative necrosis (liquefactive instead)
- Eccrine sweat glands are sympathetic but cholinergic
- Chronic alcohol = CYP450 inducer, Acute alcohol = inhibitor
- Atropine reverses muscarinic effects only, NOT nicotinic (muscle weakness persists)
- Neostigmine does NOT cross BBB (quaternary amine)

### 3. Arrow Notation for Pathways
Always encode pathways as A→B→C chains:
- LPS→macrophages→IL-1/TNF-α→COX→PGE2→posterior hypothalamus→fever
- Rolling(L-selectin)→tight binding(ICAM-1)→transmigration(PECAM-1)
- Ischemia→Na/K pump failure→cell swelling(reversible)→membrane damage(irreversible)

### 4. Drug-Pathway Integration
For every pathway, name at least one drug that targets it:
- COX pathway → NSAIDs, Aspirin
- TNF-α → Infliximab, Adalimumab
- PD-1/PD-L1 → Pembrolizumab, Nivolumab
- CDK4/6 → Palbociclib

### 5. Management Pearls
Integrate from Chapter 21 where relevant:
- "Any toxicity → measure plasma drug concentration"
- "Alpha-block FIRST then beta-block for pheochromocytoma"
- "All ICU patients get PPIs"
- "Abscess → drain + antibiotics (Metronidazole below diaphragm, Clindamycin above)"

## Lessons from Testing

### What achieved 100% coverage (Chapter 18):
- Every topic explicitly named with specific details
- Prompt was ~4,800 chars for ~8 pages of source
- Every drug, enzyme, and clinical association was listed by name
- Confusable pairs were explicitly requested

### What achieved 83% coverage (Chapter 1 V1):
- Topics were named but some sub-details were omitted
- Missing items were ones NOT explicitly named: Isoproterenol, Mirabegron, Phentolamine, Bisphenol A, Radon, Echinacea, Pyruvate metabolism

### What achieved ~97% coverage (Ch1 V2/V3, Ch15A, Ch16A, Ch17A/B/C):
- Revised prompt explicitly named every detail → recovered 15/15 previously-missed items
- PDF-only source was sufficient — adding OCR markdown did not improve coverage
- Strategy scaled across 10 podcasts consistently at ~97%
- ~97% appears to be the practical ceiling — last 3% are isolated sub-details NotebookLM occasionally skips

### What caused 94% coverage (Ch16B — ETC skipped):
- The prompt was under the char limit (3,964 chars) but covered TOO MANY DENSE TOPICS (7 biochemistry sections)
- NotebookLM ran out of podcast time (~77 min) before reaching the ETC section at the end
- **Lesson: The constraint is content density per podcast, not just prompt chars**
- Fix: Split into B1 (5 sections) and B2 (6 sections) → each covers fewer topics in depth

## Chapter Splitting Strategy

Split decisions are based on **two constraints**: the 4,900 char prompt limit AND content density per podcast.

### Pages-per-Podcast Guidelines

| Content Density | Max Pages/Podcast | Examples |
|----------------|-------------------|---------|
| **High** (biochem pathways, pharmacology, microbiology organisms) | **8-10 pages** | Biochemistry, Infectious Disease, General Principles |
| **Medium** (organ systems, clinical medicine) | **10-14 pages** | Cardiology, Respiratory, Renal, GI |
| **Low** (clinical, ethics, psychiatry, biostatistics) | **14-16 pages** | Social Sciences, Psychiatry, Biostatistics |

### Prompt Sections-per-Podcast Guidelines

| Content Density | Max Numbered Sections | Sweet Spot |
|----------------|----------------------|-----------|
| **High** | 5-6 sections | ~3,000-4,000 chars |
| **Medium** | 7-8 sections | ~3,500-4,500 chars |
| **Low** | 8-9 sections | ~4,000-4,800 chars |

### Split Decision Flowchart

1. Count source pages
2. Classify content density (high/medium/low)
3. Divide pages by max-pages-per-podcast → number of parts
4. Find natural topic boundaries for split points
5. Write prompts with appropriate section counts per part
6. **Validate: if a prompt has >6 dense sections or >9 medium sections, split further**
7. After validation, split PDF and OCR markdown at matching boundaries

### Tested Split Examples

| Chapter | Pages | Density | Parts | Result |
|---------|-------|---------|-------|--------|
| Ch18 Pathology | 8 | Medium | 1 | 100% |
| Ch01 General Principles | 16 | High | 1 | 97% |
| Ch15 Infectious Disease | 30 | High | 2 (15+15) | 97% |
| Ch06 Gastroenterology | 36 | Medium | 3 (12+12+12) | Not tested |
| Ch16 Biochemistry | 27 | High | 3 (14+6+7) | A=100%, B1/B2=pending |
| Ch17 Hematology/Onc/Immuno | 36 | Medium | 3 (14+13+9) | 97% |

### Hard Limit
**NotebookLM's customization box silently truncates at ~5,000 characters.** Prompts MUST stay under 4,900 chars. Use dense notation: = instead of "is", → instead of "leads to", drop articles, abbreviate (HR, BP, HTN, HF, Rx, DOC).

### Source Upload Strategy (Tested)
Testing across 3 podcasts (Ch1 V2, Ch1 V3, Ch15A) proved that **the prompt is the primary driver of coverage, not the source format**:

| Config | Coverage |
|--------|----------|
| Old prompt + PDF only | 83% |
| **Revised prompt + PDF only** | **~97%** |
| Revised prompt + PDF + OCR markdown | ~97% |

The OCR markdown adds no measurable coverage improvement. The prompt's explicit topic enumeration is what forces NotebookLM to cover content.

Source upload order:
1. **Primary**: Chapter PDF
2. **Optional enrichment**: OCR'd markdown (not required — use it to help *you* write a better prompt by identifying table/diagram content)
3. **Supplementary**: Vignettes file

When writing prompts, **pay special attention to content from tables, diagrams, and flowcharts** — explicitly name every item since these are at highest risk of being skipped if not in the prompt. Use the OCR markdown as a reference while authoring the prompt, even if you don't upload it to NotebookLM.

### The Golden Rule
**If a topic, drug, pathway, or association exists in the source material and is NOT explicitly named in the prompt, NotebookLM will likely skip it.** There is no shortcut — you must name everything.

## Vignettes File Format

```markdown
# Clinical Vignettes Relevant to {Chapter Name}

Use these vignettes to teach concepts from the {Chapter Name} chapter in Step 1 question stem language.

---

## {Topic Group 1} Vignettes

- {Clinical scenario} → {Diagnosis}
- {Clinical scenario} → {Diagnosis}

## {Topic Group 2} Vignettes

- {Clinical scenario} → {Diagnosis}

## Management Principles

- {Management pearl relevant to chapter}
- {Management pearl relevant to chapter}
```

Only include vignettes that directly map to chapter topics. Do not include tangential vignettes from other organ systems.
