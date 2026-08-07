# Eligibility criteria and screening rules

Source of record: `../protocol.json` (fixed 2026-07-23) and `../ie_criteria.yaml`.

---

## 1. PICOS

| Element | Included | Excluded |
|---|---|---|
| **Population** | AI/ML-based brain MRI reconstruction — accelerated/undersampled, denoising, super-resolution, motion correction, generative/diffusion, self-supervised. General reconstruction methods clearly applicable to brain MRI | Non-brain anatomy only; non-MRI modalities; animal-only; phantom-only; post-mortem |
| **Intervention** | Any method for evaluating reconstruction safety, reliability, or fidelity | Studies reporting no evaluation of reconstruction output |
| **Comparator** | Radiologist ground truth, conventional fidelity metrics, other automated evaluators, or none where a new metric is proposed | — |
| **Outcome** | Detection or quantification of reconstruction safety failure: hallucinated/fabricated pathology, omitted true pathology, geometric or anatomical distortion, artifacts, robustness/distribution-shift failure, observer performance | Studies reporting only acquisition speed, or fidelity metrics with no bearing on diagnostic content |
| **Study design** | Primary methodological/technical studies; diagnostic-accuracy studies; reader/observer studies | Reviews, editorials, letters, commentaries, protocols; single-case reports; superseded conference versions |

## 2. Additional criteria

| Criterion | Rule |
|---|---|
| Language | English. Non-English full text excluded (n=1) |
| Date | **No limit.** No lower bound; upper bound = search date (July 2026). Included studies span 1995–2026 |
| Publication type | Peer-reviewed journal articles and conference papers |
| Preprints | **Excluded a priori.** Removed before deduplication; 0 retained |
| Full text | Required for inclusion. Records whose full text could not be obtained were not included |

> The original protocol admitted "reputable preprints (arXiv/medRxiv)". This was reversed
> before screening — see `07_amendments_and_deviations.md`, item D2.

## 3. Decision labels

Every screened record received exactly one:

| Label | Meaning |
|---|---|
| `include` | Meets all PICOS criteria; counts toward the 220 |
| `exclude` | Fails ≥1 criterion; an exclusion reason is recorded |
| `flagged` | Cannot be decided from title/abstract; full text sought |
| `background_only` | Relevant to framing but not primary evidence — reviews, foundational method papers, non-brain instability work. **Cited as context, never counted in the 185** |

**Exclusion reason taxonomy** (one per excluded record, applied at both stages):
`out_of_scope`, `wrong_intervention_or_index`, `wrong_outcome`, `wrong_population`,
`wrong_study_design`, `review_editorial_protocol_commentary`, `insufficient_information`,
`non_english`.

## 4. Screening procedure, and how it was actually done

**This section is deliberately explicit, because how records were screened determines what the
selection counts can be relied on to mean.**

- **Stage 1 (title/abstract, n=26,924).** Screened by the three reviewers (Dat Tat Mai, Thai
  Viet Pham, Thu Nguyen Thi Dang) against a fixed written rubric derived from the criteria
  above. Records that could not be decided from title and abstract alone were labelled
  `flagged` and carried forward rather than excluded — a deliberately over-inclusive rule
  (1,040 records were flagged and their full text sought). Decisions were consolidated to one
  per record, so the released Stage 1 file carries a single decision column rather than
  per-reviewer votes.
- **Stage 2 (full text, n=727; 562 at the original pass + 165 in the post-registration second screening round — see amendments log D5).** The same PICOS criteria applied to retrieved full texts. The
  primary full-text screen is recorded under Dat Tat Mai; the 66 records still flagged after it
  were adjudicated by Thu Nguyen Thi Dang against the full text, leaving 0 flagged. 7 records
  carry `needs_human_review` within a decided category. Both vote trails are released in
  `4_Screening_Decisions/fulltext_screening_decisions.csv`.
- **Automation.** Confined to record acquisition: the seven database APIs, multi-tier
  deduplication, and full-text retrieval were scripted. No automated tool assigned an
  eligibility decision.
- **Human involvement.** Every record labelled `include` at full-text stage (n=220) was
  verified against its full text by the authors.

**Limitation.** Exclusions were not all independently re-screened by a second reviewer, so no
inter-rater reliability statistic (κ) is reported for screening: there is no second recorded
pass over the same excluded records to compute one from. Any κ or screening-sensitivity figure
appearing in the manuscript without a stated estimator, subset, and gold standard should be
removed or substantiated.

## 5. Borderline classes and how they were handled

Three classes a reader would expect to find among the included studies, and where they went:

1. **Major secondary syntheses** of deep-learning MRI reconstruction — matched on topic but
   are reviews, not primary studies → `background_only`, cited in Related Work.
2. **Foundational reconstruction papers** (SENSE, compressed sensing, unrolled networks,
   DAGAN and similar) — establish methods but report no evaluation of diagnostic failure
   modes, pathology preservation, or observer performance → excluded as `wrong_outcome`.
3. **Deep-inverse-problem instability work** (hallucination and instability analyses) — bears
   directly on the argument but is not specific to human brain MRI → excluded as
   `out_of_scope`, cited as context.

The operative distinction throughout: studies that *supply the review's evidence* were counted
in the 220; studies that *frame its argument* were not.
