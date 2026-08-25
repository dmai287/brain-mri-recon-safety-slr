# The Metric Blind Spot in Deep Learning Brain MRI Reconstruction

Protocol, search strategy, PRISMA records, per-study characteristics, screening decisions, and analysis code for a systematic review of how the safety, artifacts, and fidelity of deep-learning brain MRI reconstruction are evaluated.

**27,327 records identified → 26,924 after deduplication → 1,068 full texts assessed → 263 primary studies included**, spanning 1995–2026 across seven databases (PubMed/MEDLINE, SpringerLink, IEEE Xplore, Scopus, Semantic Scholar, OpenAlex, Web of Science).

## Repository Layout

| Path | Contents |
|---|---|
| `0_Manuscript/` | The compiled manuscript (PDF), supplementary material, and full LaTeX sources (v26) |
| `1_Protocol_and_Registration/` | Protocol as PRISMA-P 2015, search strategy as PRISMA-S, eligibility criteria, extraction form, appraisal plan, deviations log, `protocol.json`, `search_strategy.json`, and reviewer sign-off worksheets |
| `2_PRISMA/` | Flow report, stage-by-stage `prisma_log.json`, per-database identification counts, and PRISMA 2020 checklist |
| `3_Included_Studies/` | Per-study characteristics (`included_characteristics.csv`), supplementary appraisal (`included_characteristics_supplement.csv`), BibTeX for all 263 studies (`included_studies_263.bib`), QUADAS-2 worksheets (`quadas2_three_reviewer_worksheet.csv`), and data dictionary |
| `4_Screening_Decisions/` | Full title/abstract decisions (26,924 records) and full-text screening ledgers across all screening rounds, plus duplicate screening agreement worksheets (`kappa_human_results.csv`, `kappa_worksheet_214_HUMAN_*.csv`) |
| `5_Code/` | Python scripts for data assembly (`assemble.py`), figure generation (`make_figures.py`, `make_dpsnr_figure.py`), venue classification, and validation |
| `MANIFEST.csv` | File index with sizes, paths, and SHA-256 checksums |

## Key Findings of the Systematic Review

1. **Only 18 of 263 included studies (6.8%)** record both a pixel-wise fidelity metric (PSNR/SSIM) and a radiologist reader evaluation on the same dataset.
2. **Spatial Averaging Blind Spot:** Erasing a 5 mm³ punctate infarct shifts global PSNR by less than 0.003 dB—making clinically decisive tissue loss undetectable by standard image-quality metrics.
3. **Structural Community Divide:** 36.9% (97/263) of studies provide open code and 21.7% (57/263) perform human reader assessment, but only 4.9% (13/263) do both.
4. **Benchmark Limitations:** Zero public brain MRI reconstruction benchmarks are curated with clinically verified acute stroke or intracranial haemorrhage annotations.

## Reproducing the Analysis and Figures

```bash
cd 5_Code
python assemble.py          # Verify and reconcile per-study data against published counts
python make_figures.py      # Rebuild Figures 3 and 4
python make_dpsnr_figure.py # Rebuild Figure 2 (Delta-PSNR sensitivity map)
```

## Citation

See `CITATION.cff`. Article citation and DOI will be updated upon final publication.

## Licence

CC BY 4.0 (see `LICENSE`). Third-party bibliographic metadata remains under its respective terms.
