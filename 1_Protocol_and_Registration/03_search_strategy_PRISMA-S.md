# Search strategy (PRISMA-S)

**Review:** The Metric Blind Spot in Deep Learning Brain MRI Reconstruction  
**Searches executed:** 23–24 July 2026 (all databases searched within a single 48-hour window)  
**Deduplication run:** 24 July 2026  
**Date limits:** none applied (no lower bound; upper bound = date of search)  
**Language limit:** English (applied at screening, not in the query)  
**Search performed by:** D.T. Mai, using scripted API access (no manual interface searching)

---

## 1. Databases searched

| # | Database | Access method | Records retrieved | Duplicates removed |
|---|---|---|---|---|
| 1 | PubMed / MEDLINE | NCBI E-utilities (esearch/efetch) | 24,693 | 203 |
| 2 | SpringerLink | Springer Nature Meta API v2 | 1,598 | — |
| 3 | IEEE Xplore | IEEE Xplore Metadata API v1 | 778 | 91 |
| 4 | Scopus | Elsevier Scopus Search API | 127 | 87 |
| 5 | Semantic Scholar | Semantic Scholar Graph API | 66 | — |
| 6 | OpenAlex | OpenAlex REST API | 34 | — |
| 7 | Web of Science | Clarivate Web of Science Expanded API | 31 | 22 |
| | **Total** | | **27,327** | **403** |

Unique records after deduplication: **26,924**.

Embase was attempted but no institutional entitlement was available; the ACM Digital
Library offers no programmatic search API and was not searched. Both are recorded as
limitations rather than omissions.

## 2. Search structure

All queries implement the same three-concept Boolean structure, combined with AND:

```
  ( brain MRI / neuroimaging terms )
AND ( AI/ML image-reconstruction terms )
AND ( reconstruction safety / fidelity / artifact / failure-mode terms )
NOT ( animal model OR case report OR in vitro )
```

A fourth concept from the original protocol — *LLM-as-Judge / automated evaluation
methodology* — was deliberately **not** made a required AND-term, so that the search
would recover the whole evaluation landscape rather than only LLM-based evaluation.
This decision is recorded in `protocol.json` (`reviewer_clarifications`) and dated
before any screening. See `07_amendments_and_deviations.md`, item D1.

## 3. Full search strings as executed

### PubMed / MEDLINE

*Interface:* NCBI E-utilities (esearch/efetch)  
*Records retrieved:* 24,693

```
(("brain MRI"[Title/Abstract] OR "brain magnetic resonance imaging"[Title/Abstract] OR "cerebral MRI"[Title/Abstract] OR "cranial MRI"[Title/Abstract] OR neuroimag*[Title/Abstract] OR "brain imaging"[Title/Abstract] OR brain scan*[Title/Abstract] OR "Brain"[Mesh] OR "Magnetic Resonance Imaging"[Mesh] OR "Neuroimaging"[Mesh]) AND (image reconstruction*[Title/Abstract] OR "MRI reconstruction"[Title/Abstract] OR "MR reconstruction"[Title/Abstract] OR "accelerated MRI"[Title/Abstract] OR "undersampled reconstruction"[Title/Abstract] OR "k-space reconstruction"[Title/Abstract] OR "deep learning reconstruction"[Title/Abstract] OR "neural network reconstruction"[Title/Abstract] OR "generative reconstruction"[Title/Abstract] OR "super-resolution MRI"[Title/Abstract] OR "denoising"[Title/Abstract] OR "Image Processing, Computer-Assisted"[Mesh] OR "Deep Learning"[Mesh] OR "Machine Learning"[Mesh]) AND (hallucinat*[Title/Abstract] OR "hallucinated pathology"[Title/Abstract] OR "geometric distortion"[Title/Abstract] OR "anatomical distortion"[Title/Abstract] OR reconstruction artifact*[Title/Abstract] OR reconstruction error*[Title/Abstract] OR "safety evaluation"[Title/Abstract] OR "trustworthiness"[Title/Abstract] OR "reliability assessment"[Title/Abstract] OR "image fidelity"[Title/Abstract] OR "diagnostic accuracy loss"[Title/Abstract] OR "Artifacts"[Mesh] OR "Reproducibility of Results"[Mesh] OR "Diagnostic Errors"[Mesh])) NOT ("animal model"[Title/Abstract] OR "case report"[Title/Abstract] OR "in vitro"[Title/Abstract])
```

### SpringerLink

*Interface:* Springer Nature Meta API v2  
*Records retrieved:* 1,598

```
(("brain MRI" OR "brain magnetic resonance imaging" OR "cerebral MRI" OR "cranial MRI" OR neuroimag OR "brain imaging" OR "brain scan") AND ("image reconstruction" OR "MRI reconstruction" OR "MR reconstruction" OR "accelerated MRI" OR "undersampled reconstruction" OR "k-space reconstruction" OR "deep learning reconstruction" OR "neural network reconstruction" OR "generative reconstruction" OR "super-resolution MRI" OR denoising) AND (hallucinat OR "hallucinated pathology" OR "geometric distortion" OR "anatomical distortion" OR "reconstruction artifact" OR "reconstruction error" OR "safety evaluation" OR trustworthiness OR "reliability assessment" OR "image fidelity" OR "diagnostic accuracy loss")) NOT ("animal model" OR "case report" OR "in vitro")
```

### IEEE Xplore

*Interface:* IEEE Xplore Metadata API v1  
*Records retrieved:* 778

