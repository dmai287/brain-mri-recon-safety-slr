# Review protocol (PRISMA-P 2015)

**The Metric Blind Spot in Deep Learning Brain MRI Reconstruction: A Systematic Review and
Causal Safety Framework**

| | |
|---|---|
| Protocol first fixed | 2026-07-23 (`protocol.json`, `search_strategy.json`) |
| Searches executed | 2026-07-23 to 2026-07-24 |
| Screening began | 2026-07-27 |
| Review completed | 2026-08 |
| This document prepared | 2026-08-06 |
| Registration type | **Retrospective** — see `00_START_HERE.md` |

---

## ADMINISTRATIVE INFORMATION

### 1. Title
*The Metric Blind Spot in Deep Learning Brain MRI Reconstruction: A Systematic Review and
Causal Safety Framework.* Identified as a systematic review protocol, registered
retrospectively.

### 2. Registration
Not registered with PROSPERO: PROSPERO requires a direct health-related outcome, and this is
a review of *evaluation methodology*, not of a clinical intervention or diagnostic test in
patients. Registered on the Open Science Framework — DOI to be inserted on minting. No other
prospective register was used.

### 3. Authors
Dat Tat Mai (guarantor, corresponding), Thai Viet Pham, Thu Nguyen Thi Dang, James Jin Kang.
Affiliations and contact details in `01_registration_metadata.md`.

**Contributions.** D.T.M. conceived the review, wrote the protocol, built and ran the search
and screening pipeline, and drafted the manuscript. T.V.P. and T.N.T.D. contributed to
screening, extraction, and appraisal. J.J.K. supervised. All authors approved the final text.

### 4. Amendments
All deviations from the protocol as first written are recorded in
`07_amendments_and_deviations.md`. That log is part of the registration. **The manuscript's
present claim that no amendments were made is incorrect and is being corrected.**

### 5. Support
Sources of support, sponsor role, and competing interests to be stated in
`01_registration_metadata.md` §7 before submission.

---

## INTRODUCTION

### 6. Rationale
Deep-learning reconstruction now shortens brain MRI acquisition by factors of four to ten and
is entering routine clinical use. The learned prior that makes this possible can also
suppress genuine pathology or synthesise structure that was never measured. The metrics used
to certify these methods — PSNR, SSIM, NRMSE — are global, sign-symmetric, and dominated by
background voxels, so a reconstruction can score well while a small lesion has been erased.
No synthesis existed of how the field actually evaluates reconstruction safety, what failure
modes are documented, or which evaluation paradigms can detect prior-induced diagnostic
error. This review maps that evaluation landscape and identifies where it fails.

### 7. Objectives
Framed with PICOS, adapted because no clinical patient population is studied directly: the
"population" is the class of reconstruction methods under evaluation.

| Element | Specification |
|---|---|
| **P** | AI/ML-based brain MRI reconstruction methods — any architecture: accelerated/undersampled reconstruction, denoising, super-resolution, motion correction, generative and diffusion-based reconstruction |
| **I** | Any method used to evaluate reconstruction safety, reliability, or fidelity — pixel-wise metrics, perceptual/learned metrics, uncertainty estimation, observer/reader studies, causal or counterfactual analysis, automated or M-LLM observers |
| **C** | Any alternative evaluation approach, including radiologist ground-truth review, conventional fidelity metrics, other automated evaluators, or no comparator where a new metric is proposed |
| **O** | Ability to detect or quantify reconstruction safety failures — hallucinated or fabricated pathology, omitted true pathology, geometric/anatomical distortion, artifacts, robustness or distribution-shift failures |
| **S** | Primary methodological or technical studies, including diagnostic-accuracy and reader studies. Secondary syntheses are recorded as background only |

**Research questions**

- **RQ1** — How far, and under what acquisition conditions, do pixel-wise fidelity metrics
  diverge from radiologist diagnostic judgement?
- **RQ2** — What mechanisms explain that divergence?
- **RQ3** — Which evaluation paradigms can establish reconstruction safety before clinical
  deployment, and what do they leave unresolved?

---

## METHODS

### 8. Eligibility criteria
Given in full in `04_eligibility_criteria.md`. In summary: primary studies of human brain MRI
reconstruction reporting fidelity, artifact, robustness, or observer outcomes; English
language; no date limit; peer-reviewed journal or conference publications. Preprints,
animal-only and phantom-only studies, editorials, commentaries, and superseded conference
versions were excluded.

### 9. Information sources
Seven databases — PubMed/MEDLINE, SpringerLink, IEEE Xplore, Scopus, Semantic Scholar,
OpenAlex, Web of Science — all searched programmatically between 23 and 24 July 2026. Embase
was attempted but unavailable (no institutional entitlement); the ACM Digital Library offers
no search API. No citation chasing, grey-literature searching, or hand-searching was
performed; this bounds recall and is declared as a limitation.

