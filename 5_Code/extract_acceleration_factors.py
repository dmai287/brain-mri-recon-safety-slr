"""Evidence-linked extraction of evaluated acceleration factors from the 264 included full texts.

Per study: every candidate acceleration factor with a verbatim context quote, with
reference-list and citation-context matches filtered out and reference-acquisition
parallel-imaging factors flagged separately.
"""
import os, re, glob, io, csv
from collections import Counter

ROOT = r"C:\Users\V133280\RMIT University\Thai Pham - StrokeVault\Brain MRI Reconstruction Safety Review - Broad"
INC = os.path.join(ROOT, "Full Text Screening", "Include")
CSVP = os.path.join(ROOT, "Registration", "OSF_Upload", "3_Included_Studies", "included_characteristics.csv")
OUT = os.path.dirname(os.path.abspath(__file__))

rows = list(csv.DictReader(io.open(CSVP, encoding="utf-8-sig")))
by_pmid = {(r["pmid"] or "").strip(): r for r in rows if (r["pmid"] or "").strip()}
norm = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
by_title = {norm(r["title"])[:55]: r for r in rows}

PATS = [
    ("accel_factor", re.compile(r"\b(?:acceleration|undersampling|under-sampling|reduction)\s+factors?\s*(?:of|=|:|\s)\s*([0-9]{1,2}(?:\.[0-9])?)(?![0-9])", re.I)),
    ("R_equals",     re.compile(r"\bR\s*(?:=|\u00bc)\s*([0-9]{1,2}(?:\.[0-9])?)(?![0-9])")),
    ("fold",         re.compile(r"\b([0-9]{1,2}(?:\.[0-9])?)(?![0-9])\s*(?:x|X|\u00d7|-fold|\s*fold)[\s-]*(?:acceleration|undersampl|accelerated|retrospectiv)", re.I)),
    ("accel_of",     re.compile(r"\bacceleration\s+of\s+([0-9]{1,2}(?:\.[0-9])?)(?![0-9])", re.I)),
]

CITE = re.compile(r"(et al\.|doi|PMID|vol\.|pp\.\s*[0-9]|;\s*[0-9]{1,3}\s*\([0-9]+\)\s*:|\[[0-9]{1,3}\]\s*[A-Z][a-z]+,|[A-Z]\.\s*[A-Z]?\.?,|\(\s*(?:19|20)[0-9]{2}\s*\)\.)", re.I)
PI_REF = re.compile(r"\b(GRAPPA|SENSE|ASSET|CAIPI|iPAT|mSENSE|SPEEDER)\b", re.I)
TEST = re.compile(r"\b(retrospectiv|prospectiv|undersampl|under-sampl|reconstruct|accelerat|k-?space|propos|evaluat|compar|train|test)\w*", re.I)

REFHEAD = re.compile(r"^\s*#{0,4}\s*(references|bibliography|reference list)\s*:?\s*$", re.I | re.M)
CITEHEAD = re.compile(r"^#{1,4}\s*Citation\s*$", re.M)
NEXTHEAD = re.compile(r"^#{1,4}\s+", re.M)


def clean(t):
    """remove the Citation block; cut the trailing reference list (only after the body starts)"""
    m = CITEHEAD.search(t)
    if m:
        nxt = NEXTHEAD.search(t, m.end())
        t = t[:m.start()] + (t[nxt.start():] if nxt else "")
    body = t.find("Full-Text Content")
    start = body if body > 0 else 0
    cuts = [mm.start() for mm in REFHEAD.finditer(t) if mm.start() > start + 500]
    if cuts:
        t = t[:max(cuts)]
    return t


records = []
matched_files = 0
for f in sorted(glob.glob(os.path.join(INC, "*.md"))):
    raw = io.open(f, encoding="utf-8", errors="replace").read()
    t = clean(raw)
    mm = re.search(r"PMID[ _]?(\d+)", os.path.basename(f))
    rec = by_pmid.get(mm.group(1)) if mm else None
    if rec is None:
        k = norm(os.path.basename(f))
        rec = next((v for kk, v in by_title.items() if kk and kk[:38] in k), None)
    if rec is None:
        continue
    matched_files += 1
    seen = set()
    for pname, p in PATS:
        for m in p.finditer(t):
            try:
                v = float(m.group(1))
            except ValueError:
                continue
            if not (1.0 < v <= 30.0):
                continue
            a, b = max(0, m.start() - 130), min(len(t), m.end() + 90)
            snip = re.sub(r"\s+", " ", t[a:b]).strip()
            before = re.sub(r"\s+", " ", t[max(0, m.start() - 130):m.start()])
            after20 = t[m.end():m.end() + 22]
            supcite = bool(re.search(r"^\s*\)?\s*[.,]?\s*\d{1,2}\s+[A-Za-z]", after20))
            key = (v, snip[:60])
            if key in seen:
                continue
            seen.add(key)
            records.append({
                "study_key": rec["study_key"], "pmid": rec["pmid"], "year": rec["year"],
                "title": rec["title"][:110], "pattern": pname, "R": v,
                "citation_context": "yes" if (CITE.search(before) or supcite) else "no",
                "parallel_imaging_context": "yes" if PI_REF.search(snip) else "no",
                "test_context": "yes" if TEST.search(snip) else "no",
                "quote": snip[:300],
            })

print("files matched to a study:", matched_files)
print("raw candidate matches:", len(records), "across", len({r['study_key'] for r in records}), "studies")
print("  citation context:", sum(1 for r in records if r["citation_context"] == "yes"))
print("  parallel-imaging context:", sum(1 for r in records if r["parallel_imaging_context"] == "yes"))
print("  no test context:", sum(1 for r in records if r["test_context"] == "no"))

with io.open(os.path.join(OUT, "accel_candidates.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(records[0].keys()))
    w.writeheader()
    w.writerows(records)

kept = [r for r in records if r["citation_context"] == "no" and r["test_context"] == "yes"]
print("\nAFTER FILTER:", len(kept), "matches across", len({r['study_key'] for r in kept}), "studies")
print("R distribution (studies, by max R):")
mx = {}
for r in kept:
    mx[r["study_key"]] = max(mx.get(r["study_key"], 0), r["R"])
print("  ", dict(sorted(Counter(mx.values()).items())))
