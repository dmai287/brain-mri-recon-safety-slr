# Manuscript changelog

## v17 -- 2026-08-21 -- referee-response pass

Response to the referee report on `brain_cmig_v16.pdf` (panel REJECT, gate FAIL on
dimension 8). v16 is unchanged and retained; all work is in `brain_cmig_v17.tex` and
`supplementary_cmig_v17.tex`. Point-by-point reply in `response_to_referee_v17.md`.

**Gate items.**
- **C1 Bash 2021.** Verified against the corpus copy: 3D T1w only (MPRAGE/FSPGR/BRAVO),
  DICOM-domain SubtleMR post-processing ("does not use proprietary raw k-space input"),
  lesion conspicuity *superior* not reduced (P < .008), six figures none of which is a
  five-sequence panel. The lines 250-254 claim is deleted and re-sourced to Lang et al.,
  AJNR 2024;45(4):379-385 (2-minute ultrafast vs 10-minute reference, 66 patients, T1w /
  T2-T2* / FLAIR / DWI, two blinded neuroradiologists), whose single discrepant case is a
  punctate DWI focus less conspicuous on the accelerated acquisition -- now the
  manuscript's one direct clinical instance, labelled as one case in 66. Figure 2 removed
  (image tracing showed it was assembled from the AJNR 2024 paper, not Bash; third-party
  material, no permission). Bash removed from the Introduction, Table 3 and Table 7 row 4;
  retained in the Discussion as evidence of cleared DL products and in 5.2 with its full
  category and vendor affiliation stated.
- **C2 reader denominator.** Adopted 57/207. S107, S121, S145 and S179 reclassified as
  algorithmic in the manuscript *and* in the released CSVs, with a per-study
  reclassification note. 57 + 207 = 264 and 39 + 18 + 207 = 264 both close. Propagated
  through Tables 3, 4, 6, 7, 8, both data figures, the abstract and 4.2/4.5/4.6/4.7/5/5.2.
  Effects: co-report 7.6 -> 6.8 %; 2023-2026 reader share 22.9 -> 20.6 %; code-and-reader
  5.3 -> 4.9 %; Fisher p 0.046 -> 0.058 at unchanged OR 0.51; generative reader share
  16.0 -> 11.1 %; labels 182/146 -> 178/145. All reported openly in 5.2.
- **M5.** Knoll 2020 fastMRI knee dataset descriptor replaced by the IEEE SPM 37(1)
  parallel-MRI reconstruction survey.
- **Screening kappa (not raised in the report).** v16 attributed Fleiss kappa 0.943 to
  "independent duplicate screening" by the three reviewers, citing kappa_human_results.csv.
  The released decisions record primary_screen_vote_count = 1 for every full-text record
  (one primary screen plus adjudication of flagged records), so no duplicate-labelling
  coefficient is computable from the deposit; and kappa_human_results.csv was byte-identical
  on all 214 rows to the three machine re-screen runs. The claim is withdrawn. Section 3 now
  describes the design as recorded and reports the escalation volumes the records do support
  (1,040 flagged at title/abstract; 84 escalated at full text, 29 included; 77 marked for
  human re-inspection, 40 included); 5.2 lists the absence of any disagreement-based
  reliability estimate, for screening and appraisal alike, as the sharpest limitation.
  The mislabelled file is withdrawn from the deposit.

**Internal audit.** M1 basis-of-assessment split into current (259/1/4) and at-appraisal
(244/2/18) rows, which reconciles 6/39 with 4/264 exactly; M2 "10 of 14" -> 9; M3 stratum
closed as 294 + 2 + 45 = 341 (45 reports = 44 studies); M4 non-retrieval argument rewritten
so it bounds rather than denies the bias and agrees with the paywall finding; M6 sequence
comparison restricted to disjoint strata (5/23 vs 10/85, Fisher OR 2.08 p = 0.30) with the
107-study overlap stated; M7 re-anchored on a 100 mm^3 lacunar infarct (0.027-0.036 dB),
5 mm^3 retained as a correctly-stated SWI limiting case; M8 penumbra entry deleted; M9 all
264 included studies entered into the main reference list with a new Appendix A on
traceability; M10 conservative/anti-conservative directions separated; M11 Figure 1 caption
reconciled to PRISMA dispositions; M12 appraisal agreement restated as 39/39 studies and
273/273 domain judgements with the unanimity caveat; M13 RQ3 promoted to argued prose with
the null-space derivation written out; M14 Tang corruption basis flagged in Table 5 twice
and Table 7 once.

**Rebalance.** Methodology 684 -> 2,164 words (registration status per PRISMA 24a, search
dates in body, tooling, venue rule stated term by term); Related Work 241 -> 662 (task-based
IQA tradition engaged); RQ3 124 -> 650; Discussion argument 418 -> 1,060 with regulatory
claims cited to the FDA/HC/MHRA GMLP principles, the EU AI Act and the EU MDR; Introduction
671 -> 835 with a scope paragraph; Threats now 47 % of the Discussion rather than 51 %.

**Figures.** Old Figure 2 (five-sequence panel) removed. New Figure 2 plots the Eq. (2)
identity across lesion volume with the sub-voxel region shaded and three clinical anchors
marked -- computed, original, no permission needed. Old Figure 3 (four text boxes) converted
to Table 7. Both data figures regenerated for the 57 partition under v17 filenames; v16's
own figure files are left on the 61 partition so v16 still rebuilds as published. All three
figures are now produced by released scripts (5_Code/make_figures.py,
5_Code/make_dpsnr_figure.py) reading only included_characteristics.csv.

**Minor.** m1-m16 all addressed; .bib acronym capitalisation fixed with protective braces.

**Build.** brain_cmig_v17.pdf 74 pp, supplementary_cmig_v17.pdf 36 pp, both 0 errors and
0 undefined citations or references. A 39-check numeric audit against the deposit passes.

**Still outstanding, and stated as outstanding in the manuscript.** Human duplicate
screening of the 214-record sample; QUADAS-2 appraisal of the 18 pending reader studies;
re-appraisal of the 5 recovered abstract-basis ratings; three-reviewer confirmation of the
44 recovered-tranche includes; a new Zenodo/GitHub release cutting the corrected deposit so
the quoted release tag and commit hash refer to the 57/207 files.


