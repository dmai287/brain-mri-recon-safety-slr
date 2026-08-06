# File manifest — what is in this deposit

39 files, ≈ 19 MB, well within OSF's 5 GB per-file limit. **All paths below are relative to the
root of this deposit**, so they resolve as written whether you are reading the OSF project or the
GitHub mirror. `MANIFEST.csv` at the root carries the same list with byte sizes and SHA-256
prefixes for integrity checking.

---

## Component 0 — Manuscript

| File | Size | Notes |
|---|---|---|
| `0_Manuscript/manuscript_brain_mri_reconstruction_safety_review.pdf` | 1.1 MB | Compiled manuscript, 30 pp. |
| `0_Manuscript/manuscript_source.tex` | 149 KB | LaTeX source of the same |

## Component 1 — Protocol and registration

| File | Size | Notes |
|---|---|---|
| `1_Protocol_and_Registration/00_START_HERE.md` | 5.5 KB | Registration status disclosure — read first |
| `1_Protocol_and_Registration/01_registration_metadata.md` | 5.9 KB | Authors, affiliations, OSF roles |
| `1_Protocol_and_Registration/02_protocol_PRISMA-P.md` | 10.3 KB | The protocol, reported against PRISMA-P |
| `1_Protocol_and_Registration/03_search_strategy_PRISMA-S.md` | 9.9 KB | Full search strings, per database |
| `1_Protocol_and_Registration/04_eligibility_criteria.md` | 5.0 KB | PICOS + screening rules |
| `1_Protocol_and_Registration/05_data_extraction_form.md` | 4.5 KB | Extraction form |
| `1_Protocol_and_Registration/06_risk_of_bias_plan.md` | 7.1 KB | Appraisal plan |
| `1_Protocol_and_Registration/07_amendments_and_deviations.md` | 7.9 KB | **Deviations log** |
| `1_Protocol_and_Registration/08_file_manifest.md` | — | This file |
| `1_Protocol_and_Registration/protocol.json` | 7.4 KB | Machine-readable protocol, as fixed 2026-07-23 |
| `1_Protocol_and_Registration/search_strategy.json` | 1.1 KB | Machine-readable search specification, same date |
| `1_Protocol_and_Registration/ie_criteria.yaml` | 6.7 KB | Operational screening criteria |
| `1_Protocol_and_Registration/reviewer_signoff/README.md` | 6.1 KB | How the three-reviewer sign-off was run |
| `1_Protocol_and_Registration/reviewer_signoff/reviewer_worksheet_R1.csv` | 12.3 KB | Reviewer 1 worksheet |
| `1_Protocol_and_Registration/reviewer_signoff/reviewer_worksheet_R2.csv` | 12.4 KB | Reviewer 2 worksheet |
| `1_Protocol_and_Registration/reviewer_signoff/reviewer_worksheet_R3.csv` | 12.5 KB | Reviewer 3 worksheet |
| `1_Protocol_and_Registration/reviewer_signoff/merge_reviewers.py` | 6.7 KB | Merges the three worksheets; reports agreement and disagreements |

`protocol.json` and `search_strategy.json` record the review as specified on 2026-07-23, before
screening. Their value is as the fixed *a priori* specification: the criteria, concepts, date
range, and languages are as originally set and have not been edited to match what the executed
review turned out to find. The `_meta` block in `protocol.json` retains the research question
and the generation date.

## Component 2 — PRISMA flow and checklist

| File | Size | Notes |
|---|---|---|
| `2_PRISMA/PRISMA_2020_checklist_supplement.md` | 3.4 KB | Completed PRISMA 2020 checklist, item by item |
| `2_PRISMA/PRISMA_flow_report.md` | 3.7 KB | Flow counts, human-readable |
| `2_PRISMA/PRISMA_flow_report.json` | 5.3 KB | Same, machine-readable |
| `2_PRISMA/prisma_log.json` | 4.8 KB | Stage-by-stage log the flow report is built from |
| `2_PRISMA/prisma_identification.json` | 966 B | Per-database identification counts |

## Component 3 — Included studies and per-study data

