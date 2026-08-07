#!/usr/bin/env python3
"""Stage 1: build the per-study working record set for the characteristics + appraisal files.

Reads the 185 Include records (title/abstract/MeSH/full text), joins them to the existing
characteristics CSV, extracts deterministic signals with verbatim evidence, and writes:
  corpus.json          - all 185 records with text + deterministic signals
  quadas_subset.json   - the 36 observer/reader studies needing QUADAS-2 appraisal
  fulltext/<key>.txt   - per-study text for subagent appraisal
"""
import csv, json, re, collections
from pathlib import Path

REVIEW = Path(r"C:\Users\V133280\RMIT University\Thai Pham - StrokeVault\Brain MRI Reconstruction Safety Review - Broad")
INC = REVIEW / "Full Text Screening" / "Include"
# The original per-study characteristics file (now released as included_characteristics.csv;
# the supplement name was reassigned to the appraisal file it is cited as in the paper).
CSV_IN = REVIEW / "LaTex PDF" / "included_characteristics_supplement.csv.orig-backup"
OUT = Path(__file__).parent
FT = OUT / "fulltext"
FT.mkdir(exist_ok=True)


def parse(md: Path):
    t = md.read_text(encoding="utf-8", errors="replace")

    def sec(name):
        # Stop only at KNOWN section headers: PDF-embedded full text may itself
        # contain markdown "## " headings, which must not terminate the section.
        known = ("Authors|Abstract|Citation|MeSH Terms|Full-Text Content|"
                 "Abstract Screening Decision|Full-Text Screening Decision")
        m = re.search(rf"^## {name}\s*\n(.*?)(?=^## (?:{known})\s*$|\Z)", t, re.S | re.M)
        return m.group(1).strip() if m else ""

    fm = {}
    m = re.match(r"\s*---\s*\n(.*?)\n---", t, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    body = sec("Full-Text Content")
    unavailable = bool(re.search(r"^_?Full text unavailable", body[:200], re.I | re.M))
    return {
        "doi": fm.get("doi", "").lower(),
        "pmid": fm.get("pmid", ""),
        "title": fm.get("title", ""),
        "journal": fm.get("journal", ""),
        "year": fm.get("year", ""),
        "abstract": sec("Abstract"),
        "mesh": sec("MeSH Terms"),
        "pubtypes": fm.get("publication_types", ""),
        "fulltext": "" if unavailable else body,
        "ft_chars": 0 if unavailable else len(body),
        "file": md.name,
    }


# ---------- deterministic signal extraction, each with verbatim evidence ----------
def evidence(text, pattern, window=140):
    """Return the first matching snippet as verbatim evidence, or ''."""
    m = re.search(pattern, text, re.I)
    if not m:
        return ""
    s = max(0, m.start() - window // 2)
    snip = text[s:m.end() + window // 2].replace("\n", " ")
    return re.sub(r"\s+", " ", snip).strip()


FIELD = {
    "7T": r"\b7(\.0)?\s*-?\s*(T\b|Tesla)",
    "3T": r"\b3(\.0)?\s*-?\s*(T\b|Tesla)",
    "1.5T": r"\b1\.5\s*-?\s*(T\b|Tesla)",
}
SEQ = {
    "T1w": r"\bT1[-\s]?w(eighted)?\b|\bMPRAGE\b|\bMP-?RAGE\b",
    "T2w": r"\bT2[-\s]?w(eighted)?\b(?![*\u2217])",
    "FLAIR": r"\bFLAIR\b|fluid[-\s]attenuated inversion",
    "DWI": r"\bDWI\b|diffusion[-\s]weighted|\bADC\b map",
    "SWI": r"\bSWI\b|susceptibility[-\s]weighted|\bT2\*|\bT2-?star",
}
CODE = r"github\.com/\S+|gitlab\.com/\S+|zenodo\.\S+|code (?:is )?(?:publicly )?available|open[-\s]source|our code|codebase is"
DATA_PUBLIC = r"fastMRI|\bHCP\b|Human Connectome|\bIXI\b|\bBraTS\b|\bOASIS\b|\bADNI\b|\bCamCAN\b|\bUK Biobank\b|publicly available (?:data|dataset)|open[-\s]access dataset"
PROSPECTIVE = r"\bprospectiv"
RETROSPECTIVE = r"\bretrospectiv"
MULTICENTRE = r"multi-?cent(er|re)|multiple (?:institutions|centers|centres|sites)|\bmulti-?site\b"
SINGLECENTRE = r"single-?cent(er|re)|single institution|our institution|one center"
IRB = r"\bIRB\b|institutional review board|ethics (?:committee|approval)|informed consent"


def signals(rec):
    blob = " ".join([rec["title"], rec["abstract"], rec["mesh"], rec["fulltext"]])
    ta = " ".join([rec["title"], rec["abstract"], rec["mesh"]])  # title/abstract/MeSH scope

    # field strength: single-label, most-mentioned wins (full text preferred, TA fallback)
    src = blob if rec["ft_chars"] > 500 else ta
    counts = {k: len(re.findall(p, src, re.I)) for k, p in FIELD.items()}
    fs = max(counts, key=counts.get) if any(counts.values()) else "not reported"
    seqs = [k for k, p in SEQ.items() if re.search(p, src, re.I)]

    return {
        "field_strength": fs,
        "field_strength_evidence": evidence(src, FIELD[fs]) if fs != "not reported" else "",
        "field_strength_mentions": counts,
        "pulse_sequences": ";".join(seqs),
        "code_available": bool(re.search(CODE, blob, re.I)),
        "code_evidence": evidence(blob, CODE),
        "public_dataset": bool(re.search(DATA_PUBLIC, blob, re.I)),
        "dataset_evidence": evidence(blob, DATA_PUBLIC),
        "prospective": bool(re.search(PROSPECTIVE, blob, re.I)),
        "retrospective": bool(re.search(RETROSPECTIVE, blob, re.I)),
        "multicentre": bool(re.search(MULTICENTRE, blob, re.I)),
        "singlecentre": bool(re.search(SINGLECENTRE, blob, re.I)),
        "sampling_evidence": evidence(blob, MULTICENTRE) or evidence(blob, SINGLECENTRE) or evidence(blob, RETROSPECTIVE),
        "ethics_stated": bool(re.search(IRB, blob, re.I)),
    }


recs = {}
for p in sorted(INC.glob("*.md")):
    r = parse(p)
    recs[r["doi"]] = r

rows = list(csv.DictReader(open(CSV_IN, encoding="utf-8")))
corpus = []
for i, row in enumerate(rows):
    rec = recs[row["doi"].lower()]
    key = f"S{i+1:03d}"
    rec["key"] = key
    rec.update(signals(rec))
    rec["csv"] = row
    rec["is_reader_study"] = "Observer" in (row["evaluation"] or "")
    corpus.append(rec)
    if rec["ft_chars"] > 500:
        (FT / f"{key}.txt").write_text(
            f"KEY: {key}\nTITLE: {rec['title']}\nJOURNAL: {rec['journal']} ({rec['year']})\nDOI: {rec['doi']}\n\n"
            f"ABSTRACT:\n{rec['abstract']}\n\nFULL TEXT:\n{rec['fulltext']}",
            encoding="utf-8")

json.dump(corpus, open(OUT / "corpus.json", "w", encoding="utf-8"), indent=1)
quadas = [{"key": r["key"], "title": r["title"], "year": r["year"], "journal": r["journal"],
           "doi": r["doi"], "ft_chars": r["ft_chars"]} for r in corpus if r["is_reader_study"]]
json.dump(quadas, open(OUT / "quadas_subset.json", "w", encoding="utf-8"), indent=1)

print(f"corpus: {len(corpus)}  full-text files written: {len(list(FT.glob('*.txt')))}")
print(f"QUADAS-2 subset (observer/reader): {len(quadas)}; with full text: {sum(1 for q in quadas if q['ft_chars']>500)}")
print("\nfield strength:", collections.Counter(r["field_strength"] for r in corpus))
print("  paper claims: 3T=112, 1.5T=48, 7T=18, not reported=7")
sq = collections.Counter()
for r in corpus:
    for s in r["pulse_sequences"].split(";"):
        if s:
            sq[s] += 1
print("sequences:", dict(sq), "total labels", sum(sq.values()))
print("  paper claims: T1w=94 T2w=78 FLAIR=42 DWI=38 SWI=24, 276 labels")
print("\ncode available:", sum(r["code_available"] for r in corpus),
      "| public dataset:", sum(r["public_dataset"] for r in corpus),
      "| retrospective:", sum(r["retrospective"] for r in corpus),
      "| multicentre:", sum(r["multicentre"] for r in corpus))