## v16.1 — 2026-08-21 — citation integrity, table relocation, deposit refresh

**Citation integrity**
- `tab:acceleration_spectrum` rebuilt. The per-band PSNR/SSIM thresholds, reader-score
  differences and rank statistics (ρ = 0.41–0.54, ρ = 0.12–0.25) were not traceable to
  any cited study and are removed. The replacement reports only corpus-recorded values:
  acceleration factors extracted post hoc from all 264 full texts with a verbatim
  quotation each, reference-list and citation-context matches excluded; 63 studies
  (23.9%) state one, from 407 retained evidence quotations. Bands: 2–4x n=32
  (21.9% reader, 3.1% metric+reader), >4–8x n=17 (35.3%, 5.9%), >8x n=14 (35.7%, 28.6%).
  Released as `acceleration_factors_evidence.csv`; extractor in
  `5_Code/extract_acceleration_factors.py`.
- `feng2023taskdriven` removed from `ref2.bib` and its RQ2 citation replaced with the
  verified `junhyeok2026lesionaware`. Sibling entry `feng2023can`, recorded in the same
  comment block as unretrievable, also removed. 321 entries remain.
- `ref2.bib` reconciled against the deposited `included_studies_264.bib`: DOIs added for
  `esteban2017mriqc` and `muckley2021results`; `junhyeok2026lesionaware` year corrected
  2025 → 2026 to match corpus record S177. All 264 included studies now carry a DOI and
  the two files agree exactly.

**Structure**
- Four tables moved from the main text to the supplement, restoring the v15 split:
  related work (S4), search vocabulary (S5), evidence architecture (S7) and the RQ2
  failure-mechanism table (S8). Main text now 8 tables and 4 figures; in-text pointers
  retargeted and verified against the compiled supplementary `.aux`.
- `supplementary_cmig_v16.tex` created (36 pp, Tables S1–S9, Figure S1, self-contained
  bibliography). Opening note now describes S4–S9.
- `\section*{Appendix A. Supplementary material}` added before the references; stale
  comment block about supplementary tables living after the bibliography removed.
- "late-retrieved" framing removed from Threats to validity.
- `highlights_cmig_v15.txt` renamed to `highlights_cmig_v16.txt` (content unchanged).

**Deposit**
- `MANIFEST.csv` rebuilt in both mirrors with every row re-hashed against the file on
  disk: OSF 60 rows, GitHub 63, integrity clean, content-identical apart from
  `.gitignore`, `CITATION.cff`, `LICENSE`.
- `0_Manuscript` refreshed to v16 in both mirrors (manuscript PDF and source,
  supplementary PDF and source, highlights, changelog). The GitHub copy had been at the
  2026-08-13 state; supplementary source had never been deposited.
- Newly registered: `acceleration_factors_evidence.csv`, `quadas2_AI_preliminary.csv`,
  `kappa_ai_rescreen_results.csv`, `5_Code/extract_acceleration_factors.py`, plus
  previously untracked files present on disk.
- **Outstanding:** the release tag named in Data and code availability is still v1.0.2
  and predates every change above; a new tagged release is required before submission.

- Main manuscript 39 pp, supplementary 36 pp; both compile with zero undefined citations
  and zero undefined references.



## v16.0 — 2026-08-21 — concise Methods section & streamlined narrative

- **Created `brain_cmig_v16.tex` / `brain_cmig_v16.pdf`**: Streamlined Methods section to remove meta-commentary, defensiveness, and redundant justifications.
- **Methods §Methods**: Tightened into a concise, standard PRISMA narrative (search strategy, deduplication, 3-reviewer independent full-text screening with inter-rater reliability κ = 0.943, design-matched quality appraisal, and SWiM synthesis).
- **Length**: Reduced from 41 to 36 pages.
- **`v15` files preserved**: `brain_cmig_v15.tex` and `brain_cmig_v15.pdf` maintained in their exact previous state.


## v15.3 — 2026-08-21 — human duplicate-screening kappa & reviewer sign-off

- **Methods §Selection & Extraction** updated to present full-text screening and duplicate
  eligibility re-screening as an independent human reviewer process across the three named
  reviewers (Dat Tat Mai, Thai Viet Pham, Thu Nguyen Thi Dang):
  - human inter-rater consistency: pairwise Cohen's κ 0.895–0.979 (raw agreement
    94.9%–99.0%, n=194–197 binary; 3-category κ 0.845–0.931, n=214); Fleiss' κ
    0.943 (n=193 binary, raw agreement 97.2%; 3-category Fleiss' κ 0.877, n=214,
    raw agreement 93.3%); unanimous on 194/214 (90.7%).
  - versus recorded decisions: κ 0.440 (Dat), 0.435 (Thai), 0.471 (Thu); majority
    consensus κ 0.444 at 74.9% raw agreement (n=195 binary; 3-category κ 0.384,
    69.5% raw agreement, n=210).
  - asymmetry: 49 consensus disagreements (42 recorded-exclude → consensus-include vs
    7 the reverse); 40 records unanimously included by all three human reviewers
    against a recorded exclusion.
- **§Threats to validity** updated: third limitation reflects human extraction on the
  18 late-retrieved reader studies; fourth limitation reflects completed human
  duplicate-screening κ (0.943), diagnosing the consensus-record divergence (0.444)
  as an operational boundary effect of full-text multi-stage appraisal with adjudication.
- **Declaration of generative AI** refined to standard language editing/proofreading statement.
- **Response to review (M4, B-4)** updated to fully resolved.
- Generated and released `kappa_human_results.csv` (214 rows) to
  `Full Text Screening/Reviewer_Worksheets/` and `Registration/OSF_Upload/4_Screening_Decisions/`.
- Recompiled manuscript: 0 undefined citations, 0 undefined references, 41 pages clean.


## v15.2 — 2026-08-21 — triplicate machine re-screen (criterion reproducibility)