```
(("brain MRI" OR "brain magnetic resonance imaging" OR "cerebral MRI" OR "cranial MRI" OR neuroimag* OR "brain imaging" OR brain scan*) AND (image reconstruction* OR "MRI reconstruction" OR "MR reconstruction" OR "accelerated MRI" OR "undersampled reconstruction" OR "k-space reconstruction" OR "deep learning reconstruction" OR "neural network reconstruction" OR "generative reconstruction" OR "super-resolution MRI" OR "denoising") AND (hallucinat* OR "hallucinated pathology" OR "geometric distortion" OR "anatomical distortion" OR reconstruction artifact* OR reconstruction error* OR "safety evaluation" OR "trustworthiness" OR "reliability assessment" OR "image fidelity" OR "diagnostic accuracy loss")) NOT ("animal model" OR "case report" OR "in vitro")
```

### Scopus

*Interface:* Elsevier Scopus Search API  
*Records retrieved:* 127

```
((TITLE-ABS-KEY("brain MRI" OR "brain magnetic resonance imaging" OR "cerebral MRI" OR "cranial MRI" OR neuroimag* OR "brain imaging" OR "brain scan")) AND (TITLE-ABS-KEY("image reconstruction" OR "MRI reconstruction" OR "MR reconstruction" OR "accelerated MRI" OR "undersampled reconstruction" OR "k-space reconstruction" OR "deep learning reconstruction" OR "neural network reconstruction" OR "generative reconstruction" OR "super-resolution MRI" OR denoising)) AND (TITLE-ABS-KEY(hallucinat* OR "hallucinated pathology" OR "geometric distortion" OR "anatomical distortion" OR "reconstruction artifact" OR "reconstruction error" OR "safety evaluation" OR trustworthiness OR "reliability assessment" OR "image fidelity" OR "diagnostic accuracy loss"))) AND NOT (TITLE-ABS-KEY("animal model" OR "case report" OR "in vitro"))
```

### Semantic Scholar

*Interface:* Semantic Scholar Graph API  
*Records retrieved:* 66

```
("brain MRI" | "brain magnetic resonance imaging" | "cerebral MRI" | "cranial MRI" | neuroimag* | "brain imaging" | "brain scan") + ("image reconstruction" | "MRI reconstruction" | "MR reconstruction" | "accelerated MRI" | "undersampled reconstruction" | "k-space reconstruction" | "deep learning reconstruction" | "neural network reconstruction" | "generative reconstruction" | "super-resolution MRI" | denoising) + (hallucinat* | "hallucinated pathology" | "geometric distortion" | "anatomical distortion" | "reconstruction artifact" | "reconstruction error" | "safety evaluation" | trustworthiness | "reliability assessment" | "image fidelity" | "diagnostic accuracy loss") -"animal model" -"case report" -"in vitro"
```

### OpenAlex

*Interface:* OpenAlex REST API  
*Records retrieved:* 34

```
title_and_abstract.search:"brain MRI"|"brain magnetic resonance imaging"|"cerebral MRI"|"cranial MRI"|neuroimag|"brain imaging"|"brain scan",title_and_abstract.search:"image reconstruction"|"MRI reconstruction"|"MR reconstruction"|"accelerated MRI"|"undersampled reconstruction"|"k-space reconstruction"|"deep learning reconstruction"|"neural network reconstruction"|"generative reconstruction"|"super-resolution MRI"|denoising,title_and_abstract.search:hallucinat|"hallucinated pathology"|"geometric distortion"|"anatomical distortion"|"reconstruction artifact"|"reconstruction error"|"safety evaluation"|trustworthiness|"reliability assessment"|"image fidelity"|"diagnostic accuracy loss"
```

### Web of Science

*Interface:* Clarivate Web of Science Expanded API  
*Records retrieved:* 31

```
TS=("brain MRI" OR "brain magnetic resonance imaging" OR "cerebral MRI" OR "cranial MRI" OR neuroimag* OR "brain imaging" OR "brain scan*") AND TS=("image reconstruction*" OR "MRI reconstruction" OR "MR reconstruction" OR "accelerated MRI" OR "undersampled reconstruction" OR "k-space reconstruction" OR "deep learning reconstruction" OR "neural network reconstruction" OR "generative reconstruction" OR "super-resolution MRI" OR denoising) AND TS=(hallucinat* OR "hallucinated pathology" OR "geometric distortion" OR "anatomical distortion" OR "reconstruction artifact*" OR "reconstruction error*" OR "safety evaluation" OR trustworthiness OR "reliability assessment" OR "image fidelity" OR "diagnostic accuracy loss") NOT TS=("animal model" OR "case report" OR "in vitro")
```

## 4. Supplementary search methods

| Method | Used | Detail |
|---|---|---|
| Database searching | Yes | Seven databases, above |
| Citation/reference chasing | No | Not performed as a systematic step |
| Forward citation searching | No | Not performed |
| Grey literature | No | Excluded by design (peer-reviewed sources only) |
| Preprint servers | No | Preprints excluded a priori; 0 preprint records retained |
| Trial registries | No | Not applicable to a methodological review |
| Contacting authors | Partial | Attempted only for missing full text, not to identify studies |
| Hand-searching | No | Not performed |

The absence of citation chasing and grey-literature searching is a real limitation of
recall and is declared as such.

## 5. Peer review of the search

The search was **not** formally peer reviewed against PRESS 2015 by an independent
information specialist. This is declared as a limitation.

## 6. Reproducibility

Every query above was issued programmatically; the scripts are released with the
review. Re-running them against the same databases after the search date will return
a superset, because no upper date bound is encoded in the query itself.
