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
| `include` | Meets all PICOS criteria; counts toward the 185 |
| `exclude` | Fails ≥1 criterion; an exclusion reason is recorded |
| `flagged` | Cannot be decided from title/abstract; full text sought |
| `background_only` | Relevant to framing but not primary evidence — reviews, foundational method papers, non-brain instability work. **Cited as context, never counted in the 185** |

**Exclusion reason taxonomy** (one per excluded record, applied at both stages):
`out_of_scope`, `wrong_intervention_or_index`, `wrong_outcome`, `wrong_population`,
`wrong_study_design`, `review_editorial_protocol_commentary`, `insufficient_information`,
`non_english`.

## 4. Screening procedure, and how it was actually done

**This section is deliberately explicit, because the procedure departs from the two-independent-
human-reviewers norm.**

- **Stage 1 (title/abstract, n=26,924).** Screened by LLM against a fixed written rubric
  derived from the criteria above. Records the model could not decide were labelled `flagged`
  and carried forward rather than excluded — a deliberately over-inclusive rule (1,040 records
  were flagged and their full text sought).
- **Stage 2 (full text, n=562).** Same PICOS criteria applied to retrieved full texts. 66
  initially-flagged records were re-adjudicated with a higher-capability model; 0 remained
  flagged. 7 records carry `needs_human_review` within a decided category.
- **Human involvement.** Every record labelled `include` at full-text stage (n=185) was
  verified against its full text by the authors. Exclusions were not all independently
  re-checked by a second human.

**Limitation.** This is not dual independent human screening, and no inter-rater reliability
statistic (κ) is reported, because there were not two independent human passes over the same
records to compute one from. Any κ or screening-sensitivity figure appearing in the manuscript
without a stated estimator, subset, and gold standard should be removed or substantiated.

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
in the 185; studies that *frame its argument* were not.