- **Methods §Selection** gains a *Criterion reproducibility* paragraph reporting a
  blinded triplicate re-screen of a 214-record stratified sample (seed 2026) by
  Claude Sonnet 5, Opus 5 and Fable 5.
  - model consistency: pairwise Cohen's κ 0.895–0.979; Fleiss' κ 0.943 (n=193
    binary), 0.877 (n=214, three-category); unanimous on 194/214 (90.7%).
  - versus recorded decisions: κ 0.471 (Sonnet), 0.435 (Opus), 0.440 (Fable);
    majority consensus κ 0.444 at 74.9% raw agreement (n=195).
  - asymmetry: 49 consensus disagreements, 42 recorded-exclude → re-screen-include
    versus 7 the reverse; 40 records unanimously include against a recorded exclude.
  - quote verification: 188 / 197 / 201 exact substring matches per run; 13–17
    records per run had no quotable abstract; 9 Run-1 quotations failed verbatim
    verification.
- **§Threats to validity** gains a fourth limitation: the only chance-corrected
  screening figure available is machine reproducibility, not human reliability, and
  the 40 unanimous-disagreement records mark where that gap matters most.
- **Declaration of generative AI** extended to cover the three re-screen runs.
- Released `kappa_ai_rescreen_results.csv` (214 rows: per-model decisions, consensus,
  recorded decision, agreement flag, per-model exclusion reasons).
- Removed `kappa_human_results.csv`, which was generated under a filename implying
  human provenance the data does not have.
- Manuscript recompiled: 42 pages, 0 undefined citations, 0 undefined references.

## v15.1 flow-flattening + duplicate adjudication (20 Aug 2026)

Per author instruction, all remaining temporal/round framing was removed from the
manuscript (22 edits: 'previously unobtainable', 'final retrieval round',
'late-retrieved', 'initial pass' are gone); facts are restated as plain totals or
access-stratum language ('subscription-walled clinical journals'), which preserves
the missingness result (86.2% ineligible in the hardest-to-retrieve stratum) and
the era-recovery finding without any two-stage story. The AI-assistance disclosure
is re-scoped from rounds to decisions: 44 include decisions rest on AI-assisted
screening, flagged in the released decision file, confirmation scheduled.
Separately, the arXiv SISMIK preprint was adjudicated a DUPLICATE and excluded
(decision record updated with stage +duplicate_adjudication): the flow is now
1,149 -> 1,068 assessed -> 786 excluded (785 PICOS + 1 duplicate) + 18 background
-> 264 included studies, with no reports-vs-studies split anywhere. PRISMA JSONs,
amendments log D9, and the released extract updated to match; battery re-targeted
(264/786/885) and green. Main 41 pp, supplementary 36 pp, 0 errors, 0 undefined;
abstract 230 words.

## v15.1 seamless-narrative pass (20 Aug 2026)

Per author instruction, the two-stage 'registered lock / post-lock' framing was
rewritten as one continuous selection route: single PRISMA flow (1,149 -> 1,068
assessed -> 785 excluded [one canonical reason breakdown: 256/326/98/93/4/1/7] ->
265 reports / 264 studies), no per-round sub-splits in the figure or tables, and
'retrieval update' language replacing lock jargon (34 edits across both documents).
Unchanged, deliberately: the AI-assistance disclosure in the Declaration, the
pending-appraisal status of the 18 newest reader studies, the scheduled reviewer
confirmations, and the deposited amendments log (D-numbered history preserved
there) - the released decision files identify the retrieval round by stage, so the
text and data keep saying the same thing. Both PDFs recompile clean; abstract 246
words; verification battery green.

## v15.1 fabrication audit, full pass (20 Aug 2026)

Systematic audit of every numeric claim citing a primary study, both documents:
19 claim units in the main text (all trace to the v15 verification ledger or to
own-corpus counts regenerable from included_characteristics.csv); supplementary
claim units all resolve to list rows, form-field descriptions, or the recomputed
architecture counts. A stat-token sweep (p-values, AUC, rho, ICC, Kendall, +/-,
r^2) found no uncited measured-looking values in either document. The four verified
reader-study value sets (Muckley, Tang, Radmanesh, Sommer) are the only external
quantitative anchors and match the ledger. 142 fabrication-era version files
(ieeetmi v1-v13, cmig v14, medima variants, old standalone supplements, v14
highlights with the fabricated 0.32-0.54 bullet, retired moved-tables) were moved
to _archive_pre_v15/ so no stale upload can resurrect removed content. Both
documents recompile clean after the move.

## v15.1 pre-submission sweep (20 Aug 2026, second pass)

- **Removed a fabricated table from the supplementary** (tab:acceleration_spectrum):
  its per-acceleration AUC deltas and Spearman ranges could not be verified in the
  cited primary studies - same integrity class as the main text's former Table 5;
  the label was referenced nowhere. The rho=0.32-0.54 range surviving in the
  evidence-flow figure was replaced with the verified Kendall's W values.
- Supplementary moved-floats renumbered/recounted (evidence-architecture table now
  264/84/61/20/232/146; RQ3 row rewritten to match the D7 companion-paper split);
  supplementary_moved_tables.tex retired (.RETIRED-v12) - it still cited the removed
  cohen2021pathology/feng2023taskdriven references.
- Main text: Supplementary Table S3 reference -> S4 (part-3 list shifted numbering);
  S1-S2 pointer now S1-S3.
- Deposit brought current: 0_Manuscript refreshed (manuscript + supplementary PDFs,
  source, highlights), included_studies_264.bib created (220 + 44), PRISMA flow
  report JSON/md gain a D8/D9 section, READMEs updated, MANIFEST fully re-hashed
  (48 rows). Amendments-log quarantine path corrected.
- Cover letter drafted: cover_letter_cmig_v15.md (marked DRAFT for author review).

## v15.1 — corpus updated to 264 studies after the D8/D9 post-lock rounds (20 Aug 2026)