| File | Size | Notes |
|---|---|---|
| `3_Included_Studies/included_characteristics.csv` | 116 KB | Per-study characteristics, all 185 (PRISMA item 19) |
| `3_Included_Studies/included_characteristics_supplement.csv` | 211 KB | Per-study appraisal with verbatim quotations (item 18) |
| `3_Included_Studies/included_characteristics_README.md` | 6.3 KB | Data dictionary for both CSVs |
| `3_Included_Studies/included_studies_185.bib` | 81 KB | BibTeX for all 185, with DOIs |
| `3_Included_Studies/quadas_worksheets/batch1–6.json` | ~107 KB | Raw QUADAS-2 worksheets with supporting evidence |

The supplement carries `rater_status = verified` on the 32 QUADAS-2 rows, naming all three
reviewers in the `reviewer_1/2/3` columns; the remaining 153 rows carry
`n/a — evidence-linked extraction, not a rated appraisal`. That column is the honest record of
which rows are rated appraisals and which are not — it is deliberately released intact.

## Component 4 — Screening decisions

| File | Size | Notes |
|---|---|---|
| `4_Screening_Decisions/abstract_screening_decisions.csv` | 17.1 MB | All 26,924 title/abstract decisions |
| `4_Screening_Decisions/fulltext_screening_decisions.csv` | 400 KB | All 562 full-text decisions with reasons |

The 17.1 MB file is large but well within OSF limits, and it is the single most useful artifact
for anyone auditing selection. The manuscript cites `fulltext_screening_decisions.csv` by name,
and that citation resolves against this component as named.

## Component 5 — Analysis code

| File | Size | Notes |
|---|---|---|
| `5_Code/prep_corpus.py` | 6.9 KB | Builds the per-study record set |
| `5_Code/assemble.py` | 12.4 KB | Builds both release CSVs and verifies them against the paper |

---

## Deliberately not deposited

| Path in the working review | Size | Reason |
|---|---|---|
| `Full Text Screening/` (PDF, PDF-Missing, Retrieved Records) | **4.0 GB** | **Publisher-copyright PDFs.** Redistributing them breaches licence terms; identifiers are released instead |
| `Dedup/` | 260 MB | Bulk retrieved records containing copyrighted abstracts |
| `Articles/` | 221 MB | As above |
| `Raw XML/` | 127 MB | Raw API payloads |
| `Abstract Screening/` subfolders | 57 MB | Per-record copies; the decisions CSV is deposited instead |
| `RAG/*.db` | 47 MB | Derived index containing substantial verbatim full text |
| `Knowledge Base/`, `Concept Library/` | — | Derived from copyrighted full texts |
| `*.env`, `edge_*.db`, `temp_chrome_cookies.db*` | — | **Credentials and browser cookies. Never deposit** |
| `.obsidian/` | — | Local editor state |

Excluded material totals roughly **4.7 GB**, against ~19 MB deposited. The deposit carries every
artifact needed to audit the review; the exclusions are bulk copies of copyrighted sources and
local machine state.

Metadata (title, abstract, identifiers) may be redistributed for PubMed-sourced records;
full-text PDFs from commercial publishers may not. `included_studies_185.bib` identifies the
corpus in full by DOI.

---

## Deposit structure

```
(root)                      README.md, MANIFEST.csv
├── 0_Manuscript            compiled PDF + LaTeX source
├── 1_Protocol_and_Registration
│                           protocol, search strategy, criteria, deviations,
│                           reviewer sign-off worksheets
├── 2_PRISMA                flow report, log, identification counts, checklist
├── 3_Included_Studies      characteristics + appraisal CSVs, data dictionary,
│                           .bib, QUADAS-2 worksheets
├── 4_Screening_Decisions   title/abstract and full-text decision records
└── 5_Code                  prep_corpus.py, assemble.py
```

Registering the top-level OSF project captures all child components in one registration.

## Pre-flight check

- [x] No credential or cookie files anywhere in the deposit
- [x] No publisher PDFs
- [x] `rater_status` column intact in the supplement
- [x] Screening-decisions filenames match the manuscript's citations
- [x] `MANIFEST.csv` regenerated — every size and SHA-256 prefix current
- [ ] `TODO-INSERT-OSF-DOI` replaced in `0_Manuscript/manuscript_source.tex` (line 1332)
- [ ] `<COMMIT-SHA>` and Zenodo DOI replaced in the same file (line 1334)
- [ ] Thu Nguyen Thi Dang's ORCID added in `01_registration_metadata.md` (the last `_add_` cell; the other three are recorded)
- [ ] GitHub repository created and verified live, or the code component cited instead
- [ ] Project set **public** before registering
