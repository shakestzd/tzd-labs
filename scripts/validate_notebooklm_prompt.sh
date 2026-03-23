#!/usr/bin/env bash
# Validates a NotebookLM prompt file to ensure the prompt content
# stays within NotebookLM's ~5,000 character customization box limit.
#
# Usage: bash validate_notebooklm_prompt.sh <prompt_file.md>
#
# Checks:
#   1. File exists and contains a code block
#   2. Prompt content (between ``` markers) is under the character limit
#   3. Reports exact character count and how much to trim if over

set -euo pipefail

LIMIT=4900
WARN=4500

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <prompt_file.md>"
  exit 1
fi

FILE="$1"

if [[ ! -f "$FILE" ]]; then
  echo "❌ File not found: $FILE"
  exit 1
fi

# Extract content between the first pair of ``` markers (allowing optional info strings like ```markdown)
PROMPT_CONTENT=$(sed -n '/^```[a-zA-Z]*$/,/^```$/p' "$FILE" | sed '1d;$d')

if [[ -z "$PROMPT_CONTENT" ]]; then
  echo "❌ No code block found in $FILE"
  echo "   The prompt must be wrapped in triple backtick markers (\`\`\`)"
  exit 1
fi

CHAR_COUNT=${#PROMPT_CONTENT}
LINE_COUNT=$(echo "$PROMPT_CONTENT" | wc -l | tr -d ' ')

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "NotebookLM Prompt Validation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "File:       $(basename "$FILE")"
echo "Chars:      $CHAR_COUNT / $LIMIT"
echo "Lines:      $LINE_COUNT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [[ $CHAR_COUNT -gt $LIMIT ]]; then
  OVER=$((CHAR_COUNT - LIMIT))
  echo "❌ OVER LIMIT by $OVER characters"
  echo ""
  echo "   NotebookLM silently truncates at ~5,000 chars."
  echo "   Your prompt will be cut off, losing content from the end."
  echo ""
  echo "   Compression tips:"
  echo "   - Remove articles (a, the, an)"
  echo "   - Use = instead of 'is', → instead of 'leads to'"
  echo "   - Use abbreviations: HR, BP, HTN, HF, Rx, DOC, MOA, dx"
  echo "   - Drop parenthetical explanations that repeat source content"
  echo "   - Merge numbered sections if content is related"
  echo "   - For chapters >20 pages, split into multiple prompts"
  exit 1
elif [[ $CHAR_COUNT -gt $WARN ]]; then
  REMAINING=$((LIMIT - CHAR_COUNT))
  echo "⚠️  Close to limit — $REMAINING chars remaining"
  echo "   Consider trimming if you need to add more content."
  exit 0
else
  REMAINING=$((LIMIT - CHAR_COUNT))
  echo "✅ Under limit — $REMAINING chars remaining"
  exit 0
fi