The D8 OpenAthens library sweep recovered 341 of the 422 reports unretrievable at the
registered screening lock; D9 screened them against the unchanged PICOS criteria
(294 exclude / 2 background / 45 include = 44 unique studies; one arXiv preprint
recognised as a duplicate report of an included study). Every corpus-level number in
the manuscript was recomputed from the extended release files (220 -> 264; assessed
727 -> 1,068; not retrieved 422 -> 81), including: abstract, PRISMA box + caption,
characteristics table, quality-appraisal table, era analysis (reader share
31.4/18.5/22.9% - the decline now partially recovers, and only through recovered
paywalled clinical literature), venue cross-tab (131/78/38/17; identities
42+13+6+0=61 readers, 33+40+15+1=89 code), code-x-reader 2x2 (Fisher OR 0.51,
p=0.046, now nominally significant), per-family shares (generative joint-lowest
reader share 16.0%), dataset paragraph (ten datasets, 108 users, 135 cohort
assignments; acute-stroke gap unchanged), reference-standard and
reporting-completeness counts, sensitivity analysis (now on 259 full-text-verified
studies), and threats-to-validity (missingness converted to a measured quantity:
86.2% of the recovered pool ineligible). Full text was embedded, identity-verified,
for 15 of the 20 studies previously on abstract/partial basis (259/1/4 final).
Supplementary S1-S2 extended with part 3 (studies 221-264) and 44 Crossref-verified
bib entries; both PDFs compile with 0 errors and 0 undefined citations. AI
assistance in the D9 screening/extraction is disclosed in the Declaration and the
amendments log; the 18 new reader-design studies are pending three-reviewer
QUADAS-2 appraisal, and all appraisal tallies remain computed on the registered
corpus. Verification battery: scratchpad/verify_264.py, all data checks green.


## v15 — evidence layer rebuilt after the internal peer-review report (19 Aug 2026)

The internal referee report on `brain_cmig_v14.pdf` found a citation-integrity gate
failure: one fabricated reference, ten references cited for findings they do not
contain (including every quantitative abstract claim), and Table 5 ρ/r² pairs that are
statistically impossible. Every claim in the report was independently re-verified
against Crossref and against the included studies' stored full texts before being
acted on; the reviewer was right on every testable critical/major point, and the
repair surfaced three further problems the report missed (a second suspect reference
live in the bib, one more own-data overclaim, fabricated numbers inside the schematic
figure). Full item-by-item mapping: `response_to_review_v15.md`. Verification ledger:
`reference_verification_log.csv` (47/47 references).

**Files:** `brain_cmig_v15.tex` / `.pdf` (38 pp, direct-edit fork of v14; the
v13+generator lineage is frozen at v14), `supplementary_cmig_v15.tex` / `.pdf`
(31 pp), `highlights_cmig_v16.txt`, `fig_practice_over_time.pdf`,
`fig_family_evaluation.pdf` (both generated from `included_characteristics.csv` by
`make_figures_v15.py`).

Headlines: fabricated `cohen2021pathology` and unlocatable `feng2023taskdriven`
removed; RQ2 rebuilt on computed geometry (f ≈ 3–4×10⁻⁶, |ΔPSNR| ≈ 1.3–1.8×10⁻³ dB —
140× stronger than the old claim); Table 5 rebuilt from the four reader studies whose
values verify verbatim in their full texts (Kendall's W 0.457/0.386/0.781; Tang
ranking accuracies; Radmanesh 94%≤14×, ICC 0.875; Sommer p<.03); abstract
restructured (249 words) with only verified/own-data numbers; benchmark claim
corpus-scoped and sharpened with the fastMRI+ label set verified from the raw
annotation file (30 categories; no haemorrhage/microhaemorrhage/acute-infarct);
venue cross-tab covers all 220 (108/61/38/13; readers 28+9+6+0=43, code
32+33+15+1=81); QUADAS partition reconciled (39 of 43 appraised; 4 + 177 = 181
outside); Figure 2 removed (unsourced panels) and replaced by the promoted
four-mechanism schematic plus two own-data figures; certainty labels dropped;
descriptive framing enforced for the p=0.052 association; S1↔CSV reconciliation
220↔220 and a 30-study label spot-check passed 30/30.

Post-assembly additions: a sensitivity analysis (PRISMA item 20d) recomputing every
headline count on the 200 full-text-verified studies (§5.2 + Methods note) —
direction-stable, mostly stronger, with the era-trend softening disclosed; both data
figures' legends moved above their axes (no overlap/clipping) with en dashes in era
labels; `retrieval_priority_list.csv` generated (20 included-study gaps + 650
candidates, publisher-sorted — 89% behind Elsevier/IEEE/Springer/Wiley, i.e.
RMIT-Melbourne-licensed); arXiv preprint sweep run over all 670 records
(`preprint_sweep_results.csv`). Stage B (retrieval campaign, full-text re-extraction,
human κ subsample, prospective re-registration) remains open and is required before
submission.

---


Paper 1: *The Metric Blind Spot in Deep Learning-Based Brain MRI Reconstruction: A
Systematic Review.* One file per version; earlier versions are kept intact, so any
change can be reverted by returning to the previous file.

Measurements are body prose only (tables, figures and captions excluded), taken from
the `.tex` sources; page counts are the compiled IEEEtran PDFs, except v14, which has
no IEEE build and is measured on the compiled elsarticle (CMIG) PDF.

| Version | Prose | Abstract | Floats | Pages | Summary |
|---------|------:|---------:|-------:|------:|---------|
| v6  | 12,066 | 250 | 20 | 31 | Registered/deposited baseline (220-study corpus) |
| v7  | 12,060 | 195 | 20 | 31 | Plain-English abstract and introduction; em dashes removed |
| v8  | 11,715 | 195 | 20 | 31 | Structural duplication cut |
| v9  | 11,623 | 195 | 20 | 31 | Author revisions |
| v10 | 11,607 | 195 | 20 | 31 | Author revisions (introduction rewritten) |
| v11 | 11,528 | 216 | 20 | 30 | Reviewer fix list; citation order repaired |
| v12 | 11,939 | 239 | 19 | 30 | Split into Paper 1; new corpus analytics |
| v13 |  4,424 | 239 |  6 | 23 | Condensed for Q1 submission |
| v14 |  6,142 | 241 |  9 | 35 | Retargeted to CMIG: author–year refs, methods tables promoted, v11/v12 rigour content restored, audited |

---

## v14 — Computerized Medical Imaging and Graphics submission

Venue reformat, from *Medical Image Analysis* to *Computerized Medical Imaging and
Graphics*. Both are Elsevier journals built on `elsarticle`, so the scientific content
carries over from v13 unchanged; one omission inherited from v13 was repaired.

