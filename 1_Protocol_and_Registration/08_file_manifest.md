# File manifest — what to upload to OSF

Total upload ≈ 19 MB, comfortably within OSF's 5 GB per-file limit. All paths are relative to
the review folder.

---

## Component 1 — Protocol and registration (root of the OSF project)

| File | Size | Notes |
|---|---|---|
| `Registration/00_START_HERE.md` | 4 KB | Registration status disclosure |
| `Registration/02_protocol_PRISMA-P.md` | 11 KB | The protocol |
| `Registration/03_search_strategy_PRISMA-S.md` | 8 KB | Full search strings, per database |
| `Registration/04_eligibility_criteria.md` | 6 KB | PICOS + screening rules |
| `Registration/05_data_extraction_form.md` | 5 KB | Extraction form |
| `Registration/06_risk_of_bias_plan.md` | 6 KB | Appraisal plan |
| `Registration/07_amendments_and_deviations.md` | 8 KB | **Deviations log** |
| `protocol.json` | 6.9 KB | Original machine-readable protocol, as fixed 2026-07-23 |
| `search_strategy.json` | 1.1 KB | Original search specification, same timestamp |
| `agent2_criteria.yaml` | 7.8 KB | Operational screening criteria |

Upload `protocol.json` and `search_strategy.json` **unmodified**. Their value is as the
original artifact; editing them to match the executed review would destroy that.

## Component 2 — PRISMA flow and checklist

| File | Size |
|---|---|
| `PRISMA_flow_report.md` | 3.7 KB |
| `PRISMA_flow_report.json` | 5.3 KB |
| `prisma_log.json` | 4.8 KB |
| `LaTex PDF/PRISMA_2020_checklist_supplement.md` | 3.4 KB |

## Component 3 — Included studies and per-study data

| File | Size | Notes |
|---|---|---|
| `LaTex PDF/included_characteristics.csv` | 116 KB | Per-study characteristics (PRISMA item 19) |
| `LaTex PDF/included_characteristics_supplement.csv` | 189 KB | Per-study appraisal (PRISMA item 18) |
| `LaTex PDF/included_characteristics_README.md` | 6 KB | Data dictionary |
| `LaTex PDF/included_studies_185.bib` | 81 KB | BibTeX for all 185 |
| `LaTex PDF/scripts/quadas_worksheets/*.json` | ~60 KB | Raw appraisal worksheets with evidence |

> The supplement carries `rater_status = pending_reviewer_verification` on every row. Upload
> it as-is — the status column is the honest record. Do not strip it.

## Component 4 — Screening decisions

| File | Size | Notes |
|---|---|---|
| `Full Text Screening/agent3_final_screening_decisions.csv` | 402 KB | All 562 full-text decisions with reasons |
| `Abstract Screening/agent2_final_screening_decisions.csv` | 17.5 MB | All 26,924 title/abstract decisions |

The 17.5 MB file is large but uploadable, and it is the single most useful artifact for anyone
auditing the selection process. Upload it. If you prefer to keep the project light, zip it —
but do not omit it, since the manuscript cites `fulltext_screening_decisions.csv` as released.

> **Filename note:** the manuscript refers to `fulltext_screening_decisions.csv`; the actual
> file is `agent3_final_screening_decisions.csv`. Either rename on upload or correct the
> manuscript so the citation resolves.

## Component 5 — Analysis code

| File | Notes |
|---|---|
| `LaTex PDF/scripts/prep_corpus.py` | Builds the per-study record set |
| `LaTex PDF/scripts/assemble.py` | Builds both release CSVs and verifies against the paper |

If the GitHub repository named in the manuscript is public and populated, link it instead and
note the commit hash. If it is not yet public, upload the scripts here — a manuscript pointing
at an empty or non-existent repository is a reviewer-facing problem.

---

## Do NOT upload

| Path | Size | Reason |
|---|---|---|
| `Full Text Screening/` (PDF, PDF-Missing, Retrieved Records) | **4.0 GB** | **Publisher-copyright PDFs.** Redistributing them breaches licence terms. Release identifiers only |
| `Dedup/` | 260 MB | Bulk retrieved records containing copyrighted abstracts |
| `Articles/` | 221 MB | As above |
| `Raw XML/` | 127 MB | Raw API payloads |
| `Abstract Screening/` subfolders | 57 MB | Per-record copies (the decisions CSV is uploaded separately) |
| `RAG/*.db` | 47 MB | Derived index containing substantial verbatim full text |
| `Knowledge Base/`, `Concept Library/` | — | Derived from copyrighted full texts |
| `*.env`, `edge_cookies_temp.db`, `edge_*.db`, `temp_chrome_cookies.db*` | — | **Credentials and browser cookies. Never upload** |
| `.obsidian/` | — | Local editor state |

Excluded material totals roughly **4.7 GB**, against ~19 MB uploaded. The upload carries every
artifact needed to audit the review; the exclusions are bulk copies of copyrighted sources and
local machine state.

Metadata (title, abstract, identifiers) may be redistributed for PubMed-sourced records;
full-text PDFs from commercial publishers may not. When in doubt, release the DOI list —
`included_studies_185.bib` already provides it.

---

## Suggested OSF structure

```
Project: The Metric Blind Spot in Deep Learning Brain MRI Reconstruction
├── (root)                    README, protocol, search strategy, criteria, deviations
├── Component: PRISMA         flow report, log, checklist
├── Component: Included data  characteristics + appraisal CSVs, README, .bib, worksheets
├── Component: Screening      full-text and abstract decision records
└── Component: Code           prep_corpus.py, assemble.py (or link to GitHub)
```

Registering the top-level project captures all child components in one registration.

## Pre-flight check

- [ ] No credential or cookie files anywhere in the upload set
- [ ] No publisher PDFs
- [ ] `protocol.json` / `search_strategy.json` uploaded unmodified
- [ ] `rater_status` column left intact in the supplement
- [ ] Screening-decisions filename reconciled with the manuscript citation
- [ ] GitHub link verified live, or scripts uploaded instead
- [ ] Project set **public** before registering
