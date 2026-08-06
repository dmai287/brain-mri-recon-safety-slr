#!/usr/bin/env python3
"""Stage 2: assemble the two per-study release files the paper promises.

  included_characteristics.csv            - per-study extracted characteristics (PRISMA item 19)
  included_characteristics_supplement.csv - per-study quality appraisal / risk of bias (PRISMA item 18)

Existing characteristics columns (method_family, evaluation, failure_modes) are carried through
VERBATIM from the current file so the paper's published aggregates remain reproducible.
QUADAS-2 ratings come from the appraisal worksheets in quadas/ and are marked
pending_reviewer_verification until the two human reviewers sign off.
"""
import csv, json, re, collections
from pathlib import Path

OUT = Path(__file__).parent
REVIEW = Path(r"C:\Users\V133280\RMIT University\Thai Pham - StrokeVault\Brain MRI Reconstruction Safety Review - Broad")
DEST = REVIEW / "LaTex PDF"

corpus = json.load(open(OUT / "corpus.json", encoding="utf-8"))

# ---- load QUADAS-2 appraisal worksheets ----
quadas = {}
for f in sorted((OUT / "quadas").glob("batch*.json")):
    for rec in json.load(open(f, encoding="utf-8")):
        quadas[rec["key"]] = rec
print(f"QUADAS-2 worksheets loaded: {len(quadas)}")

# ---- RQ mapping (documented keyword rule; reported as lower bounds like the other prevalence counts) ----
RQ2_PAT = (r"hallucinat|fabricat|spurious|artifact|distort|erasure|removed|suppress|over-?smooth|"
           r"instabilit|fail|bias|blur|false (?:positive|negative)|miss(?:ed|ing) lesion")
RQ3_PAT = (r"causal|counterfactual|structural causal|do\(|intervention|physics-?(?:based|informed|guided|constrained)|"
           r"data consistency|k-?space residual|uncertaint|conformal|out-?of-?distribution|distribution shift|"
           r"automated observer|model observer|foundation model|language model|\bLLM\b")


def rq_labels(rec):
    blob = " ".join([rec["title"], rec["abstract"], rec["mesh"], rec.get("fulltext", "")[:20000]])
    ev = rec["csv"]["evaluation"] or ""
    out = []
    # RQ1: contributes to metric-vs-reader divergence evidence
    if "Pixel-wise" in ev or "Observer" in ev or "Perceptual" in ev:
        out.append("RQ1")
    # RQ2: documents a failure mechanism / failure mode
    if (rec["csv"]["failure_modes"] or "").strip() or re.search(RQ2_PAT, blob, re.I):
        out.append("RQ2")
    # RQ3: causal / physics-gated / uncertainty-aware / automated-observer evaluation
    if re.search(RQ3_PAT, blob, re.I):
        out.append("RQ3")
    return ";".join(out)


def reference_standard(rec):
    blob = " ".join([rec["abstract"], rec.get("fulltext", "")[:30000]])
    if re.search(r"fully[- ]sampl", blob, re.I):
        return "Fully sampled acquisition"
    if re.search(r"ground truth", blob, re.I):
        return "Stated ground truth (unspecified)"
    if re.search(r"radiolog|expert read|reference read", blob, re.I):
        return "Expert reader consensus"
    if re.search(r"conventional|standard[- ]of[- ]care|routine (?:clinical )?(?:protocol|sequence)", blob, re.I):
        return "Conventional/standard-of-care acquisition"
    return "Not stated"


BENCH = r"fastMRI|\bBraTS\b|\bIXI\b|\bHCP\b|Human Connectome|\bOASIS\b|\bADNI\b|\bCamCAN\b|\bUK Biobank\b|M4Raw|SKM-TEA|Calgary-?Campinas"

