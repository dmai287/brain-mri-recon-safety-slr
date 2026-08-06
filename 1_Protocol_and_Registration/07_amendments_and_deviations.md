# Amendments and deviations from the protocol

**This log is part of the registration.** It exists because the manuscript currently claims no
amendments were made, and that claim is not accurate.

Baseline: `../protocol.json` and `../search_strategy.json`, both fixed 2026-07-23, before
screening began 2026-07-27.

---

## 1. Registration status

| | |
|---|---|
| Prospectively registered in a public registry? | **No** |
| Protocol fixed before screening? | Yes — 2026-07-23, four days before screening |
| Independently timestamped? | **No.** Neither protocol file is tracked in version control; only filesystem mtime exists, which is mutable and not acceptable as evidence |
| PROSPERO? | Not eligible — no direct clinical health outcome |
| OSF registration | Retrospective, created 2026-08 after the review was complete |

The four-day gap between protocol and screening is real, but it cannot be *proved* from the
repository as currently constituted. It is therefore asserted as a statement of fact by the
authors, not offered as verifiable pre-registration.

**Remedy going forward:** commit `protocol.json` and `search_strategy.json` to git so that all
future timestamps are independently verifiable.

---

## 2. Substantive deviations

### D1 — LLM-as-Judge dropped from the required search concept
**Status:** decided before screening · **Impact: high — changed what the search retrieved**

The protocol's research question and inclusion criterion 3 centre on M-LLM-as-Judge evaluation
(with causal discovery and counterfactual diffusion simulation). The executed search does
**not** require that concept: `search_strategy.json` has three required AND-groups (brain MRI;
AI/ML reconstruction; safety/fidelity), and `protocol.json` marks the *LLM-as-Judge /
Automated Evaluation Methodology* concept `required: false`.

Recorded in `protocol.json` → `reviewer_clarifications`: *"Broaden search → drop LLM-as-Judge
concept from the required AND to widen recall."*

*Rationale.* Requiring the LLM-as-Judge term would have restricted the corpus to a small and
immature literature and defeated the aim of surveying the evaluation landscape. Widening
recall was the right call.

*Consequence.* The review as executed answers a **broader** question than the protocol's
stated research question. The manuscript's title and research questions reflect the broader
scope, so the reported work is internally consistent — but the protocol's research question
and inclusion criterion 3 were superseded and should be read as amended. Notably, **no
included study evaluated M-LLMs as automated safety observers**, which is itself a finding and
is reported as such.

### D2 — Preprints excluded, having been admitted in the protocol
**Status:** decided before screening · **Impact: moderate**

Protocol inclusion criterion 4 admitted "reputable preprint (arXiv/medRxiv)". Preprints were
instead excluded a priori and removed before deduplication (0 retained; see
`../Excluded - Preprints/`).

*Rationale.* Restricting to peer-reviewed sources raises the evidence floor for a review whose
subject is safety claims.

*Consequence.* Reduced recall of very recent work, in a fast-moving field where preprints
carry real signal. Declared as a limitation.

### D3 — Journal/venue whitelist applied, then not used to restrict screening
**Status:** during review · **Impact: none on results, but must be disclosed**

A "representative venues" filter was applied to the deduplicated pool, matching 11,075 of
26,924 records and setting aside 15,849 as non-representative. It is **not** in the protocol.

**Title/abstract screening was subsequently run on the full 26,924-record pool, not the
11,075 subset**, so the filter did not restrict the evidence base and no study was excluded by
venue. It is recorded in `prisma_log.json` under `venue_filter` and appears in the PRISMA flow
report; it must not be read as an eligibility criterion.

*Consequence.* None for the included set. Disclosed because an unexplained filter in the flow
diagram invites the inference that venue restricted eligibility.

### D4 — Screening and appraisal procedure differs from the two-independent-reviewers norm
**Status:** during review · **Impact: high — affects how the methods may be described**

The protocol did not specify how many human reviewers would screen independently. In practice:

- Title/abstract screening (26,924) was LLM-assisted against a fixed rubric, with undecidable
  records flagged and carried forward rather than excluded.
- Full-text screening (562) used the same criteria; 66 flagged records were re-adjudicated by
  a higher-capability model.
- All 185 `include` decisions were verified against full text by the authors; exclusions were
  not all independently re-checked by a second human.
- Risk-of-bias ratings are currently **`pending_reviewer_verification`** — see
  `06_risk_of_bias_plan.md` §5.

*Consequence.* No inter-rater reliability statistic can be computed, because there were not
two independent human passes over the same records. Any κ or screening-sensitivity value in
the manuscript lacking a stated estimator, subset, and gold standard should be removed.

---

## 3. Corrections to reported results identified during preparation

Found while assembling the per-study release files; full detail in
`../LaTex PDF/DISCREPANCY_REPORT_v6.md`.

| # | Item | Manuscript | Data |
|---|---|---|---|
| C1 | QUADAS-2, all four domains | 26/7/3, 29/5/2, 31/4/1, 32/3/1 | 7/17/12, 17/12/7, 19/10/7, 26/7/3 |
| C2 | Applicability concerns | ">85% Low" across domains | 61.1% / 66.7% / 63.9% Low |
| C3 | Publication period split | 2020–22 n=78; 2023–26 n=82 | n=38; n=122 |
| C4 | Studies reporting fidelity metrics | "123 studies" (×3 in body) | 45 (the manuscript's own Table VI figure) |
| C5 | Full text obtained | "185/185 (100%)" | 142 full, 19 partial, 24 abstract-only |
| C6 | Reader subset | n=36 | 6 of the 36 have no human readers |
| C7 | Data integrity | — | One wrong-PDF record (S004) found and quarantined |

C1–C6 are reporting errors in the draft, not errors in the underlying review. Corrected
Table VII: `../LaTex PDF/table7_corrected.tex`.

---

## 4. Replacement wording for the manuscript

The passage at `brain_ieeetmi_v6.tex` **L334–338** should be replaced. Suggested text:

> The protocol — scope, research questions, PICOS eligibility criteria, search vocabulary, and
> the rules for selection, appraisal, and synthesis — was fixed in the project repository
> (`protocol.json`, `search_strategy.json`) on 23 July 2026, before screening began on 27 July
> 2026. We did not register with PROSPERO, which excludes reviews without direct clinical
> health outcomes. The review is registered retrospectively on the Open Science Framework
> (DOI: 10.17605/OSF.IO/XXXXX), after completion; that registration is made to place the
> protocol, search strategy, per-study data, and deviation log on the public record, and we do
> not present it as prospective registration. Four deviations from the protocol as first
> written are documented in the registered amendments log: the LLM-as-Judge concept was
> dropped from the required search terms to widen recall; preprints were excluded rather than
> admitted; a venue filter was computed but not used to restrict screening; and screening and
> appraisal were LLM-assisted with human verification rather than dual independent human
> review.

Replace `XXXXX` with the real DOI once minted.

Also amend, in the same pass:
- **L753** — the QUADAS-2 sentence, per `06_risk_of_bias_plan.md` §5 and §6.
- **L842** — repeats the superseded 29/36, 31/36, 32/36 figures.
- **L1322** — cites `protocol.md`, which does not exist; the files are `protocol.json` and
  `search_strategy.json`.
