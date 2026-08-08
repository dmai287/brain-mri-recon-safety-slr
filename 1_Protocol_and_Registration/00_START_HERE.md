# OSF registration package — start here

Everything needed to register this systematic review on the Open Science Framework.

**Review:** The Metric Blind Spot in Deep Learning Brain MRI Reconstruction: A Systematic
Review and Causal Safety Framework
**Package prepared:** 6 August 2026

---

## ⚠ Read this first: the registration is RETROSPECTIVE

The review is **complete** — searching, screening, extraction, appraisal and manuscript
drafting have all finished. An OSF registration created now carries an OSF timestamp of the
date you submit it, which is *after* the work was done. Under PRISMA 2020 item 24a this must
be reported as a **retrospective registration**, not a prospective one.

This matters because of what is currently in the manuscript. `brain_ieeetmi_v6.tex` L334–338
states:

> "The protocol is pre-registered in the project repository (`protocol.md`), timestamped
> before screening began. We did not register with PROSPERO... and the review is not
> registered in any other prospective register. The review was carried out as specified in
> that protocol, and we made no amendment to the research questions, eligibility criteria,
> search strategy, screening procedure..."

Three problems with that passage as it stands:

1. **`protocol.md` does not exist.** The protocol is `protocol.json` plus `search_strategy.json`.
2. **Neither file is tracked in git.** There is no independent, tamper-evident timestamp —
   only filesystem mtime (2026-07-23 16:33), which anyone can set and which no reviewer will
   accept as evidence of pre-registration. Screening artifacts are dated 2026-07-27, so the
   4-day gap is real, but it is not *provable* from the repository as currently constituted.
3. **"We made no amendment"** is not accurate — see `07_amendments_and_deviations.md`, which
   documents four substantive decisions, one of which (dropping the LLM-as-Judge concept from
   the required search terms) changed what the search retrieved.

**Recommended fix:** register on OSF now, declare it retrospective, upload the protocol files
as-is, and rewrite the manuscript passage using the wording supplied in
`07_amendments_and_deviations.md` §4. That is defensible and honest. Presenting this as a
prospective registration would not be.

PROSPERO is correctly ruled out — it requires a direct health-related outcome, which a
methodological review of evaluation practice does not have. OSF Registries is the right venue.

---

## What to do, in order

1. **Create an OSF project** (not a registration yet) at <https://osf.io> →
   *My Projects* → *Create Project*. Use the title and description in `01_registration_metadata.md`.
2. **Add components and upload files** per `08_file_manifest.md`.
3. **Add contributors** (see `01_registration_metadata.md` §2), set their roles, and set the
   project licence to **CC-BY 4.0**.
4. **Make the project public** — a registration inherits the project's files, and a private
   project produces a registration nobody can inspect.
5. **Register**: project → *Registrations* → *New registration* → choose
   **"Open-Ended Registration"** (see below for why).
6. Answer the registration form using `01_registration_metadata.md` §4.
7. **Do not embargo**, unless a journal requires it. If you do, use the shortest period.

### Which OSF template?

| Template | Verdict |
|---|---|
| **Open-Ended Registration** | ✅ **Use this.** It is the only template that fits a completed review without asking you to answer prospective-tense questions ("what *will* you do") untruthfully. You attach the full protocol as a file. |
| OSF Preregistration | ❌ Written for prospective studies with hypotheses and planned analyses; asks whether data collection has begun. Answering it for finished work invites misrepresentation. |
| AsPredicted.org | ❌ Designed for experiments, not reviews. |
| Registered Report Protocol Preregistration | ❌ For Stage-1 registered reports. |

If you later run an **update or extension** of this review, register *that* prospectively with
the OSF Preregistration template before you begin.

---

## Package contents

| File | Purpose |
|---|---|
| `00_START_HERE.md` | This file |
| `01_registration_metadata.md` | Title, contributors, description, keywords, licence, and answers for the OSF form |
| `02_protocol_PRISMA-P.md` | The review protocol, structured to PRISMA-P 2015 (17 items) |
| `03_search_strategy_PRISMA-S.md` | Full search strings as executed, per database, with counts |
| `04_eligibility_criteria.md` | PICOS and the operational screening rules |
| `05_data_extraction_form.md` | The extraction form and coding rules |
| `06_risk_of_bias_plan.md` | Appraisal instruments, domains, and procedure |
| `07_amendments_and_deviations.md` | **Protocol deviations — read before submitting** |
| `08_file_manifest.md` | What to upload where, and what to withhold |

## Honest-reporting checklist before you submit

- [ ] Registration type declared **retrospective** in the OSF description
- [x] Manuscript registration statement rewritten (wording in `07_amendments_and_deviations.md` §4)
- [ ] Manuscript registration statement updated with the OSF DOI once minted
- [x] Risk-of-bias worksheet independently appraised by three reviewers with complete
      agreement (see `06_risk_of_bias_plan.md` §5)
- [x] Table VI and Table VII recomputed from the released per-study files (220-study corpus)
- [ ] `protocol.json` and `search_strategy.json` committed to git so future timestamps are real