char_rows, supp_rows = [], []
for rec in corpus:
    c = rec["csv"]
    reader = rec["is_reader_study"]
    # Text sufficiency: some records carry a stub or intro-only body without the
    # "unavailable" banner, so grade the basis by extent rather than presence.
    if rec["ft_chars"] >= 10000:
        basis = "full text"
    elif rec["ft_chars"] > 500:
        basis = "partial full text (truncated)"
    else:
        basis = "abstract + MeSH only"
    blob = " ".join([rec["abstract"], rec.get("fulltext", "")])
    bench = sorted(set(m.group(0) for m in re.finditer(BENCH, blob, re.I)))

    design = "Diagnostic accuracy / reader study" if reader else "Algorithmic / methodological reconstruction study"
    q = quadas.get(rec["key"])
    if q and q.get("design"):
        design_detail = q["design"]
    else:
        design_detail = ""

    char_rows.append({
        "study_key": rec["key"],
        "pmid": c["pmid"],
        "doi": c["doi"],
        "year": c["year"],
        "journal": c["journal"],
        "title": c["title"],
        "study_design": design,
        "method_family": c["method_family"],
        "evaluation": c["evaluation"],
        "failure_modes": c["failure_modes"],
        "field_strength": rec["field_strength"],
        "field_strength_evidence": rec["field_strength_evidence"],
        "pulse_sequences": rec["pulse_sequences"],
        # NOTE: no rq_mapping column. Keyword assignment could not reproduce the
        # paper's RQ1/RQ2/RQ3 split (123/83/40) at any defensible threshold, so
        # releasing a heuristic column here would imply support the data does not give.
        "reference_standard": reference_standard(rec),
        "public_dataset_or_benchmark": ";".join(bench),
        "code_available": "yes" if rec["code_available"] else "not stated",
        "full_text_basis": basis,
        "source_record": rec["file"],
    })

    row = {
        "study_key": rec["key"],
        "pmid": c["pmid"],
        "doi": c["doi"],
        "year": c["year"],
        "title": c["title"],
        "study_design": design,
        "design_detail": design_detail,
        "appraisal_instrument": "QUADAS-2" if reader else "Reproducibility & robustness checklist",
        "appraisal_basis": basis,
        "n_readers": (q or {}).get("n_readers", "") if reader else "",
        "n_subjects": (q or {}).get("n_subjects", "") if reader else "",
        # Flags studies the keyword classifier placed in the reader subset although the
        # appraisal found no human reader - i.e. false positives in the n=36 denominator.
        "reader_subset_verified": ("no human readers found at appraisal"
                                   if reader and not (q or {}).get("n_readers") else
                                   "yes" if reader else ""),
    }
    # QUADAS-2 domains (blank for the algorithmic subset - instrument does not apply)
    for dom, label in [("patient_selection", "rob_patient_selection"),
                       ("index_test", "rob_index_test"),
                       ("reference_standard", "rob_reference_standard"),
                       ("flow_timing", "rob_flow_timing"),
                       ("app_patient_selection", "app_patient_selection"),
                       ("app_index_test", "app_index_test"),
                       ("app_reference_standard", "app_reference_standard")]:
        d = (q or {}).get(dom) or {}
        row[label] = d.get("rating", "") if reader else "n/a"
        row[label + "_evidence"] = (d.get("evidence", "") if reader else "")
        row[label + "_rationale"] = (d.get("rationale", "") if reader else "")

    # reproducibility / robustness appraisal - applies to every study
    row.update({
        "repro_code_available": "yes" if rec["code_available"] else "not stated",
        "repro_code_evidence": rec["code_evidence"],
        "repro_public_dataset": "yes" if rec["public_dataset"] else "not stated",
        "repro_dataset_evidence": rec["dataset_evidence"],
        "repro_benchmark": ";".join(bench),
        "repro_reference_standard": reference_standard(rec),
        "repro_sampling": ("prospective" if rec["prospective"] and not rec["retrospective"]
                           else "retrospective" if rec["retrospective"] and not rec["prospective"]
                           else "both stated" if rec["prospective"] and rec["retrospective"]
                           else "not stated"),
        "repro_centres": ("multi-centre" if rec["multicentre"] and not rec["singlecentre"]
                          else "single-centre" if rec["singlecentre"] and not rec["multicentre"]
                          else "both stated" if rec["multicentre"] and rec["singlecentre"]
                          else "not stated"),
        "repro_sampling_evidence": rec["sampling_evidence"],
        "repro_ethics_stated": "yes" if rec["ethics_stated"] else "not stated",
        "rater_status": "pending_reviewer_verification",
        "reviewer_1": "",
        "reviewer_2": "",
        "consensus_note": "",
    })
    supp_rows.append(row)

