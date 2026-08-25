# -*- coding: utf-8 -*-
"""Release the derived venue-community classification used in Results 4.3."""
import pathlib
import pandas as pd

ROOT = pathlib.Path(r"C:\Users\V133280\RMIT University\Thai Pham - StrokeVault"
                    r"\Brain MRI Reconstruction Safety Review - Broad")
SRC = ROOT / "Registration/OSF_Upload/3_Included_Studies/included_characteristics.csv"
df = pd.read_csv(SRC)

ENG = ["ieee", "medical image analysis", "medical physics", "miccai", "isbi", "arxiv",
       "proceedings", "conference", "symposium", "workshop", "pattern recognition",
       "computer methods", "computerized medical imaging", "physics in medicine",
       "machine learning", "signal processing", "biomedical engineering", "access",
       "sensors", "informatics", "shape in medical imaging", "neural networks"]
CLIN = ["radiolog", "ajnr", "jmri", "magnetic resonance in medicine",
        "magnetic resonance imaging", "nmr in biomedicine", "magma",
        "magnetic resonance materials", "clinical", "tomography", "european journal of",
        "japanese journal", "korean journal", "investigative", "academic radiology",
        "stroke", "neurosurg", "medicine", "diagnostics", "cancers", "abdominal",
        "pediatric radiology", "zeitschrift", "nihon", "mrms",
        "magnetic resonance in medical sciences", "quantitative imaging"]
GEN = ["neuroimage", "scientific reports", "plos", "nature", "bmc", "frontiers",
       "human brain mapping", "elife", "communications", "heliyon", "peerj",
       "neuroinformatics", "biomtc", "biometrics"]


def vclass(j):
    s = str(j).lower()
    if any(k in s for k in ENG):
        return "engineering_methods"
    if any(k in s for k in GEN):
        return "general_neuroscience"
    if any(k in s for k in CLIN):
        return "clinical_imaging"
    return "unclassified"


out = df[["study_key", "pmid", "doi", "year", "journal"]].copy()
out["venue_community"] = df["journal"].map(vclass)
out["rule"] = "keyword match on journal title; see 5_Code/venue_classification.py"

for pkg in ["Registration/OSF_Upload", "github_repo"]:
    dest = ROOT / pkg / "3_Included_Studies" / "venue_community_classification.csv"
    out.to_csv(dest, index=False)
    print("wrote", dest.relative_to(ROOT))

# release the rules themselves as code
code = pathlib.Path(__file__).read_text(encoding="utf-8")
for pkg in ["Registration/OSF_Upload", "github_repo"]:
    dest = ROOT / pkg / "5_Code" / "venue_classification.py"
    dest.write_text(code, encoding="utf-8")
    print("wrote", dest.relative_to(ROOT))

print()
print(out["venue_community"].value_counts().to_string())
