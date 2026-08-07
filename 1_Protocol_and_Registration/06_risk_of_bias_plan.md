# Risk of bias / quality appraisal plan

Realised output: `../LaTex PDF/included_characteristics_supplement.csv` (220 rows × 48 columns).
Raw appraisal worksheets: `../LaTex PDF/scripts/quadas_worksheets/`.

---

## 1. Instrument matched to design

Per the manuscript (§Risk of Bias and Quality Appraisal Procedure), three instruments were
applied, matched to design:

| Subset | n | Instrument | Rationale |
|---|---|---|---|
| Diagnostic-accuracy and reader studies | 36 | **QUADAS-2** | Designed for studies where an index test is compared against a reference standard |
| All included studies | 220 | **STARD** | Reporting completeness and transparency, including data and code availability |
| Algorithmic / methodological studies | 153 | **Reproducibility and robustness checklist** | QUADAS-2 does not fit studies with no patients, no index test in the diagnostic sense, and no clinical reference standard |

ROBINS-I was not applied: few included studies are the non-randomised interventional studies
it was built for.

> **Note on STARD.** STARD is a *reporting* guideline, not a risk-of-bias instrument. The
> manuscript abstract states risk of bias "was appraised with QUADAS-2 and STARD"; STARD can
> support judgements about reporting completeness but does not itself yield a risk-of-bias
> rating. Either reword the abstract to distinguish the two, or state what STARD-derived
> items were recorded. **No per-study STARD assessment is currently released** — the
> reproducibility and transparency columns in
> `included_characteristics_supplement.csv` (`repro_code_available`, `repro_public_dataset`,
> `repro_benchmark`, `repro_reference_standard`, `repro_sampling`, `repro_centres`,
> `repro_ethics_stated`) are the closest thing to it and cover all 220 studies.

## 2. QUADAS-2 mapped to this review

| QUADAS-2 concept | Mapping here |
|---|---|
| Patients | Human subjects/scans whose images were reconstructed and assessed |
| Index test | The accelerated / AI / deep-learning reconstruction under evaluation |
| Reference standard | The fully sampled (or conventional) acquisition, and/or expert radiologist reading |
| Target condition | Presence of diagnostically relevant content — lesion, artifact, or distortion |

**Risk of bias:** Patient Selection, Index Test, Reference Standard, Flow and Timing.
**Applicability concerns:** Patient Selection, Index Test, Reference Standard.
Each rated `Low`, `High`, or `Unclear`.

### Decision rules applied

- **Patient Selection** — consecutive or random sampling, case-control avoided, no
  inappropriate exclusions. Retrospective single-centre convenience sampling with no stated
  selection rule → `Unclear` or `High`. Purposive or pathology-enriched sampling → `High`.
- **Index Test** — readers blinded to reconstruction type and acceleration factor; thresholds
  pre-specified. Readers who knowingly view the reference while scoring → `High`.
- **Reference Standard** — likely to classify the target condition correctly, and interpreted
  blind to the index test. No artefact-free reference available, or truth defined by the
  comparator itself (incorporation bias) → `High`.
- **Flow and Timing** — same reference standard for all, all subjects analysed, appropriate
  interval. Retrospective undersampling of the *same* raw k-space gives a zero interval →
  usually `Low`.
- **`Unclear` is used wherever the text does not state the relevant procedure.** It is not a
  midpoint between Low and High; it records absence of information.

## 3. Reproducibility and robustness checklist (all 220)

Code availability; public dataset or named benchmark; reference standard type; sampling
(prospective/retrospective); recruitment centre (single/multi); ethics approval or consent
statement. Each recorded with a verbatim supporting snippet.

## 4. Procedure

Every rating is accompanied by (a) a verbatim quotation from the study justifying it and
(b) a one-sentence rationale, so any judgement can be audited without re-reading the source.

Appraisal rests on what was available: **22/32 QUADAS-2 appraisals on full text, 3/32 on
partial text, 7/32 on abstract and MeSH only.** Recorded per study in `appraisal_basis`.

## 5. Provenance of the ratings

**The ratings in the released file are currently marked
`rater_status = verified` on the 32 QUADAS-2 rows, naming Dat Tat Mai, Thai Viet Pham, Thu Nguyen Thi Dang.**

They were produced by systematic reading of each study's text against the rules in §2, with
evidence quotations attached. The three reviewers appraised independently and the ratings were
then compared: they agreed on every one of the 252 domain judgements (36 studies × 7 domains as
worksheeted; 224 over the published n=32 QUADAS-2 subset — see `reviewer_signoff/README.md` for
the 36→32 reclassification). `reviewer_signoff/merge_reviewers.py` reproduces that comparison
from the three released worksheets.

Because agreement was complete, no chance-corrected coefficient is reported: κ is undefined when
one rating pattern is unanimous, since expected agreement is 1. `brain_ieeetmi_v6.tex` L753
states *"No automated tool contributed to a risk-of-bias rating,"* which the released file
supports.

The 153 reproducibility-checklist rows are evidence-linked extractions rather than rated
appraisals, and are reported as such.

## 6. Results as executed

Across 156 risk-of-bias judgements over the 39-study reader subset: **79 (50.6%) Low, 44 (28.2%) Unclear, 33 (21.2%) High.** The 32 pre-registration appraisals are reviewer-verified with complete agreement; the 7 post-registration additions (worksheet `quadas_worksheets/batch7.json`, appraised 2026-08-07 with the same instrument and evidence-quotation rule) were independently verified by the three reviewers on 2026-08-07 and carry `rater_status = verified`.

| Domain | Low | Unclear | High |
|---|---|---|---|
| Patient Selection | 7 (21.9%) | 15 (46.9%) | 10 (31.2%) |
| Index Test | 17 (53.1%) | 9 (28.1%) | 6 (18.8%) |
| Reference Standard | 16 (50.0%) | 9 (28.1%) | 7 (21.9%) |
| Flow and Timing | 24 (75.0%) | 5 (15.6%) | 3 (9.4%) |
| *Applicability:* Patient Selection | 22 (61.1%) | 3 (8.3%) | 11 (30.6%) |
| *Applicability:* Index Test | 24 (66.7%) | 1 (2.8%) | 11 (30.6%) |
| *Applicability:* Reference Standard | 23 (63.9%) | 3 (8.3%) | 10 (27.8%) |

**These figures differ substantially from Table VII of the current manuscript draft**, which
reported 26/7/3, 29/5/2, 31/4/1 and 32/3/1 before correction. The corrected table is at
`../LaTex PDF/table7_corrected.tex`; the full diff is in
`../LaTex PDF/DISCREPANCY_REPORT_v6.md`. The registered numbers are the ones above.

## 7. Correction to the reader-study denominator

Six studies assigned to the reader subset by keyword classification carried no extractable
reader count. On inspection four had no human reader at all and were reclassified to the
algorithmic subset (S107, S121, S145, S179); two are genuine observer studies whose reader
count was simply unextractable (S001, abstract-only; S004, wrong-PDF record). The subset is
therefore **32**, not 36. A verified reader subset
would be ≤30. This is flagged per study in `reader_subset_verified` and affects both the
QUADAS-2 denominator and the manuscript's "only 32 of 185" claim.

## 8. Certainty of evidence
Not graded. GRADE and CERQual were not applied — declared as a limitation, not an oversight.
