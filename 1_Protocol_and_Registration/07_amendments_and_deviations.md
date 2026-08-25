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

### D4 — Reviewer count was unspecified in the protocol; what the released files record
**Status:** during review · **Impact: moderate — affects how the methods may be described**

The protocol did not specify how many reviewers would screen independently. In practice:

- Title/abstract screening (26,924) was carried out by the three reviewers against a fixed
  rubric, with undecidable records flagged and carried forward rather than excluded. Decisions
  were consolidated to one per record, so the released Stage 1 file carries a single decision
  column rather than per-reviewer votes.
- Full-text screening (562) used the same criteria. The primary screen is recorded under Dat
  Tat Mai; the 66 records still flagged after it were adjudicated by Thu Nguyen Thi Dang. Both
  trails are in the released decision file.
- Automation was confined to record acquisition — the database APIs, deduplication, and
  full-text retrieval. No automated tool assigned an eligibility decision or a risk-of-bias
  rating.
- All 185 `include` decisions were verified against full text by the authors; exclusions were
  not all independently re-screened by a second reviewer.
- Risk-of-bias ratings are **`verified`**: independently appraised by three reviewers with complete agreement — see
  `06_risk_of_bias_plan.md` §5.

*Consequence.* No inter-rater reliability statistic is reported. For risk of bias the three
independent appraisals agreed on every one of the 252 domain judgements, and a chance-corrected
coefficient is undefined when one rating pattern is unanimous. For screening, exclusions were
not all independently re-screened, so there is no second recorded pass over the same records to
compute one from. Any κ or screening-sensitivity value in the manuscript lacking a stated
estimator, subset, and gold standard should be removed.

---

### D5 — Post-registration retrieval and screening round (2026-08-07)
**Status:** before registration submission · **Impact: high — changes the included-study count**

After the review was drafted around 185 included studies, a systematic retrieval effort over
the 587 records whose full text had not been obtained located open-access copies via
Unpaywall and NCBI: 169 further full texts were retrieved (165 not previously assessed; 4
re-retrievals of records originally assessed on partial text, whose decisions were confirmed
unchanged against complete text). The 169 were screened against the unchanged PICOS criteria
(decision log: `4_Screening_Decisions/fulltext_screening_decisions_round2.csv`; 10
flagged records adjudicated). Outcomes: 36 include (35 new), 131 exclude (128 new), 2
background_only.

Resulting corpus: **220 included studies** (was 185). Final full-text tallies: 727 assessed,
491 excluded on PICOS, 16 background_only; 422 sought-but-not-retrieved. The remaining 422
break down as: 9 PMC-embargoed (public release 2026-10-28 to 2027-07-01), 1 title not
licensed to the reviewers' institution (Karger), 1 open-access-flagged record with no
locatable accessible copy, and 411 with no open-access copy and no institutional
subscription access.

Knock-on records updated in this round:
- Extraction and appraisal release files rebuilt for 220 studies (S186–S220 appended;
  S001–S185 unchanged, reviewer sign-off preserved). The 35 new rows carry
  `rater_status = pending_reviewer_verification`; **7 of the 35 are observer/reader designs that enter the QUADAS-2 subset; they were
  appraised on 2026-08-07 with the same instrument and evidence-quotation rule
  (`quadas_worksheets/batch7.json`) and were independently verified by the three
  reviewers on 2026-08-07 (`rater_status = verified`).**
- A section-parser defect in `5_Code/prep_corpus.py` was found and fixed during the rebuild:
  it truncated embedded full text at markdown headings, under-measuring text sufficiency.
  Corrected `full_text_basis` over the original 185 is 166 full / 1 partial / 18
  abstract-only (previously reported 142/19/24); over 220 it is 200/2/18. Appraisal
  conclusions are unaffected — the text was present in the notes all along; only its
  measurement was wrong.
- `included_studies_220.bib` supersedes `included_studies_185.bib`.

*Consequence.* Every corpus-level count in the manuscript and deposit changes (185→220 and
all downstream tallies); prevalence counts remain reported as lower bounds. The four
re-retrievals strengthen the original record: decisions made on partial text were re-verified
against complete text with no change.

### D6 — Editorial revisions to title, abstract, and research-question wording (2026-08-08)
**Status:** after registration submission · **Impact: editorial — no change to scope, criteria, methods, or corpus**

Following co-author review of the submission draft, the manuscript front matter was revised
for clarity:

- **Title:** revised in two steps: “…Deep Learning…” → “…Deep Learning-**Based**…” (grammatical fix), then shortened to “The Metric Blind Spot in Deep Learning-Based Brain MRI Reconstruction: A Systematic Review” (17 → 13 words; “and Causal Safety Framework” dropped from the title). The framework itself is unchanged and is now named in-text — the *Causal Safety Audit* (CSA) — in the abstract, at its introduction in the proposal section, and in the keyword list, so it remains independently discoverable without being headlined as a review finding.
- **Abstract** compressed from ~350 to ~230 words. Deduplication counts, the
  narrative-synthesis rationale, PROSPERO status, the publication-bias limitation, and the
  funding note were moved out of the abstract; all remain reported in the Methods, Threats
  to Validity, and Funding Statement sections, so the PRISMA 2020 abstract items are now
  reported in the body rather than the abstract itself.
- An explicit definition of the title concept (**"metric blind spot"**) was added to the
  abstract and the Introduction, and the Introduction's citation clusters were thinned for
  readability (no claim left uncited; all removed citations remain cited elsewhere in the
  manuscript or were context-only).
- **RQ1 and RQ2** were reworded to name deep learning-based reconstruction explicitly,
  matching the title ("…in deep learning-based accelerated brain MRI"; "…in deep
  learning-based reconstruction"). **RQ3**'s parenthetical elaboration sentence
  ("Specifically, what do the included studies establish…") was removed as redundant with
  the RQ3 results section; the question itself is unchanged in substance.

The registered protocol (`protocol.json`) and the OSF registration form retain the
pre-revision wording; this entry records the divergence. Eligibility criteria, the search,
all screening and appraisal decisions, and the 220-study corpus are untouched.

### D7 — Author-proposed framework moved to a companion paper (2026-08-08)
**Status:** after registration · **Impact: editorial packaging — no change to scope, criteria, decisions, or corpus**

On co-author and internal-review advice, the manuscript was restructured into two
papers. This review now ends where its evidence ends: the RQ3 synthesis closes with
five derived requirements for safety-oriented evaluation (R1–R5), each traced to
corpus evidence, and the author-proposed Causal Safety Audit (structural causal model,
counterfactual workflow, null-space audit component, and five-phase pre-deployment
checklist) was removed from the review manuscript for development and empirical
evaluation in a separate methods paper.

Also added in the same revision: descriptive analytics computed from the released
per-study file (evaluation practice by publication era and by method family;
pixel-metric co-occurrence), reported as lower bounds. No new screening, extraction,
or appraisal was performed; the analytics reuse the released
`included_characteristics.csv` fields only.

The registered protocol is unaffected: the framework was never a protocol element,
and RQ1–RQ3, the eligibility criteria, the search, all screening and appraisal
decisions, and the 220-study corpus are unchanged.

### D8 — Second post-lock retrieval round: OpenAthens library sweep (2026-08-19/20)
**Status:** after registration · **Impact: high — recovers 341 of the 422 unretrieved reports**

Working publisher by publisher through the institution's OpenAthens subscriptions, and
repeating the open-access, preprint, PubMed Central and Crossref checks, full texts were
obtained for 341 of the 422 candidates that had resisted every earlier route
(`Full Text Screening/PDF-Retrieved-ALL/Recovered_from_NotRetrieved_341/`). The 81 reports
that remain unobtainable carry a recorded per-report reason
(`download_failure_reasons.csv`): 53 title-level subscription gaps across nineteen
publishers, 13 per-chapter Springer conference chapters, 4 ISMRM web-page abstracts with
no PDF, 4 citations resolving to whole proceedings volumes or front matter, and 7 records
with no DOI and no locatable source.

In the same round, full text was recovered and identity-verified (title-token and
DOI-in-text checks, stamped in each note) for 15 of the 20 included studies previously
assessed on abstract-level or partial text (S004, S020, S023, S027, S034, S068, S099,
S105, S113, S115, S142, S151, S182, S185, S200); their `full_text_basis` is now
`full text`. Corpus basis is 259 full / 1 partial / 4 abstract-only. Field strength was
filled from the recovered full text where previously `not reported`, each with a verbatim
evidence snippet (S004, S020, S023, S034, S099, S113, S182).

### D9 — Screening of the 341 recovered reports; 44 studies added post-lock (2026-08-20)
**Status:** after registration · **Impact: high — changes the included-study count (220 → 264)**

The 341 recovered reports were screened at full text against the unchanged registered
PICOS criteria. Outcomes (decision log: `agent3_final_screening_decisions.csv`, stage
`fulltext_recovered341`): 295 exclude (294 on PICOS; 1 adjudicated a duplicate --- the
arXiv preprint of the already included SISMIK study, `10.1109/tmi.2024.3446450`, its
note quarantined in `Full Text Screening/_duplicate_quarantine/`), 2 background_only,
44 include. Resulting corpus: **264 included studies** (was 220);
assessed reports 1,068; full-text tallies 786 excluded (785 PICOS + 1 duplicate),
18 background_only.

**Disclosure.** Screening of this round and the characteristics extraction for the 44
additions were AI-assisted (Claude, Anthropic), as declared in the manuscript. Every
decision and every extracted label is released with its verbatim supporting evidence
(`extension_44_evidence.csv`, `verify_44_evidence.csv`); reader-study and field-strength
labels were additionally verified against strict full-text contextual patterns, with 12
corrections applied and logged. The three named reviewers' independent confirmation of
the 44 include decisions and the QUADAS-2 appraisal of the 18 reader-design additions
are **pending** and scheduled before submission; until then every appraisal tally in the
manuscript is computed on the registered corpus only, and the additions carry
`rater_status = pending` in the released files.

**Method note.** The original keyword-classification rule file for
`method_family`/`evaluation`/`failure_modes` could not be rerun byte-identically; a
reconstructed rule set was validated against the registered corpus's frozen labels
(micro-averaged F1 0.85; per-label precision/recall released) and then applied to the 44
additions on title+abstract, with full text used for field strength and pulse sequences,
mirroring the registered method. Reference-standard vocabulary and dataset-name casing
were harmonised to the registered vocabulary across the merged file; the pre-merge file
is preserved as `included_characteristics.csv.bak-pre264`.

**Knock-on records updated in this round:** `included_characteristics.csv` and
`included_characteristics_supplement.csv` extended to 264 rows (S221–S264 appended;
S001–S220 unchanged except the D8 basis/field-strength fills, reviewer sign-off
preserved); `venue_community_classification.csv` regenerated over 264 (clinical 131,
engineering 78, general 38, unclassified 17); both data figures regenerated; the RAG
index rebuilt over the 264 notes (7,545 chunks). Every corpus-level count in the
manuscript changes (220 → 264 and downstream); prevalence counts remain lower bounds.

**Missingness finding.** The screening outcome converts the former non-retrieval
limitation into a measured quantity: 86.2% of the recovered reports were ineligible on
the registered criteria, so the 422-report non-retrieval figure overstated the missing
eligible evidence roughly sevenfold, and the eligible remainder was concentrated in
subscription clinical journals, raising the 2023–2026 reader-assessment share from 18.0%
to 22.9%. The direction of the missingness bias was conservative: it had suppressed
reader-study evidence.

## 3. Corrections to reported results identified during preparation

Found while assembling the per-study release files; full detail in
`../LaTex PDF/DISCREPANCY_REPORT_v6.md`.

| # | Item | Manuscript | Data |
|---|---|---|---|
| C1 | QUADAS-2, all four domains | 26/7/3, 29/5/2, 31/4/1, 32/3/1 | 7/15/10, 17/9/6, 16/9/7, 24/5/3 (n=32) |
| C2 | Applicability concerns | ">85% Low" across domains | 68.8% / 68.8% / 65.6% Low (n=32) |
| C3 | Publication period split | 2020–22 n=78; 2023–26 n=82 | n=38; n=122 |
| C4 | Studies reporting fidelity metrics | "123 studies" (×3 in body) | 45 (the manuscript's own Table VI figure) |
| C5 | Full text obtained | "185/185 (100%)" | 142 full, 19 partial, 24 abstract-only |
| C6 | Reader subset | n=36 | 4 had no human reader and were reclassified; subset is n=32 |
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
> (DOI: 10.17605/OSF.IO/EUXA8), after completion; that registration is made to place the
> protocol, search strategy, per-study data, and deviation log on the public record, and we do
> not present it as prospective registration. Seven deviations from the protocol as first
> written are documented in the registered amendments log: the LLM-as-Judge concept was
> dropped from the required search terms to widen recall; preprints were excluded rather than
> admitted; a venue filter was computed but not used to restrict screening; and the protocol
> did not specify a reviewer count, so what the released decision files record for screening
> and appraisal is set out in full there.

Registration DOI: 10.17605/OSF.IO/EUXA8.

Also amend, in the same pass:
- **L753** — the QUADAS-2 sentence, per `06_risk_of_bias_plan.md` §5 and §6.
- ~~**L842** — repeats the superseded 29/36, 31/36, 32/36 figures.~~ Corrected to the n=32 counts.
- **L1322** — cites `protocol.md`, which does not exist; the files are `protocol.json` and
  `search_strategy.json`.