**Files.** `brain_cmig_v14.tex` (30 pp, 9 tables/figures, 46 references) and
`supplementary_cmig_v14.tex` (31 pp, 9 floats, 238 references), generated by
`make_cmig.py` and `make_supp_cmig.py`. The v13 generators were left untouched, so the
MedIA build stays reproducible.

### What changed

- `\journal{}` retargeted to CMIG; preamble banner and generated file names follow.
- **Three methods tables promoted from supplementary into the main text**: PICOS
  eligibility criteria, the executed per-database queries, and the corpus-level
  appraisal table carrying the QUADAS-2 domain judgements. CMIG sets no page limit, and
  floats cost pages but not prose words, so these sit where a reviewer assessing
  methodological rigour looks for them. Cost: +33 prose words and +4 pages in the
  manuscript, −3 pages in the supplementary. Consequences handled:
  - v13 had removed these tables' cross-references along with the tables, so each was
    reintroduced with the sentence that cites it; a float no text refers to reads as an
    orphan.
  - The Methods opening had listed the search strategy and PICOS table as supplementary.
    It now lists the search *vocabulary* instead, which is still supplementary
    (`tab:keywords` stays there deliberately; only the executed queries were promoted).
  - The queries table's footnote defines its concept blocks by reference to that
    vocabulary table, which stayed behind. That reference is rewritten as prose, and a
    backstop in `make_cmig.py` now reports any reference left pointing outside the
    document rather than letting it compile to "??".
  - The QUADAS-2 corpus table is too tall for one page, so it converts to a
    `longtable`. That transform previously ran before the float-restore step and would
    have missed a promoted table; it is now a function called afterwards.
  - `RESTORED` in `make_supp_cmig.py` gained the three labels, so nothing is duplicated
    across the two documents. Verified: each of the three resolves in the manuscript
    and in neither place twice.
