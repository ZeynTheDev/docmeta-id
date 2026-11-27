# DocMeta-ID Annotation Guidelines

Version: 1.0

## 1. Objective

This guideline defines how document metadata
must be transcribed from document images.

## 2. Target Fields

### 2.1 Document Numbers

All document numbers visible in the selected
document page must be transcribed.

Rules:
- Preserve leading zeros.
- Preserve punctuation and separators.
- Preserve capitalization.
- Exclude the field label "NOMOR".
- Preserve reading order from top to bottom.
- Each distinct number is one array element.

### 2.2 Document Subject

The document subject may originate from:

- PERIHAL
- HAL
- TENTANG
- JUDUL
- Other explicitly identified subject fields.

Rules:
- Preserve the original words.
- Preserve capitalization.
- Join line breaks using a single space.
- Exclude the field label.
- Do not paraphrase or infer missing text.

## 3. Multiple Document Numbers

When a document contains several official numbers,
record all numbers in one document record.

The order must follow their visual reading order.

## 4. Missing or Unreadable Fields

Documents with missing or unreadable target fields
must be flagged and reviewed.

Do not guess metadata from document context.

## 5. Annotation Verification

Each record must have:
- An annotator identifier.
- A guideline version.
- A verification status.

Disagreements must be recorded and adjudicated.

## 6. Example

Input:
NOMOR 1497 TAHUN 2025
NOMOR 2 TAHUN 2025
NOMOR 5 TAHUN 2025

Output:
[
  "1497 TAHUN 2025",
  "2 TAHUN 2025",
  "5 TAHUN 2025"
]

