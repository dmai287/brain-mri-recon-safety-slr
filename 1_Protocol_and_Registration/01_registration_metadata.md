# OSF registration metadata — form field values

Copy these directly into the OSF project and registration forms.

---

## 1. Project title

```
The Metric Blind Spot in Deep Learning Brain MRI Reconstruction: A Systematic Review and Causal Safety Framework
```

## 2. Contributors

Add in this order; the first is the corresponding author and project administrator.

| # | Name | Affiliation | E-mail | Role on OSF | ORCID |
|---|---|---|---|---|---|
| 1 | Dat Tat Mai | School of Science, Engineering & Technology, RMIT University Vietnam, Ho Chi Minh City, Vietnam | dat.mai2@rmit.edu.vn | Administrator | [0009-0006-5256-5646](https://orcid.org/0009-0006-5256-5646) |
| 2 | Thai Viet Pham | School of Computing Technologies, RMIT University, Melbourne, VIC, Australia | s4229249@student.rmit.edu.au | Read + Write | [0009-0003-3707-5081](https://orcid.org/0009-0003-3707-5081) |
| 3 | Thu Nguyen Thi Dang | School of Health and Biomedical Science, RMIT University, Melbourne, VIC, Australia | S4205224@student.rmit.edu.au | Read + Write | [0000-0002-7232-2477](https://orcid.org/0000-0002-7232-2477) |
| 4 | James Jin Kang | School of Science, Engineering & Technology, RMIT University Vietnam, Ho Chi Minh City, Vietnam | james.kang@rmit.edu.vn | Administrator | [0000-0002-0242-4187](https://orcid.org/0000-0002-0242-4187) |

Corresponding author and guarantor: Dat Tat Mai (dat.mai2@rmit.edu.vn).
E-mail addresses match the `\thanks` block of the manuscript.

All four are added as contributors on the OSF draft, each marked as a bibliographic
contributor. All four ORCID iDs are recorded above. An ORCID is linked to an OSF *account*, not
frozen into the registration, so each author can authenticate with ORCID after registering
and it will attach to their profile. Linking beforehand is tidier, but it is not a blocker.

> Registrations themselves are frozen and cannot be edited or deleted, only
> withdrawn. Title, description, publication DOI, affiliated institutions, licence
> and tags remain editable by an administrator afterwards, and further contributors
> can be added. Plan the *content* of the registration as final; account-level
> details such as ORCID are not.

## 3. Project description

```
A systematic review of how the safety, artifacts, and fidelity of deep-learning brain MRI
reconstruction are evaluated, following PRISMA 2020.

Deep neural priors can shorten brain MRI acquisition four- to tenfold, but the same priors
can erase or invent diagnostic detail without disturbing the numbers used to certify them.
Seven databases were searched to July 2026 for primary studies of human brain MRI
reconstruction reporting fidelity, artifact, robustness, or observer outcomes. From 27,327
records identified and 26,924 after deduplication, 220 primary studies published between
1995 and 2026 were included.

The review asks three questions: (RQ1) how far do pixel-wise fidelity metrics diverge from
radiologist judgement; (RQ2) what mechanisms explain that divergence; and (RQ3) what
evaluation paradigms could establish reconstruction safety before deployment. Risk of bias in
the diagnostic-accuracy and reader-study subset was appraised with QUADAS-2; the remaining
algorithmic studies were appraised on reproducibility and robustness.

REGISTRATION STATUS: This is a RETROSPECTIVE registration. The review was completed before
this registration was created. The protocol was fixed in the project repository on
2026-07-23, before screening began on 2026-07-27, but that timestamp rests on filesystem
metadata rather than an independent registry, and is therefore not offered as proof of
prospective registration. Protocol deviations are documented in full in the registered
amendments log.

This review was not registered with PROSPERO, which does not accept reviews without a direct
clinical health outcome.
```

## 4. Registration form answers (Open-Ended Registration)

**"Summary" / narrative field:**

```
This registration documents a completed systematic review of evaluation practice in
deep-learning brain MRI reconstruction (PRISMA 2020; 220 included studies; seven databases
searched 23-24 July 2026).

It is a RETROSPECTIVE registration: searching, screening, data extraction, quality appraisal
and manuscript drafting were complete before this registration was created. It is made to
place the protocol, search strategy, eligibility criteria, extraction form, appraisal plan,
per-study data and full deviation log on the permanent public record, not to assert that the
plan was registered in advance of the work.

The registered materials comprise: the review protocol (PRISMA-P structure), the complete
search strings as executed for each of the seven databases with retrieval counts, the PICOS
eligibility criteria and operational screening rules, the data extraction form, the risk-of-
bias appraisal plan, per-study characteristics and per-study appraisal records for all 220
included studies, the PRISMA 2020 flow counts and checklist, and a log of every deviation
from the original protocol.

Readers are directed in particular to the amendments and deviations log, which records four
substantive departures from the protocol as first written, including the decision to drop the
LLM-as-Judge concept from the required search terms in order to widen recall.
```

**Category:** `Systematic Review or Meta-Analysis`
**Licence:** `CC-BY 4.0 (Attribution)`
**Embargo:** none (register immediately public)

## 5. Keywords / tags

```
systematic review; PRISMA 2020; brain MRI; MRI reconstruction; accelerated MRI;
deep learning; image reconstruction; reconstruction safety; hallucination; artifacts;
image quality assessment; observer study; reader study; QUADAS-2; uncertainty estimation;
diffusion models; k-space; medical imaging evaluation
```

## 6. Subjects (OSF taxonomy)

- Engineering → Biomedical Engineering and Bioengineering
- Medicine and Health Sciences → Radiology
- Physical Sciences and Mathematics → Computer Sciences → Artificial Intelligence

## 7. Related identifiers

| Field | Value |
|---|---|
| Preprint / article DOI | _add once available_ |
| Code repository | `https://github.com/dmai287/brain-mri-recon-safety-slr` |
| Funding | _state funder and grant number, or "No specific funding received"_ |
| Conflicts of interest | _state, or "The authors declare no competing interests"_ |

> The manuscript's Data and Code Availability section names the GitHub repository above.
> Confirm it is public and populated **before** registering, or replace the link with the
> OSF project itself. A registration pointing at a non-existent repository is worse than one
> that hosts the files directly.

## 8. After registering

1. Copy the registration DOI (`10.17605/OSF.IO/XXXXX`).
2. Insert it into `brain_ieeetmi_v6.tex` using the replacement wording in
   `07_amendments_and_deviations.md` §4.
3. Add the DOI to the manuscript's Data and Code Availability section.
4. A registration is **permanent and cannot be edited**. Corrections are made by withdrawing
   (leaving a public tombstone) or by registering an amendment. Get §4 of the amendments log
   settled before you press submit.
