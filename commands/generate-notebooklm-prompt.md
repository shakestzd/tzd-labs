---
name: generate-notebooklm-prompt
description: Generate a NotebookLM Audio Overview prompt for a USMLE Step 1 chapter. Reads the chapter, extracts relevant vignettes, and produces a prompt + vignettes file.
argument-hint: "<chapter number or path to chapter PDF>"
---

Generate a NotebookLM Audio Overview customization prompt for the specified USMLE Step 1 chapter.

Use the `notebooklm-prompt-generator` agent to:

1. Read the chapter content from `$ARGUMENTS` (accept a chapter number like "3" or a path like "chapters/03_Endocrinology.pdf")
2. If a chapter number is given, find the matching PDF in the project's `chapters/` directory
3. Check if OCR'd markdown already exists in `markdown/` — if so, use it; if not, read the PDF directly
4. Extract relevant clinical vignettes from `markdown/20_Clinical_Vignettes_and_Management.md` and `markdown/21_Principles_of_Management.md`
5. Generate the prompt file at `notebooklm_prompts/{chapter_filename}.md`
6. Generate the vignettes file at `notebooklm_sources/{chapter_filename}_vignettes.md`
7. Report the character count of the prompt and list all topics covered