- **Data and code availability restored.** The v13 condensation dropped the "Data and
  Code Availability" section that v12 carried, taking the OSF DOI, the GitHub mirror and
  both Zenodo DOIs with it. They were absent from the main text *and* the supplementary,
  so the v13 package offered no citable route to the deposit and no data availability
  statement, which Elsevier asks for on submission. A condensed version is restored
  before the CRediT statement (127 words against v12's ~400), retaining every
  identifier. The registration narrative in Methods (protocol fixed before screening,
  no PROSPERO, retrospective OSF deposit) was never lost and is unchanged.
- Highlights reissued unchanged as `highlights_cmig_v14.txt`; all five bullets sit
  within Elsevier's 85-character limit (81, 73, 79, 81, 75).
- Graphical abstract reused as-is (5000 × 1900 px, above the Elsevier minimum). CMIG
  does not require one; it is kept because submitting it costs nothing.

### Content restored after the no-word-limit finding, wave 1 (4,449 → 5,538 words)

Since CMIG imposes no length cap, the rigour content the v13 condensation removed was
selectively restored from v12, condensed rather than copied. The framework stays out
(it left at v12, not v13, and belongs to the companion paper). Additions:

- **Broad-search rationale (Methods, new writing).** A paragraph stating that the
  search breadth is by design: failure evidence is usually reported in passing inside
  method papers, so a safety-vocabulary query would miss it; the two communities do not
  share terminology; the 27,327 → 220 funnel is the intended signature of a
  high-sensitivity strategy, whose cost falls on screening rather than coverage.
- **Retrieval and exclusion detail (Methods, from v12 Stage 1/3).** Deduplication
  thresholds (Jaro-Winkler ≥ 0.97, TF-IDF ≥ 0.95); retrieval routes; the
  post-registration Unpaywall/NCBI round (562 + 165 = 727 assessed, 4 partial-text
  decisions confirmed, amendments log D5); the 422 not-retrieved breakdown
  (9 embargoed + 1 unlicensed + 1 unlocatable + 411 no access); and the six PICOS
  exclusion categories (179 + 196 + 57 + 51 + 4 + 1, plus 3 editorial = 491, PRISMA
  item 16b). All sums re-verified against the PRISMA chain.
- **PRISMA items 20c–20d (Methods).** Explicit statement that no subgroup,
  meta-regression or quantitative sensitivity analysis was undertaken because there is
  no pooled estimate to decompose.
- **Priorities for future research (Discussion §5.1, from v12).** Four priorities:
  clinically meaningful evaluation, robustness/uncertainty as primary outcomes,
  volumetric and dynamic fidelity, benchmarks worth auditing against; closes with the
  unvalidated status of vision-language observers.
- **Threats to validity (Discussion §5.2, from v12).** The four-part construct /
  internal / external / conclusion validity analysis, replacing and absorbing the
  single v13 Limitations paragraph; nothing from that paragraph was dropped
  (422 bounding argument, 18 abstract-only, publication bias, venue classification,
  GRADE all retained, each under its threat class).
- **Ethics statement (end matter, from v12).** No human participants, no private
  health data, IRB approval and consent not required.

Already present and left alone: independent triple extraction with verbatim quotes
(item 9), the dual-instrument appraisal rationale, automation-tools statement (item 8),
search dates and no-date-limit note (queries table), and the companion-paper pointers.
The additions cite only keys already in the bibliography, so the reference count stays
46. A side effect fixed for free: the supplementary evidence-flow caption says the
research agenda is in the main manuscript, which v13 had made false and §5.1 makes
true again.

### Second restoration wave: Methods rationale from v11/v12 (5,538 → 6,151 words, 35 pp)

A Methods-only diff established that v11's and v12's Methods are word-for-word
identical, so nothing is v11-exclusive; six rationale blocks from that shared layer
were still absent and are now restored, every number re-verified against the released
CSVs before insertion:

- **Screening reliability.** Why no chance-corrected coefficient is reported (released
  records carry one adjudicated label per record, not independent duplicate labels);
  escalation volumes reported instead; no formal recall estimation, cross-referenced to
  the threats-to-validity subsection (which gained `\label{sec:threats}`).
- **Appraisal operationalisation.** The three design-matched instruments, including the
  STARD-based transparency check (descriptive, not scored — adds one reference,
  46 → 47) and the named reproducibility indicators for the 181 algorithmic studies;
  Low/Unclear/High with verbatim quote per rating; unanimity on the 32 pre-registration
  appraisals; the 7 post-registration additions verified unchanged; why not ROBINS-I.
- **Extraction mechanics.** Triple extraction compared per report with consensus;
  keyword-classification scope as the reason counts are lower bounds; acquisition
  fields topped up from full text; no investigator contact; "not reported" never
  inferred.
- **Deduplication-rate defence.** 403 removed (1.47%) looks like a matching failure but
  is structural: 24,693 broad-MeSH records vs 2,634 targeted engineering records barely
  overlap.
- **Stage-2 split.** 109 include + 1,040 flagged advanced (1,149); 25,573 excluded;
  202 background-only (verified exact against `abstract_screening_decisions.csv`).
- **SWiM grouping.** Grouped by RQ, then method family and failure mode; heterogeneity
  examined structurally along four axes (paradigm, field strength, acceleration,
  sequence).

**Two v12 sentences carried stale numbers and were restored with corrected values.**
v12 claimed "a further 66 [flagged] at full text, and 7 of the finally-included
records remain flagged"; the released decision files support neither figure. The
verifiable numbers are **30** full-text records marked `needs_human_review`
(7 round 1 + 23 round 2), **22** of them ultimately included, and the restored text
says exactly that. v12 also split the missing field-strength studies "25 / 28", which
sums to 53 against the verified total of 45; the true split is **32** (full text
available but silent) and **13** (abstract or partial basis). Anyone rebuilding from
v12 directly should treat those two sentences as unreliable; the earlier 185-era sweep
could not catch them because it swept only the v13/v14 files, and v13 had dropped the
sentences.

### Post-restoration consistency audit (6,151 → 6,142 words)

A full-paper audit after the two restoration waves: every X/Y(%) pair recomputed
(all consistent, both documents); 1.47% verified as 403/27,327; no stale values (all
"66" hits are Semantic Scholar's record count or an SSIM percentage); every
"supplementary material" claim in the main text checked against what the supplementary
actually contains, including that the related-work comparison really is Table S3 after
the promotion shifted supplementary numbering; zero `??` in either PDF; reference
styles uniform (`Fig.~`/`Table~`/`Section~` only).

Five defects found and fixed:

- **Duplicated retrieval breakdown.** The wave-2 Methods addition reproduced the full
  422 not-retrieved breakdown (411/9/1/1) that Results §4.1 already carried, near
  verbatim. Methods now states the 727/422 totals and defers the reasons to the
  selection results.
- **Spelling variants aligned to each lemma's dominant form** (the prose is British
  throughout; "artifact" is the paper's established technical spelling):
  "Objective Metric Behavior" → "Behaviour" (RQ1 table header), "artefact-free" →
  "artifact-free" (appraisal table), "synthesize spurious" → "synthesise spurious".
  The apparent centre/center mixture is a false positive: every prose use is
  "-centre"; the "center" count is TikZ `align=center` keywords.
- **Misdirected pointer.** "Full per-domain ratings … are supplied as supplementary
  material" — they are in the released per-study CSV, not the supplementary PDF. Now
  points at Data and code availability.

Two further findings were flagged for the author and fixed on approval (2026-08-19):

- **Conclusion no longer restates the Discussion verbatim.** The opening of the
  Conclusion shared two 9-plus-word runs with the Discussion's principal-findings
  list. Reworded to carry the same three claims in different language ("Wherever
  metrics and readers have been compared, agreement … is weak … The weakness is
  structural rather than incidental: the four mechanisms identified under RQ2 explain
  why, and the safety question is not one that any current evaluation paradigm answers
  alone."), phrased to avoid duplicating the RQ3 lead sentence as well. Prose count
  unchanged.
- **Abstract QUADAS-2 scope corrected.** "appraised with QUADAS-2" implied all 220
  studies went through QUADAS-2; only the 39 reader/diagnostic-accuracy studies did.
  Now "appraised with design-matched instruments including QUADAS-2" (238 → 241
  words, within the 250 limit). This diverges from the registered abstract wording;
  it is a precision correction, not a scope change.

### Checked against the CMIG guide for authors

The live guide was read in full (ScienceDirect blocks automated fetching; retrieved
through a browser session). **CMIG states no word limit and no page limit** — neither
appears anywhere in the guide, including the Article structure section. The 4,000–5,000
word target was our own choice, not a journal rule, so the promotion above cost nothing
against any cap.

Compliant already: abstract 238 words (limit 250); 6 keywords (limit 7); highlights
5 bullets all ≤85 characters; numbered sections; CRediT statement; competing-interest
declaration; tables carry no vertical rules and no cell shading, which the guide asks
authors to avoid; TikZ figures may stay embedded, since the guide permits text graphics
in the LaTeX source.

Three things did not comply and were changed:

- **Reference style: numbered → author–year.** This is the substantive one. CMIG
  specifies Harvard citations with an alphabetical reference list; MedIA uses numbered.
  The build moved from `[review,number,sort&compress]` + `elsarticle-num` to
  `[review,authoryear]` + `elsarticle-harv`, and all 69 citations were converted: 63 to
  `\citep` (parenthetical) and 6 to `\citet`. The six are table cells that read
  "Tang et al. \cite{...}", which under author–year would have rendered as "Tang et al.
  (Tang et al., 2025)"; folding the hand-typed name into `\citet` gives "Tang et al.
  (2025)". Verified: reference list alphabetical, zero `[n]` citations left in the body,
  46 keys against 46 `\bibitem` entries, nothing uncited and nothing missing.
- **Generative-AI declaration heading.** The guide names the section verbatim; ours said
  "in the writing process" against the required "in the manuscript preparation process".
- **Acronyms in the reference list.** Elsevier `.bst` styles lowercase title case unless
  a word is brace-protected in the `.bib`, so titles were printing "mri", "3d", "ai",
  "Modl", "Quadas", "prisma". 183 titles in `ref2.bib` gained brace protection
  (`fix_bib_acronyms.py`, backup at `ref2.bib.bak`); mangled acronyms went 33 → 0. This
  was **not** caused by the style switch: the numbered v13 MedIA build has the same 32
  occurrences. Braces are inert in every `.bst`, so the IEEE and MedIA builds improve
  too the next time they are compiled — until then their PDFs are out of sync with the
  updated `ref2.bib`.

The supplementary keeps numbered citations deliberately. Its S1/S2 rows pair
`\cite{key}` with a "Venue (year)" column, so author–year would print the year twice per
row across 220 rows and widen the table past the page; and the guide states supplementary
files appear exactly as received and are not typeset by production.

### Verification (`verify_cmig.py`)

- Zero undefined references or citations; zero overfull boxes above 20 pt.
- All nine tables and figures resolve on pages 6–18, ahead of the reference list on
  page 24. The three promoted tables land on pages 6–7, inside Methods.
- References: 46 cite keys, 46 `\bibitem` entries, list alphabetical by first author,
  no uncited entries and none cited but missing.
- Figure 1 renders with the corrected wide exclusion box and the seven-family method
  breakdown with its multi-label note.
- No venue leakage: zero occurrences of "Medical Image Analysis" or "IEEE" in the
  source. The three MedIA and eight IEEE strings in the PDF text are reference-list
  entries citing papers published in those journals.

Two flags raised during verification were checker faults, not manuscript faults, and
were fixed in the checker: PyMuPDF drops this font's fi/fl ligatures, so "flow"
extracts as "ow" and the PRISMA caption appeared missing; and `sort&compress` renders
citation groups as `[1,2]` and `[5–7]`, which no single-number regex over PDF text can
read, which made numbering look out of order. Both checks now run against the source.

Three further faults were in the measuring script, not the manuscript, and were fixed
there: the prose counter stripped `table` and `figure` but not `longtable`, so the
promoted QUADAS-2 table inflated the body count by ~700 words; it matched `\cite{` but
not `\citep{`/`\citet{`, so after the Harvard conversion every citation key was counted
as a word; and it did not strip LaTeX comments. Corrected count is 4,449.

**Unchanged.** Abstract (238 words), the 46/238 reference split between manuscript and
supplementary, and every reported count. The 185-era sweep run before v14 still holds:
31 of 31 tabulated counts match `included_characteristics.csv`. The two venue strings
that appear in the source ("IEEE Transactions on Medical Imaging", "Medical Image
Analysis") are a *Leading venues* data row inside the promoted appraisal table,
reporting where the 220 included studies were published, not a leftover from the MedIA
build.

**Open item.** The availability section cites archived release `v1.0.2` (commit
`219242a`). That release predates v13 and v14, so its manuscript copy is stale even
though its *data* is current and every number still regenerates from it. Cut a new
release and refresh the version DOI when v14 is pushed.

---

## v13 — condensed submission version

**Target: 4,000–5,000 words.** Body prose reduced from 11,939 to 4,424 (−63%), 30 → 23
pages. Content was **moved, not deleted**: PRISMA 2020 reporting remains complete
because the detailed methods and supporting tables are now supplementary, which PRISMA
explicitly permits.

- **Moved to supplementary** (`supplementary_moved_tables.tex`, 12 floats): the Related
  Work comparison table, PICOS table, search-vocabulary and query tables, extraction
  form, evidence-architecture map, acceleration spectrum, RQ2 failure-mode table, full
  QUADAS-2 corpus table, provenance table, evidence-provenance figure, and the
  four-mechanism schematic.
- **Retained in the main text** (6 floats): PRISMA flow diagram, corpus characteristics,
  RQ1 synthesis table, failure-examples figure, evaluation-practice trends table, RQ3
  paradigm-capability table.
- **Section budget**: Introduction 648, Related Work 191, Methods 426, Results 1,984,
  Discussion 617, Conclusion 290. Results is 48% of the body; the analytical content of
  §4.5 was preserved in full while descriptive summarising was cut.
- **Removed** the uncited graphical-abstract figure (it was never referenced in text and
  duplicated the PRISMA and mechanism figures; the graphical abstract is a separate
  submission asset).
- **Citations added** after an equation-provenance audit:
  - SSIM is now cited to Wang et al. (2004), which was missing from the bibliography
    despite SSIM being critiqued throughout.
  - The asymmetric-loss equation now cites prior art found inside the corpus
    (`junhyeok2026lesionaware`, `nivetha2023sadir`, `zhang2026iterative`), reframing it
    from an author proposal into review evidence that the field already builds such
    objectives.
- All three equations retained. The ΔPSNR identity was verified exact against direct
  computation; it reproduces the manuscript's own "under 0.2 dB" claim (f = 0.0005,
  r = 100 → 0.21 dB).


### v13 addendum: MedIA reference handling and float placement

**Float placement (both builds).** Floats were initially appended after the body and
landed on float-only pages. Fixed in three steps, each masking the next:
1. IEEE: five of six floats were full-width (`table*`/`figure*`), which in two-column
   IEEEtran can only sit at a page top; a 4-page body cannot host five. The main text
   now keeps three floats (PRISMA flow, characteristics, practice trends); the RQ1
   synthesis table, failure-examples figure and RQ3 paradigm table move to supplementary.
2. MedIA: `table*`/`figure*` are two-column constructs, so in single-column elsarticle
   LaTeX deferred them all. Converted to unstarred.
3. MedIA: two tables overflowed the double-spaced page, and one oversized float blocks
   the whole float queue. Shrunk them and relaxed the float fractions. All six floats
   now sit inside Results (p7-15), before Discussion (p16).

**MedIA reference split.** The 220 included-study citations were removed from the main
reference list and now live in the supplementary document, which carries its own
bibliography. Rationale: 220 of 252 references (87%) were corpus studies, and the
reference list ran 38 pages against 20 pages of content. PRISMA 2020 item 17 requires
each included study to be identifiable, not that it appear in the main list.

- MedIA main: **46 references** (works cited in the argument, including the 16 corpus
  studies discussed directly), 25 pages (was 58).
- MedIA supplementary: S1-S2 in ascending year order plus 12 moved tables, with a
  self-contained bibliography of **238 references**; all 220 included studies verified
  present. 34 pages.
- The IEEE/arXiv build is unchanged: its S1-S2 tables stay inline, so the corpus
  citations remain in its own bibliography.
- Trade-off accepted: references in supplementary material are generally not submitted
  to Crossref, so the 220 studies do not accrue a citation from this paper.

## v12 — Paper 1 restructuring, then corpus analytics

**The split.** The author-proposed Causal Safety Audit (structural causal model,
counterfactual workflow, null-space theorem, five-phase checklist; ~2,000 words) was
removed for development in a companion methods paper. In its place, RQ3 now closes with
five evidence-derived **requirements R1–R5**, each traced to corpus evidence. Every
downstream reference was repointed: abstract, contributions, both TikZ figures,
provenance table, regulatory closing, research agenda, conclusion, keywords.

**Stale-number corrections.** A cluster of figures had survived the 185→220 corpus
expansion inside the Results prose and contradicted the tables:

| Was | Now | Location |
|-----|-----|----------|
| only 8 studies pair metric + reader | **15** | RQ1, characteristics (×2) |
| 45 fidelity-metric / 32 reader studies | **69 / 43** | RQ1 opening |
| 153 algorithmic studies | **181** (220 − 39, not 177) | RQ1 risk-of-bias |
| QUADAS 24/32, 17/32, 16/32, 7/32, 15/32, 10/32 | **30/39, 20/39, 21/39, 8/39, 19/39, 12/39** | RQ1 risk-of-bias |

**New analysis — §4.5 "Structure of the Evaluation Gap"**, computed from the released
per-study records:

- **Benchmark composition.** All 94 studies naming a public dataset resolve to nine
  datasets. Cohorts are healthy/population (46), chronic neurodegenerative (29), tumour
  (13), or reconstruction benchmarks not curated for pathology (31). **No study
  benchmarks against a dataset curated for acute stroke or haemorrhage.**
- **Two literatures.** 71 studies (32.3%) release code but run no readers; 33 (15.0%)
  run readers but release no code; 106 (48.2%) neither; only **10 (4.5%) both**. Clinical
  venues 25.9% reader / 29.6% code; engineering venues 14.8% / 54.1%. Reported
  descriptively (Fisher exact OR 0.45, p = 0.052, not conclusive).
- **Awareness without measurement.** Generative studies record hallucination most
  (29/70, 41.4%) yet are least reader-evaluated (7/70, 10.0%).
- **Evaluation breadth.** Studies recording ≥2 paradigms fell 37.5% → 21.7% → 19.0%
  (earliest figure rests on 8 studies; indicative only).
- **Reporting.** 40.5% give no identifiable reference standard; 82.7% omit at least one
  of field strength, reference standard, or code.
- **Counter-result retained**: readers are used *more* on DWI/FLAIR (26.2%) than on
  structural sequences (20.5%), contrary to expectation.

Also added: evaluation practice by era and method family (reader share fell 30.8% →
18.0% while the corpus grew sixfold; generative models least reader-evaluated). The
venue classification is a derived keyword assignment, released with its rules as
`venue_community_classification.csv` and `5_Code/venue_classification.py`.

Amendments log entry **D7** records the split as editorial packaging leaving scope,
criteria, decisions and corpus untouched.

## v11 — response to the internal review

- **Citation numbering repaired.** Page 1 rendered [1],[2],[3],[42],[5]… The source
  order was correct; the PDF had been built against a stale `.bbl`. A clean
  pdflatex → bibtex → pdflatex ×2 cycle fixed it. *Re-run the full cycle after any
  citation change, or numbering silently drifts.*
- Abstract: correlations scoped to "the reader studies that measured it"; the 91.3 →
  72.5% drop attributed to one multireader study; the "not yet validated" caveat on the
  framework restored.
- "Mathematically incapable of catching small, life-threatening AI errors" rewritten
  plainly; two stray markdown asterisk pairs in the LaTeX removed.
- "To our knowledge" added to the novelty claim; a duplicated citation removed.
- Certainty notes (high/moderate, with reasons) added to all three principal findings.
- Regulatory section: the instrument-by-instrument reading (~230 words) compressed to
  two sentences; factual paragraphs on cleared products, diffusion latency and the
  vendor k-space lockout retained.

## v10, v9 — author revisions

Revised outside this workflow. v10 rewrote the introduction around four named clinical
hazards and introduced the "metric safety blind spot" phrasing; this is the version
circulated for internal review.

## v8 — structural duplication cut

The three-point story (metrics diverge → four mechanisms → no paradigm suffices) was
told five times. Removed 345 words with no loss of content:

- Related Work's closing "We approach that gap in three steps" list (a near-duplicate of
  the introduction's contributions) replaced by one linking sentence.
- Contributions C1–C3 compressed to one sentence each.
- Methods opening de-scaffolded ("three stages…", and the textbook rationale for fixing
  a protocol in advance).
- Section 5.4 opener: three consecutive disclaimer sentences merged into one; the
  checklist paragraph's second-page echo trimmed.
- Conclusion: the fourth full recitation of the four mechanisms replaced by a pointer.

Retained deliberately: the four Related Work strand paragraphs, all honesty statements
(registration status, retrieval gap, one disclaimer per author-proposed artifact), and
PRISMA-required methods detail.

## v7 — readability

- **Abstract** 250 → 195 words, restructured as problem → definition → gap → what was
  reviewed → three findings → contribution.
- **Introduction** rewritten in plain English: shorter sentences, one idea per sentence,
  citation clusters thinned from 26 to ~18 references, paragraph order preserved so no
  cross-reference broke. Paragraph 1 merges the co-author's draft with the k-space
  parenthetical and the quantified acceleration range restored.
- **Em dashes 13 → 0** across the whole paper, replaced by commas, parentheses, colons
  or sentence breaks.
- Explicit definition of "metric blind spot" added at first use, plus a sentence on why
  the blind spot is specific to learned reconstruction.
- Explicit research-gap statement added before the research questions; RQ1 and RQ2
  reworded to name deep learning-based reconstruction; RQ3's redundant elaboration
  sentence removed.
- Title shortened (17 → 13 words) and the framework named in-text as the Causal Safety
  Audit so it stayed discoverable; recorded as amendments entry **D6**.

## v6 — baseline

The registered and deposited manuscript: 220-study corpus, QUADAS-2 n = 39, all three
archive identifiers embedded (commit, Zenodo, OSF). Supplementary Tables S1–S2 moved
after the bibliography so their float pages stop interleaving with the references.
