# The Metric Blind Spot in Deep Learning Brain MRI Reconstruction

Protocol, search strategy, PRISMA records, per-study data, screening decisions, and analysis
code for a systematic review of how the safety, artifacts, and fidelity of deep-learning brain
MRI reconstruction are evaluated.

**27,327 records identified → 26,924 after deduplication → 562 full texts assessed → 185 studies
included**, spanning 1995–2026 across seven databases (PubMed/MEDLINE, SpringerLink, IEEE Xplore,
Scopus, Semantic Scholar, OpenAlex, Web of Science).

## Repository layout

| Path | Contents |
|---|---|
| `1_Protocol_and_Registration/` | Protocol as PRISMA-P 2015, search strategy as PRISMA-S, eligibility criteria, extraction form, appraisal plan, deviations log, plus the original machine-readable `protocol.json` and `search_strategy.json` |
| `2_PRISMA/` | Flow report, stage-by-stage `prisma_log.json`, per-database identification counts, completed PRISMA 2020 checklist |
| `3_Included_Studies/` | Per-study characteristics (PRISMA item 19), per-study quality appraisal with verbatim supporting quotations (item 18), data dictionary, BibTeX for all 185, raw QUADAS-2 worksheets |
| `4_Screening_Decisions/` | Every decision at both stages with its recorded reason — 26,924 title/abstract and 562 full-text |
| `5_Code/` | Scripts that build the per-study release files and verify them against the manuscript |
| `MANIFEST.csv` | Every file with size, source path, and SHA-256 prefix |

## Read this before using the appraisal data

**Ratings are pending reviewer verification.** Every row of
`included_characteristics_supplement.csv` carries `rater_status = pending_reviewer_verification`.
Ratings were produced by structured reading of each full text, with a verbatim quotation
recorded for every non-*Unclear* judgement so each can be checked against its source. They are
not yet a signed-off two-reviewer consensus. The column is deliberate — it is the honest record
of what the file is.

**Not every appraisal rests on full text.** Of the 36 QUADAS-2 appraisals, 26 are based on full
text, 3 on partial text, and 7 on abstract and controlled vocabulary only. The
`appraisal_basis` column records this per study, and it explains much of the *Unclear* band.

## Limitations recorded with the data

- Prevalence counts derived by keyword classification over titles, abstracts, and controlled
  vocabulary are **lower bounds**, not exhaustive counts.
- Six studies in the 36-study reader subset were found on appraisal to involve **no human
  readers**; they are flagged in `reader_subset_verified`.
- No citation chasing, grey-literature searching, or PRESS peer review of the search strategy
  was performed. Each reduces recall and is declared rather than omitted.
- Certainty of evidence was not formally graded (no GRADE or CERQual).
- Registration is **retrospective** — see `1_Protocol_and_Registration/00_START_HERE.md`.

## What is not here

Full-text PDFs of the included studies are **not** redistributed — publisher copyright. The
complete DOI list is in `3_Included_Studies/included_studies_185.bib`, so the corpus is fully
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
