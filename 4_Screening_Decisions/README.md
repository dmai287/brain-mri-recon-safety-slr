# Screening decisions — data dictionary

Two files, one row per record, covering every eligibility decision in the review.

| File | Rows | Columns | Stage |
|---|---|---|---|
| `abstract_screening_decisions.csv` | 26,924 | 14 | Title and abstract, all deduplicated records |
| `fulltext_screening_decisions.csv` | 562 | 22 | Full text, original retrieval pass |
| `fulltext_screening_decisions_round2.csv` | 169 | 18 | Full text, post-registration second screening round (2026-08-07) — see amendments log D5 |

Decisions were made by the three reviewers against the fixed rubric in
`../1_Protocol_and_Registration/04_eligibility_criteria.md`. Automation was confined to record
acquisition — the seven database APIs, multi-tier deduplication, and full-text retrieval. No
automated tool assigned an eligibility decision.

---

## `abstract_screening_decisions.csv`

| Column | Type | Description |
|---|---|---|
| `file` | text | Source note filename for the record |
| `pmid` | text | PubMed identifier where one exists |
| `doi` | text | DOI where one exists |
| `decision` | enum | `exclude` 25,573 · `flagged` 1,040 · `background_only` 202 · `include` 109 |
| `reason_label` | enum | Controlled reason code. Most frequent: `wrong_intervention_or_index` 11,652 · `wrong_population` 9,130 · `out_of_scope` 4,305 · `insufficient_information` 1,066 |
| `primary_reason` | text | Free-text statement of the deciding reason |
| `picos_population` | text | Which PICOS facet the record satisfied or failed, one column per facet |
| `picos_intervention` | text | " |
| `picos_comparator` | text | " |
| `picos_outcome` | text | " |
| `picos_study_design` | text | " |
| `evidence_spans` | text | Verbatim spans from the title or abstract supporting the decision |
| `confidence_score` | float | Rubric margin — see below |
| `confidence` | enum | Band derived from `confidence_score` — see below |

`flagged` records were not excluded. All 1,040 were carried forward and their full text sought,
a deliberately over-inclusive rule.

## `fulltext_screening_decisions.csv`

| Column | Type | Description |
|---|---|---|
| `timestamp_utc` | ISO 8601 | When the decision was written to the log |
| `pmid`, `doi`, `year`, `title`, `journal` | text | Record identity |
| `decision` | enum | (this file only) `exclude` 363 · `include` 185 · `background_only` 14 |
| `stage` | enum | `fulltext_screening` 496 (primary screen) · `fulltext_Thu_adjudication` 66 (records still flagged after the primary screen). The `+reverified_clean_data` suffix on 2 rows marks re-verification after a corrupted PDF was re-retrieved |
| `include_reason` | text | Populated on the matching decision; blank otherwise |
| `exclude_reason` | text | " |
| `flag_reason` | text | " |
| `background_reason` | text | " |
| `needs_human_review` | bool | `TRUE` on 7 records that carry a residual query inside an already-decided category |
| `reviewer_votes` | JSON | Full vote trail, e.g. `{"Dat Mai_fulltext": "flagged", "Thu_adjudicator": "include"}` |
| `evidence_spans` | text | Verbatim spans from the full text supporting the decision |
| `source_path`, `copy_path` | path | Where the PDF was read from and archived to |
| `confidence_score` | float | Rubric margin — see below |
| `confidence` | enum | Band derived from `confidence_score` — see below |
| `adjudicator_votes` | JSON | `reviewer_votes` filtered to the adjudication pass only; non-empty on the 66 adjudicated records |
| `primary_screen_vote_count` | int | Number of primary-screen votes on the record (1 throughout) |
| `primary_screen_votes_summary` | JSON | Those votes tallied by label, e.g. `{"exclude": 1}` |

---

## `confidence_score` and `confidence`

**`confidence_score` is a rubric margin, not a certainty that the decision is correct.** It
records how decisively the criterion that settled the record matched it. Values are discrete and
drawn from the rubric, not continuous estimates.

The distinction matters, and the data shows why. At full text the median score is **0.6 on
`include`** and **0.8 on `exclude`**. If the field meant certainty-of-correctness, inclusions —
the decisions verified most carefully, each checked against the full text — would score highest.
They score lowest, because exclusion criteria settle a record decisively on one failed facet
(wrong population, review article, non-English), whereas inclusion requires every PICOS facet to
hold and therefore sits nearer the margin.

Read the field as *how clear-cut was this call under the rubric*, and low scores on included
studies read correctly: those were the judgement calls.

**`confidence` bands** `confidence_score` at fixed thresholds:

| Band | Range | Abstract | Full text |
|---|---|---|---|
| `low` | < 0.70 | 119 | 216 |
| `medium` | 0.70 – 0.849 | 4,912 | 174 |
| `high` | ≥ 0.85 | 21,893 | 172 |

Thresholds are applied to the value, so records with equal `confidence_score` always share a
band. An earlier revision of these files binned by rank into equal thirds, which split tied
scores across bands — 0.85 appeared as both `low` and `medium`. That revision is superseded;
`confidence` is now reproducible from `confidence_score` alone.

---

## Reconciliation to the PRISMA flow

| Count | Where |
|---|---|
| 26,924 records screened at title and abstract | `abstract_screening_decisions.csv`, all rows |
| 1,040 flagged + 109 included = 1,149 sought at full text | `decision` in (`flagged`, `include`) |
| 562 retrieved and screened at the original pass | `fulltext_screening_decisions.csv`, all rows |
| 169 retrieved and screened in the second full-text round (165 unique + 4 re-verifications) | `fulltext_screening_decisions_round2.csv`, all rows |
| **727 assessed · 220 included · 491 excluded · 16 background** | union of the two full-text files (4 overlapping records counted once, decisions identical) |
| 422 sought but not retrieved | 9 PMC-embargoed (release 2026-10 to 2027-07) · 1 not licensed to the institution · 1 no locatable copy · 411 no open-access copy and no subscription access |

`background_only` records are cited as context and are **not** among the 220 included studies.

The three screening files above are the primary record of what was decided. The retrieval
log in `../2_PRISMA/` is a secondary record of what was fetched; its final tallies now match
these files, and its superseded 2026-07-27 intermediate batch is retained inside it for
provenance.
