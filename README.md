# Text-Faithful Image Reconstruction

A Codex skill for reconstructing scanned pages and document-like images into clean, print-ready outputs while preserving exact readable text, layout, typography, tables, labels, page numbers, and illustrations.

This is not a generic image enhancer. It is a reconstruction protocol for pages where content fidelity matters.

## What It Does

Use this skill for:

- low-quality textbook scans
- workbook and worksheet pages
- document photos
- scanned forms and tables
- comic/story pages with speech bubbles
- multi-page numbered image batches
- page images that need to look like clean publisher-master exports

The skill guides an AI agent to use image-model reconstruction conservatively, with strict rules against text hallucination, layout drift, or creative redesign.

## What It Preserves

- exact readable words
- exact numbers, dates, page numbers, and punctuation
- exact table and worksheet structure
- exact speech bubble text and labels
- original page proportions and margins
- original illustrations and visual hierarchy
- filename order for batches such as `0001.png` to `0064.png`

## What It Avoids

- rewriting or correcting text
- translating content
- inventing missing letters
- changing table structure
- modernizing illustrations
- fake vector redraws
- harsh thresholding or oversharpening
- generic AI-art style

## Install

Install from GitHub with:

```bash
npx skills add alghabry/text-faithful-image-reconstruction
```

If your skill runner requires a specific skill folder name, use:

```bash
npx skills add https://github.com/alghabry/text-faithful-image-reconstruction --skill text-faithful-image-reconstruction
```

## Basic Use

Example prompt:

```text
Use $text-faithful-image-reconstruction to reconstruct this scanned textbook page into a clean print-ready image. Preserve every readable character, table, label, page number, layout position, and illustration exactly.
```

## Example: Single Textbook Page

```text
Use $text-faithful-image-reconstruction on 0030.jpg.

Reconstruct the page so it looks like a clean publisher-master print version. Preserve all text exactly, including headings, table text, punctuation, page number, and layout. Do not redesign the page or change the illustration style.
```

## Example: Text-Heavy Page

```text
Use $text-faithful-image-reconstruction on this scanned page.

Important visible text to preserve exactly:
"Language summary"
"Ask and answer questions like these:"
"Did you have eggs for breakfast?"
"Yes, I did."
"No, I didn't."

Preserve punctuation, apostrophes, table cells, line breaks, and page number exactly.
```

## Example: Comic Or Story Page

```text
Use $text-faithful-image-reconstruction on this story page.

Preserve every speech bubble exactly. Do not change dialogue, apostrophes, question marks, or bubble order. Keep the original comic drawings as the same drawings, only cleaner and print-ready.
```

## Example: Batch Of Numbered Pages

```text
Use $text-faithful-image-reconstruction for all images from 0001.jpg to 0064.jpg.

Save outputs as 0001.png to 0064.png in the same order. After processing, verify that every output file exists and report any missing numbers.
```

The skill includes a small sequence checker:

```bash
python text-faithful-image-reconstruction/scripts/verify_sequence.py ./output --start 1 --end 64 --ext .png
```

## Quality Checklist

Before accepting an output, check:

- no word changed
- no number changed
- no punctuation changed
- no page number changed
- no table cells shifted
- no speech bubble text rewritten
- no fake tiny labels appeared
- no illustration content changed
- no margins or page proportions drifted

If any text changed, regenerate with stricter page-specific text instructions.

## Best Results

For pages with dense text, paste important visible text into the prompt. This gives the image model less room to guess.

For batch jobs, process pages one by one and verify the output sequence at the end.

## License

Use this skill only on documents and images you have the right to process.
