#!/usr/bin/env python3
"""Reconcile the independent QUADAS-2 rating worksheets.

  Stage 1  python merge_reviewers.py            -> agreement stats + disagreements.csv
  Stage 2  fill the 'consensus' column in disagreements.csv, then:
           python merge_reviewers.py --apply --r1 "Name" --r2 "Name" --r3 "Name"
           -> writes the agreed ratings into included_characteristics_supplement.csv
              and flips rater_status to 'verified'

Reads every ``reviewer_worksheet_R*.csv`` present, so it handles two reviewers or three.
A domain is unanimous when all reviewers who rated it gave the same label; anything else is
a disagreement and goes to ``disagreements.csv`` for resolution.

On inter-rater reliability: a chance-corrected coefficient is only meaningful when there is
some spread in the ratings. If agreement is unanimous, kappa is degenerate (expected agreement
is 1, so the coefficient is undefined or trivially 1.00) and should NOT be quoted as evidence
of reliability. This script reports the raw agreement and computes kappa only where the ratings
actually vary; where they do not, it says so instead of printing a number.
"""
import argparse
import csv
import datetime as dt
import itertools
import re
import shutil
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent

DOMAINS = ["rob_patient_selection", "rob_index_test", "rob_reference_standard", "rob_flow_timing",
           "app_patient_selection", "app_index_test", "app_reference_standard"]
VALID = {"Low", "High", "Unclear"}


def find_supplement():
    """Locate the supplement in either the deposit layout or the working review tree."""
    candidates = [
        HERE.parents[1] / "3_Included_Studies" / "included_characteristics_supplement.csv",
        HERE.parents[2] / "LaTex PDF" / "included_characteristics_supplement.csv",
        HERE.parents[1] / "LaTex PDF" / "included_characteristics_supplement.csv",
    ]
    for c in candidates:
        if c.exists():
            return c
    raise SystemExit("could not locate included_characteristics_supplement.csv; looked in:\n  "
                     + "\n  ".join(str(c) for c in candidates))


def load(p):
    return {r["study_key"]: r for r in csv.DictReader(open(p, encoding="utf-8"))}


def kappa(pairs):
    """Cohen's kappa for (a, b) label pairs. None when expected agreement is 1 (degenerate)."""
    n = len(pairs)
    if not n:
        return None
    po = sum(1 for a, b in pairs if a == b) / n
    c1, c2 = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum((c1[k] / n) * (c2[k] / n) for k in set(c1) | set(c2))
    return None if pe >= 1.0 else (po - pe) / (1 - pe)


