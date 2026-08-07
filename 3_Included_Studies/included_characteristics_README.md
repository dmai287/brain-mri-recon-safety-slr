# Per-study release files — data dictionary and provenance

Two files accompany the review, matching the split promised in `brain_ieeetmi_v6.tex` L774:

| File | Purpose | PRISMA item |
|---|---|---|
| `included_characteristics.csv` | Per-study extracted characteristics (220 rows × 18 cols) | Item 19 — results of individual studies |
| `included_characteristics_supplement.csv` | Per-study quality appraisal / risk of bias (220 rows × 48 cols) | Item 18 — risk of bias in studies |

> **Status: `rater_status = verified` on the 32 QUADAS-2 rows.**
> Those studies were independently appraised by three reviewers — Dat Tat Mai, Thai Viet Pham,
> Thu Nguyen Thi Dang — whose independent ratings agreed on every domain judgement, so no
> adjudication was required. Each rating carries the verbatim quotation it rests on, so any row
> can be checked against its source. The other 153 rows use the reproducibility checklist rather
> than QUADAS-2: their fields are evidence-linked extractions, not rated appraisals, and read
> `rater_status = n/a - evidence-linked extraction, not a rated appraisal`.

---

## 1. `included_characteristics.csv`

| Column | Meaning | Provenance |
|---|---|---|
| `study_key` | Stable within-review ID (S001–S220, ordered by year) | assigned |
| `pmid`, `doi`, `year`, `journal`, `title` | Bibliographic identity | Include record front-matter |
| `study_design` | `Algorithmic / methodological reconstruction study` (n=153) or `Diagnostic accuracy / reader study` (n=32) | derived from `evaluation` |
| `method_family` | Reconstruction paradigm, `;`-separated multi-label | **carried through unchanged** |
| `evaluation` | Evaluation paradigm, `;`-separated multi-label | **carried through unchanged** |
| `failure_modes` | Reported failure modes, `;`-separated multi-label | **carried through unchanged** |
| `field_strength` | Single-label `3T` / `1.5T` / `7T` / `not reported` | **newly derived** (see §3) |
| `field_strength_evidence` | Verbatim snippet supporting the value | newly derived |
| `pulse_sequences` | `T1w;T2w;FLAIR;DWI;SWI` multi-label | **newly derived** |
| `reference_standard` | Fully sampled / expert consensus / conventional / not stated | newly derived |
| `public_dataset_or_benchmark` | Named public datasets detected (fastMRI, IXI, HCP, BraTS, …) | newly derived |
| `code_available` | `yes` / `not stated` | newly derived |
| `full_text_basis` | `full text` (≥10k chars) / `partial full text (truncated)` / `abstract + MeSH only` | derived |
| `source_record` | Filename in `Full Text Screening/Include/` | — |

The three **carried-through** columns are byte-identical to the previous file. They reproduce
every published aggregate exactly (method families 73/58/46/30/24/12/11 = 254 labels;
evaluation 45/32/15/11 = 103 labels, 15 multi-label, 8 with both pixel-wise and reader) and
were deliberately not recomputed.

## 2. `included_characteristics_supplement.csv`

- `appraisal_instrument` — `QUADAS-2` (the 32 reader/diagnostic studies) or
  `Reproducibility & robustness checklist` (the 153 algorithmic studies). QUADAS-2 is not
  applicable to the algorithmic subset, so those rows carry `n/a` in the domain columns,
  matching the paper's stated procedure.
- `rob_*` — the four QUADAS-2 **risk of bias** domains; `app_*` — the three **applicability
  concern** domains. Each is a triplet: `<domain>`, `<domain>_evidence` (verbatim quote from
  the study), `<domain>_rationale` (one sentence). Values: `Low` / `High` / `Unclear`.
- `repro_*` — reproducibility and robustness signals extracted for **all 220** studies:
  code availability, public dataset, named benchmark, reference standard, sampling
  (prospective/retrospective), centres (single/multi), ethics statement — each with evidence.
- `appraisal_basis` — what the rating rests on. **Only 22 of the 32 QUADAS-2 appraisals rest
  on full text**; 3 are partial (S046, S052, S059) and 7 are abstract-only.
- `reader_subset_verified` — `yes` for the 32 confirmed reader studies. Four studies keyword-
  assigned to this subset had **no human reader** on inspection of their full text and were
  reclassified to the algorithmic subset (**S107, S121, S145, S179**); S001 and S004 are genuine
  observer studies whose reader count was unextractable and were retained.
- `reviewer_1`, `reviewer_2`, `reviewer_3`, `consensus_note`, `rater_status` — sign-off record: Dat Tat Mai, Thai Viet Pham, Thu Nguyen Thi Dang.

## 3. Method and its limits

Characteristics classification follows the method stated in the paper: structured keyword
classification of **titles, abstracts, and MeSH terms**, reported as **lower bounds**.
Field strength and pulse sequences additionally use full text where available, because those
attributes are usually stated only in the acquisition subsection.

**No `rq_mapping` column is released.** The paper's RQ1/RQ2/RQ3 split (123 / 83 / 40) could
not be reproduced from the extracted data at any defensible keyword threshold — a broad rule
assigns RQ2 to nearly all studies, a narrow one to far fewer. Publishing a heuristic column
would imply traceability the data does not support. If you supply the rule actually used to
assign studies to research questions, the column can be regenerated.

## 4. Before you publish — required actions

1. ~~Verify the risk-of-bias worksheet.~~ **Done** — three reviewers, complete agreement,
   recorded in the sign-off columns and in `1_Protocol_and_Registration/reviewer_signoff/`.
2. ~~Reconcile Table VI and Table VII against the manuscript.~~ **Done** —
   Table VII replaced with the appraised counts; Table VI's publication-period and
   field-strength rows corrected; the "123 studies" claim resolved to 45.
3. ~~Decide on the flagged non-reader studies.~~ **Done** — four reclassified (S107, S121,
   S145, S179); S001 and S004 retained as genuine observer studies. Subset is n=32.
4. ~~Decide what the non-QUADAS rows should say.~~ **Done** — the 153 rows now read
   `n/a - evidence-linked extraction, not a rated appraisal`, which is what they are.

## 5. Reproducing

```
python prep_corpus.py     # stage 220 records + deterministic signals
python assemble.py        # build both CSVs + verify against the paper
```

Prior version of the mis-named file is preserved as
`included_characteristics_supplement.csv.orig-backup`.
