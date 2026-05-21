---
name: text-faithful-image-reconstruction
description: Rebuild scanned pages, textbook images, worksheets, forms, and document photos with image-model reconstruction while preserving exact readable text, numbers, punctuation, layout, typography, tables, labels, illustrations, and page order. Use when a user asks to restore, reconstruct, regenerate, reprint, upscale, clean, or convert low-quality document images into faithful print-ready images rather than applying a simple enhancement filter.
---

# Text-Faithful Image Reconstruction

Use this skill as a strict reconstruction protocol for scanned pages and document-like images. The goal is a clean master-print version of the same page, not a redesigned or creatively enhanced image.

## Core Standard

Treat the source image as the only authority.

Preserve exactly:
- readable text, numbers, dates, punctuation, symbols, and page numbers
- typography style, weight, size, line breaks, and alignment
- layout, margins, tables, grid lines, labels, captions, and illustrations
- image/page order and filename numbering in batches

If a region is uncertain, preserve the original appearance rather than inventing, correcting, or completing it.

## Forbidden Changes

Do not:
- rewrite, paraphrase, translate, or correct text
- hallucinate missing letters or labels
- redesign pages, tables, diagrams, or illustrations
- change margins, page proportions, reading order, or visual hierarchy
- over-sharpen, threshold, vectorize, posterize, or hard-clip the background
- make the result look like generic AI art

## Workflow

1. Inspect the image at full available detail.
2. Identify high-risk content: small text, page numbers, dates, labels, tables, captions, speech bubbles, math symbols, and brand/product names.
3. For text-heavy pages, include the visible text explicitly in the image edit prompt.
4. Instruct the image model to use the source image as the only content source.
5. Request conservative reconstruction: gentle denoise, natural white balance, stable ink, clean background, and print-safe contrast.
6. Preserve illustrations as the same original drawings, only cleaned and stabilized.
7. Review the generated result for changed text, fake letters, missing labels, wrong numbers, or layout drift.
8. Regenerate with stricter text instructions if any content changes.
9. Save each output with the same numbering scheme as the input.

## Prompt Skeleton

Use this base prompt and add page-specific visible text when needed:

```text
Use the provided scanned page as the only edit target and content source. Reconstruct it conservatively into a clean print-ready document image while preserving exact page proportions, layout, margins, typography, line breaks, spacing, tables, labels, illustrations, colors, and page number.

Absolute text fidelity is mandatory. Preserve every readable character exactly as shown. Do not rewrite, translate, correct, paraphrase, invent, remove, or alter any text, punctuation, numbers, symbols, labels, or formatting.

Only clean scan noise, stabilize faded ink, gently normalize the background, restore natural print contrast, and improve readability. Avoid fake letters, text hallucination, layout drift, hard white clipping, oversharpening, redesigned artwork, altered margins, or AI-looking redraw.

The result should look like the original publisher exported a clean master print version of this exact page.
```

For more prompt patterns, read `references/prompt-patterns.md`.

## Batch Checks

When processing numbered image batches, verify all expected outputs exist before finishing. Use `scripts/verify_sequence.py` when helpful:

```bash
python scripts/verify_sequence.py /path/to/output --start 1 --end 64 --ext .png
```

Report missing files and any pages that were regenerated because of text errors.