def interpret(k):
    if k is None:
        return "degenerate - no spread in ratings; do not quote"
    for t, lab in ((0.81, "almost perfect"), (0.61, "substantial"), (0.41, "moderate"),
                   (0.21, "fair"), (0.0, "slight")):
        if k >= t:
            return lab
    return "poor"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write consensus into the supplement")
    ap.add_argument("--r1", default="")
    ap.add_argument("--r2", default="")
    ap.add_argument("--r3", default="")
    ap.add_argument("--adjudicator", default="")
    a = ap.parse_args()

    sheets = sorted(HERE.glob("reviewer_worksheet_R*.csv"),
                    key=lambda p: int(re.search(r"R(\d+)", p.name).group(1)))
    if len(sheets) < 2:
        raise SystemExit(f"need at least two worksheets; found {len(sheets)} in {HERE}")
    R = [load(p) for p in sheets]
    labels = [re.search(r"(R\d+)", p.name).group(1) for p in sheets]
    print(f"worksheets: {', '.join(p.name for p in sheets)}")

    keys = sorted(set.intersection(*(set(r) for r in R)))
    print(f"studies in common: {len(keys)}   domains: {len(DOMAINS)}   "
          f"cells: {len(keys) * len(DOMAINS)}")

    bad = [(k, d, lab, r[k][d]) for k in keys for d in DOMAINS for lab, r in zip(labels, R)
           if r[k][d].strip() and r[k][d].strip() not in VALID]
    if bad:
        print("INVALID values (must be exactly Low / High / Unclear):")
        for k, d, lab, v in bad[:12]:
            print(f"   {k} {d}: {lab}={v!r}")
        raise SystemExit(1)

    blank = sum(1 for k in keys for d in DOMAINS
                if not all(r[k][d].strip() for r in R))
    if blank:
        print(f"WARNING: {blank} domain cells are not rated by every reviewer.\n")

    print(f"\n{'domain':28s} {'unanimous':>11}  kappa (pairwise)")
    disagreements, tot_agree, tot_n = [], 0, 0
    for d in DOMAINS:
        rated = [k for k in keys if all(r[k][d].strip() for r in R)]
        if not rated:
            continue
        agree = sum(1 for k in rated if len({r[k][d].strip() for r in R}) == 1)
        tot_agree += agree
        tot_n += len(rated)
        ks = []
        for (i, ri), (j, rj) in itertools.combinations(list(enumerate(R)), 2):
            kv = kappa([(ri[k][d].strip(), rj[k][d].strip()) for k in rated])
            ks.append(f"{labels[i]}/{labels[j]}=" + ("n/a" if kv is None else f"{kv:.3f}"))
        print(f"{d:28s} {agree:4d}/{len(rated):<4d}  {'  '.join(ks)}")
        for k in rated:
            vals = {r[k][d].strip() for r in R}
            if len(vals) > 1:
                row = {"study_key": k, "domain": d}
                for lab, r in zip(labels, R):
                    row[f"{lab}_rating"] = r[k][d].strip()
                    row[f"{lab}_note"] = r[k].get(d + "_note", "")
                row.update({"consensus": "", "resolution": "", "adjudicated_by": ""})
                disagreements.append(row)

    if tot_n:
        print(f"\nunanimous on {tot_agree}/{tot_n} domain judgements "
              f"({100 * tot_agree / tot_n:.1f}%)")
        if tot_agree == tot_n:
            print("Agreement is complete. Kappa is degenerate here and must not be reported as "
                  "a reliability statistic — state complete agreement and say why.")
    print(f"disagreements to resolve: {len(disagreements)}")

    dis_path = HERE / "disagreements.csv"
    if not a.apply:
        fields = (list(disagreements[0].keys()) if disagreements else
                  ["study_key", "domain"] + [f"{l}_{s}" for l in labels for s in ("rating", "note")]
                  + ["consensus", "resolution", "adjudicated_by"])
        with open(dis_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(disagreements)
        print(f"\nwrote {dis_path.name} — fill the 'consensus' column, then re-run with --apply")
        return

    # ---- apply ----
    names = [n for n in (a.r1, a.r2, a.r3) if n]
    if len(names) < len(R):
        raise SystemExit(f"--apply needs a name for each of the {len(R)} worksheets "
                         f"(--r1/--r2/--r3), for the record")

    resolved = {}
    if dis_path.exists():
        for row in csv.DictReader(open(dis_path, encoding="utf-8")):
            c = row["consensus"].strip()
            if c:
                if c not in VALID:
                    raise SystemExit(f"invalid consensus {c!r} for "
                                     f"{row['study_key']} {row['domain']}")
                resolved[(row["study_key"], row["domain"])] = c
    unresolved = [d for d in disagreements if (d["study_key"], d["domain"]) not in resolved]
    if unresolved:
        raise SystemExit(f"{len(unresolved)} disagreements still have no consensus value — "
                         f"fill them in {dis_path.name} first")

    SUP = find_supplement()
    rows = list(csv.DictReader(open(SUP, encoding="utf-8")))
    shutil.copy2(SUP, SUP.with_suffix(".csv.bak-before-signoff"))
    stamp = dt.date.today().isoformat()
    n = 0
    for r in rows:
        k = r["study_key"]
        if k not in keys or r["appraisal_instrument"] != "QUADAS-2":
            continue
        for d in DOMAINS:
            vals = [x[k][d].strip() for x in R]
            if not all(vals):
                continue
            r[d] = vals[0] if len(set(vals)) == 1 else resolved[(k, d)]
        r["rater_status"] = "verified"
        for i, name in enumerate(names, start=1):
            col = f"reviewer_{i}"
            if col in r:
                r[col] = name
        note = f"Independent rating by {len(names)} reviewers, {stamp}."
        if any((k, d) in resolved for d in DOMAINS):
            note += (" Disagreements resolved by discussion"
                     + (f"; adjudicated by {a.adjudicator}" if a.adjudicator else "") + ".")
        else:
            note += " Agreement was unanimous; no adjudication required."
        r["consensus_note"] = note
        n += 1

    with open(SUP, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\napplied consensus to {n} studies; rater_status -> verified")
    print(f"target: {SUP}")
    print(f"backup: {SUP.name}.bak-before-signoff")
    print("\nNow recompute the Table VII counts with 5_Code/assemble.py. Report a "
          "chance-corrected coefficient only if the ratings actually varied.")


if __name__ == "__main__":
    main()