### 10. Search strategy
Full strings for every database, with retrieval counts, are in
`03_search_strategy_PRISMA-S.md`. Three concepts combined with AND (brain MRI/neuroimaging;
AI/ML reconstruction; safety/fidelity/artifact), with `animal model`, `case report` and
`in vitro` excluded. The search was not peer reviewed against PRESS.

### 11. Study records

**11a. Data management.** Records were retrieved via database APIs and stored as one Markdown
file per record with structured front-matter (identifiers, title, abstract, MeSH terms,
venue, the query that retrieved it). Deduplication was multi-tier: DOI, then PMID, then
normalised title + year.

**11b. Selection process.** Two stages. Title/abstract screening applied the eligibility
criteria to all 26,924 deduplicated records, assigning each `include`, `exclude`, `flagged`,
or `background_only`. Full-text screening then applied the same PICOS criteria to every
retrieved full text. Screening was LLM-assisted under a fixed rubric with human review of
flagged records; the procedure and its limitations are set out in `04_eligibility_criteria.md`
§4. Records marked `background_only` are cited as context and are **not** counted among the
185 included studies.

**11c. Data collection process.** Extraction used the form in `05_data_extraction_form.md`.
Variables not stated in a source were recorded as *not reported* rather than inferred. Study
investigators were not contacted to supply missing data; authors were contacted only to
request full text that could not be retrieved.

### 12. Data items
Bibliographic identity; reconstruction method family; evaluation paradigm; reported failure
modes; magnetic field strength; pulse sequences; study design; reference standard; public
dataset or benchmark; code availability; sampling and centre; and per-study risk-of-bias
ratings. Definitions and coding rules in `05_data_extraction_form.md`.

### 13. Outcomes and prioritisation
The primary outcome is the **evaluation method's ability to detect reconstruction safety
failures**. Prioritised, in order: (i) observer/reader outcomes measuring diagnostic
acceptability or lesion detection; (ii) documented failure modes; (iii) agreement between
fidelity metrics and reader judgement; (iv) fidelity metric values alone. No pooled effect
measure was defined, because the corpus supports none.

### 14. Risk of bias in individual studies
Instrument matched to design: QUADAS-2 for diagnostic-accuracy and reader studies; a
reproducibility and robustness checklist for algorithmic studies, which QUADAS-2 does not
fit. Domains, decision rules, and the procedure actually followed are in
`06_risk_of_bias_plan.md`. **Note the unresolved provenance issue recorded there in §5.**

### 15. Data synthesis

**15a.** Narrative synthesis following SWiM within the PRISMA 2020 framework. Studies grouped
by research question, and within RQ1–RQ2 by method family and failure mode.

**15b–c. No meta-analysis was performed or planned.** Methods, datasets, acquisition settings
and outcome measures are not commensurable; no common effect measure exists. Every quantity
quoted in the synthesis is a value from a named individual study, never a pooled estimate.

**15d.** Prevalence counts derive from structured keyword classification of titles, abstracts
and MeSH terms and are reported as **lower bounds**, not exhaustive counts.

Because no pooled estimate is produced, subgroup analysis, meta-regression and sensitivity
analysis (PRISMA items 13e–f) have nothing to operate on and were not conducted.
Heterogeneity was examined structurally instead, along four axes: reconstruction paradigm,
field strength, acceleration factor, and pulse sequence.

### 16. Meta-bias(es)
No formal statistical assessment of reporting bias was performed: funnel plots and Egger's
test require a common effect measure and a quantitative synthesis, neither of which this
corpus supports. Reporting bias is treated narratively and judged **material and asymmetric** —
a literature rewarded for demonstrating improvement has weak incentive to publish erased
pathology or negative reader outcomes, which are precisely this review's subject. The true
prevalence of metric-invisible failure is therefore more likely under- than over-represented.

### 17. Confidence in cumulative evidence
Certainty was **not** graded by GRADE, CERQual, or any other formal system. This is declared
as a limitation. Corpus-level quality indicators and domain-wise risk of bias are reported
instead.

---

## Outcome of the review as executed

Recorded here for transparency; these are results, not plan.

| Stage | Count |
|---|---|
| Records identified | 27,327 |
| Duplicates removed | 403 |
| Unique records screened | 26,924 |
| Excluded at title/abstract | 25,573 |
| Full text sought | 1,149 (109 include + 1,040 flagged) |
| Full text retrieved | 562 |
| Not retrievable | 654 |
| Excluded at full text | 363 |
| Background only | 14 |
| **Studies included** | **185** (1995–2026) |

Full flow and per-stage exclusion reasons in `../PRISMA_flow_report.md`; PRISMA 2020 checklist
in `../LaTex PDF/PRISMA_2020_checklist_supplement.md`.