DEST.mkdir(exist_ok=True)
for name, rows in [("included_characteristics.csv", char_rows),
                   ("included_characteristics_supplement.csv", supp_rows)]:
    p = DEST / name
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {p.name}: {len(rows)} rows x {len(rows[0])} cols")

# ---------------- verification against the paper ----------------
print("\n" + "=" * 66)
print("VERIFICATION AGAINST brain_ieeetmi_v6.tex")
print("=" * 66)


def cnt(rows, col, multi=True):
    c = collections.Counter()
    for r in rows:
        vals = (r[col] or "").split(";") if multi else [r[col] or ""]
        for v in vals:
            if v.strip():
                c[v.strip()] += 1
    return c


checks = []


def chk(label, got, want):
    ok = got == want
    checks.append(ok)
    print(f"  {'OK ' if ok else 'DIFF'}  {label}: got {got}, paper says {want}")


print("\n-- carried through unchanged (must match) --")
mf = cnt(char_rows, "method_family")
for k, want in [("Compressed sensing / parallel imaging", 73), ("Generative (GAN/diffusion/VAE)", 58),
                ("Motion correction", 46), ("Physics-based / unrolled", 30), ("Denoising", 24),
                ("Super-resolution", 12), ("Self-supervised / unsupervised", 11)]:
    chk(f"method {k[:34]}", mf[k], want)
ev = cnt(char_rows, "evaluation")
for k, want in [("Pixel-wise metrics (PSNR/SSIM/NRMSE)", 45), ("Observer / reader study", 36),
                ("Uncertainty estimation", 15), ("Perceptual / learned metrics", 11)]:
    chk(f"eval {k[:38]}", ev[k], want)

print("\n-- newly derived (report honestly) --")
fs = cnt(char_rows, "field_strength", multi=False)
for k, want in [("3T", 112), ("1.5T", 48), ("7T", 18), ("not reported", 7)]:
    chk(f"field strength {k}", fs[k], want)
sq = cnt(char_rows, "pulse_sequences")
for k, want in [("T1w", 94), ("T2w", 78), ("FLAIR", 42), ("DWI", 38), ("SWI", 24)]:
    chk(f"sequence {k}", sq[k], want)
dz = cnt(char_rows, "study_design", multi=False)
chk("design: algorithmic", dz["Algorithmic / methodological reconstruction study"], 149)
chk("design: reader/diagnostic", dz["Diagnostic accuracy / reader study"], 36)
print("  ..    RQ mapping: column omitted - paper's 123/83/40 split is not reproducible "
      "from the extracted data at any defensible keyword threshold")

print("\n-- QUADAS-2 (n=36) --")
paper_q = {"rob_patient_selection": (26, 7, 3), "rob_index_test": (29, 5, 2),
           "rob_reference_standard": (31, 4, 1), "rob_flow_timing": (32, 3, 1)}
readers = [r for r in supp_rows if r["appraisal_instrument"] == "QUADAS-2"]
print(f"  reader/diagnostic studies: {len(readers)}")
for dom, (wl, wu, wh) in paper_q.items():
    c = collections.Counter(r[dom] for r in readers)
    got = (c["Low"], c["Unclear"], c["High"])
    ok = got == (wl, wu, wh)
    checks.append(ok)
    print(f"  {'OK ' if ok else 'DIFF'}  {dom:26s} Low/Unclear/High = {got[0]}/{got[1]}/{got[2]}   paper: {wl}/{wu}/{wh}")
for dom in ["app_patient_selection", "app_index_test", "app_reference_standard"]:
    c = collections.Counter(r[dom] for r in readers)
    pct = 100 * c["Low"] / max(1, len(readers))
    print(f"  ..    {dom:26s} Low={c['Low']} ({pct:.1f}%)  Unclear={c['Unclear']} High={c['High']}  (paper: >85% Low)")

print(f"\n  {sum(checks)}/{len(checks)} checks match the paper")
json.dump({"char": char_rows, "supp": supp_rows}, open(OUT / "assembled.json", "w", encoding="utf-8"), indent=1)
