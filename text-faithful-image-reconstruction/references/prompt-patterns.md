# Prompt Patterns

Load this reference when a reconstruction task has dense text, tables, speech bubbles, tiny labels, or multi-page batch requirements.

## General Page Reconstruction

```text
Use the provided scanned page as the only edit target and content source. Reconstruct it conservatively into a clean print-ready page while preserving exact page proportions, layout, margins, typography, line breaks, spacing, illustrations, tables, labels, colors, and page number.

Absolute text fidelity is mandatory. Preserve every readable character exactly as shown. Do not rewrite, translate, correct, paraphrase, invent, remove, or alter any text, punctuation, numbers, symbols, labels, or formatting.

Only clean scan noise, stabilize faded ink, gently normalize the background, restore natural print contrast, and improve readability. Avoid fake letters, text hallucination, layout drift, hard white clipping, oversharpening, redesigned artwork, altered margins, or AI-looking redraw.
```

## Text-Heavy Page

```text
Preserve the following visible text exactly, including punctuation, capitalization, line breaks, apostrophes, page number, and spacing:

[paste exact visible text here]

If any word or character is uncertain, preserve the original scanned appearance rather than generating new text.
```

## Tables And Worksheets

```text
Preserve every table cell, grid line, column width, row height, alignment, and label exactly. Do not merge, split, straighten creatively, simplify, or redraw the table structure. Text must remain in the same cells with the same line breaks and punctuation.
```

## Speech Bubbles And Comics

```text
Preserve every speech bubble shape, tail direction, speaker placement, and bubble text exactly. Do not change dialogue, apostrophes, question marks, ellipses, capitalization, or bubble order. Keep the original comic/story artwork as the same drawing, only cleaned.
```

## Illustrations

```text
Keep the illustration as the same original drawing: same people, poses, objects, clothing, colors, style, and positions. Do not modernize, redesign, recompose, or add/remove content. Clean and stabilize the scan only.
```

## Multi-Page Batch

```text
Process pages independently. Use each source page as its only content source. Preserve filename numbering in the output. After generation, verify that every expected page exists and that no output number is missing.
```

## Regeneration Trigger

Regenerate the image if any of these appear:
- changed or invented words
- wrong page number
- fake labels or distorted small text
- altered table columns or row structure
- replaced illustration content
- layout drift or changed margins
- ellipsis or punctuation normalization that differs from the scan
