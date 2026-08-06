# Data extraction form and coding rules

Realised output: `../LaTex PDF/included_characteristics.csv` (185 rows × 18 columns).
Data dictionary: `../LaTex PDF/included_characteristics_README.md`.

---

## 1. Extracted variables

| Field | Type | Values / rule |
|---|---|---|
| `study_key` | ID | Stable within-review identifier S001–S185, ordered by year |
| `pmid`, `doi`, `year`, `journal`, `title` | Bibliographic | From the source record front-matter |
| `study_design` | Single | `Algorithmic / methodological reconstruction study` \| `Diagnostic accuracy / reader study` |
| `method_family` | **Multi** | `Compressed sensing / parallel imaging`, `Generative (GAN/diffusion/VAE)`, `Motion correction`, `Physics-based / unrolled`, `Denoising`, `Super-resolution`, `Self-supervised / unsupervised` |
| `evaluation` | **Multi** | `Pixel-wise metrics (PSNR/SSIM/NRMSE)`, `Observer / reader study`, `Uncertainty estimation`, `Perceptual / learned metrics` |
| `failure_modes` | **Multi** | `Artifacts (aliasing/ghosting/Gibbs)`, `Hallucination / fidelity / instability`, `Geometric / anatomical distortion`, `Motion degradation`, `Robustness / distribution shift` |
| `field_strength` | Single | `3T` \| `1.5T` \| `7T` \| `not reported` |
| `field_strength_evidence` | Text | Verbatim supporting snippet |
| `pulse_sequences` | **Multi** | `T1w`, `T2w`, `FLAIR`, `DWI`, `SWI` |
| `reference_standard` | Single | `Fully sampled acquisition` \| `Expert reader consensus` \| `Conventional/standard-of-care acquisition` \| `Stated ground truth (unspecified)` \| `Not stated` |
| `public_dataset_or_benchmark` | **Multi** | Named datasets detected (fastMRI, ADNI, HCP, IXI, BraTS, OASIS, …) |
| `code_available` | Single | `yes` \| `not stated` |
| `full_text_basis` | Single | `full text` \| `partial full text (truncated)` \| `abstract + MeSH only` |
| `source_record` | Text | Filename of the source record |

Multi-valued fields are `;`-separated. A study may carry several method families or failure
modes; totals therefore exceed 185 by design (254 method-family labels, 103 evaluation labels).

## 2. Coding rules

1. **Not stated ≠ absent.** Where a variable is not stated in the source it is recorded as
   `not reported` / `not stated`, never inferred. This is why 53 studies carry
   `field_strength = not reported`.
2. **Lower bounds.** Classification is keyword-based over titles, abstracts and MeSH terms
   (field strength and sequences additionally use full text, since those are usually stated
   only in the acquisition subsection). Counts are **lower bounds on prevalence**, not
   exhaustive counts, and must be reported as such.
3. **Evidence required.** Derived judgement fields carry a verbatim supporting quotation so
   any single value can be checked without re-reading the paper.
4. **Text sufficiency is recorded.** `full_text_basis` states what each row rests on: 142/185
   full text, 19/185 partial, 24/185 abstract + MeSH only.

## 3. Verification

- Every `include` decision was checked against its full text by the authors.
- All extracted values were re-derived programmatically from stored source records, so the
  file regenerates deterministically (`scripts/prep_corpus.py`, `scripts/assemble.py`).
- A domain-vocabulary integrity sweep over all substantive full texts detected one record
  (S004, PMID 17117780) carrying a **wrong PDF** — an unrelated sonar-visualisation paper.
  It was quarantined, its contaminated chunks removed from the retrieval index, and the study
  re-appraised from abstract and MeSH. No further mismatches were found.

## 4. Not extracted

Deliberately out of scope, and their absence should not be read as "not reported by the
studies": acceleration factor as a numeric variable, scanner vendor and model, sample size for
algorithmic studies, training-set size, and per-metric numeric values (PSNR/SSIM figures).
These were judged too heterogeneously reported across the corpus to code reliably, and the
review makes no claim requiring them.

## 5. Fields promised in the manuscript but not released

The manuscript's Table maps studies to research questions (RQ1 123, RQ2 83, RQ3 40). **No
per-study `rq_mapping` column is released**, because no keyword rule reproduces that split at
any defensible threshold — a broad rule assigns RQ2 to 184 of 185 studies. Publishing a
heuristic column would imply traceability the data does not support. If the assignment rule
actually used is supplied, the column can be regenerated.
