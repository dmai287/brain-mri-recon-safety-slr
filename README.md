# The Metric Blind Spot in Deep Learning Brain MRI Reconstruction

Protocol, search strategy, PRISMA records, per-study data, screening decisions, and analysis
code for a systematic review of how the safety, artifacts, and fidelity of deep-learning brain
MRI reconstruction are evaluated.

**27,327 records identified → 26,924 after deduplication → 727 full texts assessed → 220 studies
included**, spanning 1995–2026 across seven databases (PubMed/MEDLINE, SpringerLink, IEEE Xplore,
Scopus, Semantic Scholar, OpenAlex, Web of Science).

## Repository layout

| Path | Contents |
|---|---|
| `0_Manuscript/` | The compiled manuscript (PDF) and its LaTeX source |
| `1_Protocol_and_Registration/` | Protocol as PRISMA-P 2015, search strategy as PRISMA-S, eligibility criteria, extraction form, appraisal plan, deviations log, the machine-readable `protocol.json` and `search_strategy.json` as fixed 2026-07-23, and the three reviewer sign-off worksheets with the script that merges them |
| `2_PRISMA/` | Flow report, stage-by-stage `prisma_log.json`, per-database identification counts, completed PRISMA 2020 checklist |
| `3_Included_Studies/` | Per-study characteristics (PRISMA item 19), per-study quality appraisal with verbatim supporting quotations (item 18), data dictionary, BibTeX for all 220, raw QUADAS-2 worksheets |
| `4_Screening_Decisions/` | Every decision at both stages with its recorded reason — 26,924 title/abstract and 727 full-text across two screening rounds |
| `5_Code/` | Scripts that build the per-study release files and verify them against the manuscript |
| `MANIFEST.csv` | Every file with size, source path, and SHA-256 prefix |

## Read this before using the appraisal data

**Ratings are verified.** The QUADAS-2 subset was independently appraised by three
reviewers (Dat Tat Mai, Thai Viet Pham, Thu Nguyen Thi Dang). They rated 36 studies as
originally classified — 252 domain judgements — and agreed on every one, so no
adjudication was required. Four of those 36 were subsequently found to involve no human
reader and were reclassified to the algorithmic subset, so the published QUADAS-2 subset
is 32 studies and 224 domain judgements; a second full-text screening round added 7 further
reader-design studies, appraised with the same instrument and independently verified by the
three reviewers on 2026-08-07, for a verified QUADAS-2 subset of 39. `rater_status` reads
`verified` on all 39 rows and each names the three reviewers. Because agreement was complete,
no chance-corrected coefficient is quoted — kappa is degenerate when one rating pattern is
unanimous. Each rating carries the verbatim quotation it rests on, so any row can be checked
against its source. The remaining 181 studies use the reproducibility checklist rather than
QUADAS-2; their fields are evidence-linked extractions, not rated appraisals.

**Not every appraisal rests on full text.** Of the 39 QUADAS-2 appraisals, 33 are based on full
text and 6 on abstract and controlled vocabulary only. The
`appraisal_basis` column records this per study, and it explains much of the *Unclear* band.

## Limitations recorded with the data

- Prevalence counts derived by keyword classification over titles, abstracts, and controlled
  vocabulary are **lower bounds**, not exhaustive counts.
- Four studies keyword-assigned to the reader subset had **no human reader** on inspection of
  their full text and were reclassified to the algorithmic subset; with the second round's 7 additions the verified subset is 39.
- No citation chasing, grey-literature searching, or PRESS peer review of the search strategy
  was performed. Each reduces recall and is declared rather than omitted.
- Certainty of evidence was not formally graded (no GRADE or CERQual).
- Registration is **retrospective** — see `1_Protocol_and_Registration/00_START_HERE.md`.

## What is not here

Full-text PDFs of the **included studies** are **not** redistributed — publisher copyright. The only PDF here is our own manuscript, in `0_Manuscript/`. The
complete DOI list is in `3_Included_Studies/included_studies_220.bib`, so the corpus is fully
identifiable. Also excluded: bulk retrieved-record copies, the derived vector index built from
full texts, and all local credentials and machine state.

## Reproducing the per-study files

```bash
cd 5_Code
python prep_corpus.py     # stage the per-study record set from the Include folder
python assemble.py        # build both release CSVs and verify against the manuscript
```

`assemble.py` prints a check of every derived figure against the published tables.

## Citation

See `CITATION.cff`. Article citation and DOI will be added on publication.

## Licence

CC BY 4.0 — see `LICENSE`. Third-party bibliographic metadata remains under its original terms.
