# Reviewer sign-off for the QUADAS-2 appraisal

> **2026-08-07 update (amendments log D5):** the post-registration second screening round added 35
> included studies (S186–S220), of which **7 are observer/reader designs that enter the
> QUADAS-2 subset.** They were appraised on 2026-08-07 with the same instrument and
> evidence-quotation rule (worksheet `quadas_worksheets/batch7.json`); their ratings were
> independently verified by the three reviewers on 2026-08-07 and carry
> `rater_status = verified`. The sign-off
> below covers the original worksheets and is unaffected: S001–S185 rows, ratings, and
> reviewer agreement are unchanged.

## What was done

**Three reviewers** — Dat Tat Mai, Thai Viet Pham, Thu Nguyen Thi Dang — independently appraised
the diagnostic-accuracy and reader studies against QUADAS-2, each recording ratings in their own
worksheet without sight of the others'. Their ratings agreed on **every domain judgement**, so no
adjudication was required and no disagreement log was produced.

| | |
|---|---|
| Reviewers | 3, rating independently |
| Studies rated | 36, as classified at the time of the appraisal |
| Domains per study | 7 — 4 risk-of-bias, 3 applicability |
| Domain judgements | 252, unanimous on all |
| Published QUADAS-2 subset | **32** studies, **224** domain judgements |

The gap between 36 and 32 is deliberate and documented: four studies keyword-assigned to the
reader subset were found on inspection of their full text to involve **no human reader**, and
were reclassified to the algorithmic subset. The worksheets still carry all 36 rows, because
they record what the reviewers actually assessed. `included_characteristics_supplement.csv`
carries `rater_status = verified` on the 32 that remain in the QUADAS-2 subset, naming all three
reviewers with a dated consensus note.

Agreed ratings over the published n=32 subset, as they appear in Table VII
(Low / Unclear / High):

| Domain | Low | Unclear | High |
|---|---|---|---|
| Patient selection | 7 | 15 | 10 |
| Index test | 17 | 9 | 6 |
| Reference standard | 16 | 9 | 7 |
| Flow and timing | 24 | 5 | 3 |

## Why no kappa is reported

Cohen's kappa is **degenerate when agreement is unanimous**: expected agreement is 1, so the
coefficient is undefined, and the 1.00 that some implementations return carries no information
about reliability. The manuscript states complete agreement and explains why no chance-corrected
coefficient is quoted, which is the correct handling.

Do not substitute an approximate figure. All three worksheets ship with this deposit, so any
reader can recompute the statistic and will see exactly what is described here.

## Files

| File | What it is |
|---|---|
| `reviewer_worksheet_R1.csv` | Reviewer 1's independent ratings, 36 studies × 7 domains |
| `reviewer_worksheet_R2.csv` | Reviewer 2's, same structure |
| `reviewer_worksheet_R3.csv` | Reviewer 3's, same structure |
| `merge_reviewers.py` | Reconciles the worksheets and writes the agreed ratings |

Each worksheet row carries `source_record` (the full-text filename the rating was made from) and
`appraisal_basis`. The latter matters when reading the *Unclear* band: of the published 32, 22
appraisals rest on full text, 3 on partial text, and 7 on abstract and controlled vocabulary
only. Where only an abstract was available, `Unclear` is the correct rating rather than a guess.
`06_risk_of_bias_plan.md` §2 maps QUADAS-2's clinical vocabulary onto reconstruction studies —
what counts as the index test, the reference standard, the target condition.

## Re-running or extending the appraisal

The tooling remains usable if the appraisal is ever repeated or extended. `merge_reviewers.py`
reads every `reviewer_worksheet_R*.csv` present, so it works with two reviewers or three.

```bash
python merge_reviewers.py
```

Reports per-domain unanimity and pairwise kappa, and writes `disagreements.csv` — one row per
domain where the reviewers differ, with each reviewer's rating and note side by side. Where the
ratings do not vary, it prints `n/a` for kappa and says why rather than printing a misleading
number.

Fill the `consensus` column for each disagreement, recording in `resolution` how it was settled
and in `adjudicated_by` who decided anything the reviewers could not settle themselves. Then:

```bash
python merge_reviewers.py --apply --r1 "Full Name" --r2 "Full Name" --r3 "Full Name"
```

This writes the agreed ratings into the supplement, sets `rater_status` to `verified`, records
the reviewer names and a dated consensus note, and backs up the previous file first. It refuses
to run if any disagreement lacks a consensus value or if a reviewer name is missing — the names
are the audit trail. Recompute the Table VII counts afterwards with `5_Code/assemble.py`.

> One person must not fill two worksheets. Two ratings from one head are one rating.

## What this sign-off does not cover

The other **153** included studies carry
`appraisal_instrument = Reproducibility & robustness checklist`, not QUADAS-2. Their `repro_*`
fields are extracted signals with evidence quotes — code availability, public dataset, benchmark,
reference standard, sampling, centres, ethics — rather than judgements, so they are outside this
sign-off and read `rater_status = n/a - evidence-linked extraction, not a rated appraisal`.
