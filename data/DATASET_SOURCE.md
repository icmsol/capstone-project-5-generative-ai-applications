# Dataset Source and Provenance

## Dataset
Federal Acquisition Regulation (FAR), Subpart 52.2, **Text of Provisions and Clauses**.

## Official source
Acquisition.gov, an official website of the U.S. General Services Administration.

## Frozen source version
- Federal Acquisition Circular: **FAC 2026-01**
- Effective date: **March 13, 2026**
- Source file: `FAR_FAC_2026-01.pdf`
- Source PDF page count: **2,026**
- Part 52.2 page range in the frozen PDF: **1437-2004**
- SHA-256: `f22a17e30ff99682edcba9f6827e349cac0ecbe8908888c08616a81397e85bca`

## Scope
The processed modeling dataset excludes:
- Section 52.200, which only describes the scope of the subpart.
- Reserved section headings that contain no provision or clause text.
- Repeated page headers, page footers, and intentionally blank pages.

The processed dataset contains **610** usable provision/clause records from a new public source that was not used in Capstone Projects 1-4.

## Reproducibility
The extraction script records the deterministic section-boundary and cleaning rules. The original source PDF is retained so the processed CSV can be regenerated and audited.

## Responsible-use note
The FAR text is used as an academic modeling corpus. Generated text will not be represented as legally valid, current, complete, or suitable for insertion into an acquisition document. Human validation against authoritative source material is required.
