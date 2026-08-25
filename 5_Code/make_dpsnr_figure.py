"""
Sensitivity analysis for the aggregate PSNR penalty caused by degrading a
focal lesion region, per Eq. (2) of the manuscript:

    |Delta PSNR| = 10 * log10( 1 + f * (r - 1) )   [dB]

where
    f = V_lesion / V_total                      (lesion volume fraction)
    r = MSE_lesion / MSE_bg                     (lesion-to-background error ratio)

This is an identity, not a bound: the expression is monotonically increasing
and unbounded in r. The figure is therefore a sensitivity map over (f, r),
not a proof that any fixed decibel value bounds the effect.

Dependencies: numpy >= 1.20, matplotlib >= 3.4
Run:  python dpsnr_sensitivity.py
Out:  dpsnr_sensitivity.pdf  (and .png)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatterMathtext

# ---------------------------------------------------------------- parameters
F_MIN, F_MAX = 1e-6, 1e-3      # lesion volume fraction
R_MIN, R_MAX = 1.0, 1000.0     # lesion-to-background MSE ratio
N = 600

BRAIN_VOLUME_MM3 = 1.2e6       # ~1200 mL, adult brain

# Clinically anchored lesion fractions, stated so the reader can check them.
LESION_ANCHORS = {
    "punctate infarct\n(5 mm$^3$)":        5.0    / BRAIN_VOLUME_MM3,
    "cerebral microbleed\n(~14 mm$^3$, 3 mm)": (4/3)*np.pi*1.5**3 / BRAIN_VOLUME_MM3,
    "lacunar infarct\n(~500 mm$^3$)":      500.0  / BRAIN_VOLUME_MM3,
}


def delta_psnr(f, r):
    """Magnitude of aggregate PSNR change, in dB. Eq. (2)."""
    return 10.0 * np.log10(1.0 + f * (r - 1.0))


def main():
    f = np.logspace(np.log10(F_MIN), np.log10(F_MAX), N)
    r = np.logspace(np.log10(R_MIN + 1e-9), np.log10(R_MAX), N)
    F, R = np.meshgrid(f, r, indexing="ij")
    Z = delta_psnr(F, R)

    fig, ax = plt.subplots(figsize=(6.0, 4.4), constrained_layout=True)

    levels = np.logspace(-5, 0.5, 45)
    cf = ax.contourf(F, R, Z, levels=levels, norm="log", cmap="viridis", extend="both")

    # Reference contours at decibel values people actually quote.
    for lv, ls in [(0.001, ":"), (0.01, "--"), (0.1, "-."), (0.5, "-")]:
        cs = ax.contour(F, R, Z, levels=[lv], colors="white", linewidths=1.2,
                        linestyles=ls)
        ax.clabel(cs, fmt={lv: f"{lv} dB"}, fontsize=8, inline=True)

    # Clinically relevant band.
    ax.axvspan(LESION_ANCHORS["punctate infarct\n(5 mm$^3$)"], 1e-3,
               color="white", alpha=0.10, zorder=1)

    for label, fv in LESION_ANCHORS.items():
        if F_MIN <= fv <= F_MAX:
            ax.axvline(fv, color="crimson", lw=1.0, alpha=0.85)
            ax.text(fv, R_MAX * 0.62, label, rotation=90, fontsize=6.5,
                    color="crimson", ha="right", va="top")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"lesion volume fraction  $f = V_{\mathrm{lesion}}/V_{\mathrm{total}}$")
    ax.set_ylabel(r"error ratio  $r = \mathrm{MSE}_{\mathrm{lesion}}/\mathrm{MSE}_{\mathrm{bg}}$")
    ax.set_title(r"$|\Delta\mathrm{PSNR}| = 10\log_{10}(1 + f(r-1))$  [dB]", fontsize=10)

    cb = fig.colorbar(cf, ax=ax, format=LogFormatterMathtext())
    cb.set_label(r"$|\Delta\mathrm{PSNR}|$  (dB)")

    fig.savefig("dpsnr_sensitivity.pdf")
    fig.savefig("dpsnr_sensitivity.png", dpi=220)

    # ------------------------------------------------------ reported values
    print("Values quoted in the manuscript text:\n")
    checks = [
        ("previously quoted operating point", 5e-4, 86.0),
        ("5 mm^3 punctate infarct, complete erasure", 5.0 / BRAIN_VOLUME_MM3, 628.0),
        ("5 mm^3 punctate infarct, r = 86", 5.0 / BRAIN_VOLUME_MM3, 86.0),
        ("3 mm microbleed, complete erasure", (4/3)*np.pi*1.5**3 / BRAIN_VOLUME_MM3, 628.0),
        ("500 mm^3 lacunar infarct, complete erasure", 500.0 / BRAIN_VOLUME_MM3, 628.0),
        ("f = 5e-4, r = 628", 5e-4, 628.0),
    ]
    for name, fv, rv in checks:
        print(f"  f = {fv:9.3e}, r = {rv:6.1f}  ->  |dPSNR| = {delta_psnr(fv, rv):8.5f} dB   ({name})")


if __name__ == "__main__":
    main()
