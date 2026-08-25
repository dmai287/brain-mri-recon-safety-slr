# -*- coding: utf-8 -*-
"""Rebuild Figures 3 and 4 for v26 -- layout only, plotted values unchanged.

Why this exists
---------------
Up to v25/v26 the two bar figures were included at 0.86\\textwidth and
0.84\\textwidth from natively larger canvases, so their lettering printed at
roughly 4.8 pt and 5.9 pt.  At that reduction the seven two-line category
labels of Figure 3 no longer fitted their slots and "/ parallel imaging" ran
into "Generative (GAN/diff./VAE)".

The fix is typographic only:

  * Figure 3 becomes a horizontal bar chart, so the long family names sit in
    the left margin of the axes and cannot collide with each other.
  * Both figures are emitted at exactly \\linewidth (343.5 pt) and included
    with width=\\linewidth, so nothing is rescaled and the lettering prints at
    the point sizes set here.
  * En dashes are used for the era ranges; the v18 figures carried the literal
    LaTeX source "--".

Every plotted quantity is the value already drawn in fig_*_v18.pdf, written
here as the underlying count over its denominator so it is exact:

  Figure 3   hallucination counts 14/93, 31/80, 7/57, 10/37, 9/30, 5/25, 8/17
             reader counts        24/93,  9/80, 12/57,  4/37, 6/30, 5/25, 0/17
  Figure 4   era denominators     34, 55, 174            (sum 263)
             any reader           11/34, 10/55, 36/174   (sum 57, verified subset)
             metric + reader       2/34,  4/55, 12/174   (sum 18)

Run from this directory:

    python make_figures_v26.py
"""
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))

# Manuscript \linewidth, in points.  savefig(bbox_inches="tight") trims to the
# drawn content, so the canvas width that yields exactly this is found by a
# short fixed-point iteration rather than guessed.
TARGET_PT = 343.5
START_IN = 4.77

BLUE, ORANGE, GREY = "#3B6EA5", "#D1893B", "#B8BCC2"
plt.rcParams.update({
    "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8.5,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7.5,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.linewidth": 0.7, "xtick.major.width": 0.7, "ytick.major.width": 0.7,
    "figure.dpi": 300, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
})


def _pdf_width_pt(path):
    """Width in points of a one-page PDF, read from its MediaBox."""
    data = open(path, "rb").read()
    m = re.search(rb"/MediaBox\s*\[\s*([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)",
                  data)
    return float(m.group(3)) - float(m.group(1))


def save_at_column_width(draw, name, height_in):
    """draw(fig, ax) plots the figure; save it exactly TARGET_PT wide."""
    path = os.path.join(OUT, name)
    w, got = START_IN, None
    for _ in range(6):
        fig, ax = plt.subplots(figsize=(w, height_in))
        draw(fig, ax)
        fig.savefig(path)
        plt.close(fig)
        got = _pdf_width_pt(path)
        if abs(got - TARGET_PT) < 0.5:
            break
        w *= TARGET_PT / got
    print("wrote %s: %.1f pt wide (canvas %.3f in)" % (name, got, w))


# --------------------------------------------------------------------------
# Figure 3: reader assessment against hallucination awareness, by family
# --------------------------------------------------------------------------
# (label, n, hallucination count, reader count), families in descending n.
FAMILIES = [
    ("Compressed sensing /\nparallel imaging (n=93)", 93, 14, 24),
    ("Generative (GAN/\ndiffusion/VAE) (n=80)",       80, 31,  9),
    ("Motion correction (n=57)",                      57,  7, 12),
    ("Physics-based /\nunrolled (n=37)",              37, 10,  4),
    ("Denoising (n=30)",                              30,  9,  6),
    ("Super-resolution (n=25)",                       25,  5,  5),
    ("Self-supervised /\nunsupervised (n=17)",        17,  8,  0),
]


def fig_family_evaluation(fig, ax):
    names = [f[0] for f in FAMILIES]
    hal = [100.0 * f[2] / f[1] for f in FAMILIES]
    rea = [100.0 * f[3] / f[1] for f in FAMILIES]

    y = range(len(FAMILIES))
    h = 0.36
    b1 = ax.barh([i - h / 2 for i in y], hal, h, color=ORANGE,
                 label="Records a hallucination or instability failure mode")
    b2 = ax.barh([i + h / 2 for i in y], rea, h, color=BLUE,
                 label="Carries any reader assessment")
    for bars, vals in ((b1, hal), (b2, rea)):
        for bar, v in zip(bars, vals):
            ax.text(v + 0.9, bar.get_y() + bar.get_height() / 2, "%.0f" % v,
                    ha="left", va="center", fontsize=7)
    ax.set_yticks(list(y))
    ax.set_yticklabels(names)
    ax.set_ylim(len(FAMILIES) - 0.5, -0.5)      # largest family at the top
    ax.set_xlabel("Share of family's studies (%)")
    ax.set_xlim(0, 55)
    ax.grid(axis="x", color="0.9", linewidth=0.6)
    ax.set_axisbelow(True)
    # Two long entries, so one per row and above the axes rather than over data.
    ax.legend(loc="lower left", bbox_to_anchor=(0.0, 1.01), ncol=1,
              frameon=False, handlelength=1.4, handletextpad=0.5,
              borderaxespad=0.0, labelspacing=0.35)


# --------------------------------------------------------------------------
# Figure 4: evaluation practice across publication eras
# --------------------------------------------------------------------------
# (era, n, any-reader count, metric-and-reader count)
ERAS = [
    ("1995–2019",  34, 11,  2),
    ("2020–2022",  55, 10,  4),
    ("2023–2026", 174, 36, 12),
]


def fig_practice_over_time(fig, ax):
    eras = [e[0] for e in ERAS]
    n = [e[1] for e in ERAS]
    rd = [100.0 * e[2] / e[1] for e in ERAS]
    co = [100.0 * e[3] / e[1] for e in ERAS]

    ax.bar(eras, n, color=GREY, width=0.5, label="Included studies (count)")
    for e, v in zip(eras, n):
        ax.text(e, v + 3, str(v), ha="center", va="bottom", fontsize=7.5,
                color="0.35")
    ax.set_ylabel("Included studies (count)", color="0.35")
    ax.set_ylim(0, max(n) * 1.30)
    ax.tick_params(axis="y", colors="0.35")

    ax2 = ax.twinx()
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_linewidth(0.7)
    ax2.plot(eras, rd, marker="o", markersize=4, color=BLUE, linewidth=1.6,
             label="Any reader assessment (%)")
    ax2.plot(eras, co, marker="s", markersize=4, color=ORANGE, linewidth=1.6,
             label="Metric and reader on the same data (%)")
    for e, v in zip(eras, rd):
        ax2.annotate("%.1f%%" % v, (e, v), textcoords="offset points",
                     xytext=(0, 7), ha="center", fontsize=7.5, color=BLUE)
    for e, v in zip(eras, co):
        ax2.annotate("%.1f%%" % v, (e, v), textcoords="offset points",
                     xytext=(0, -12), ha="center", fontsize=7.5, color=ORANGE)
    ax2.set_ylabel("Share of era's studies (%)")
    ax2.set_ylim(0, 42)

    # Legend above the axes so it cannot sit on the 32.4% annotation.
    hs = ax.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0]
    ls = ax.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1]
    ax.legend(hs, ls, loc="lower left", bbox_to_anchor=(0.0, 1.01), ncol=1,
              frameon=False, handlelength=1.6, handletextpad=0.5,
              borderaxespad=0.0, labelspacing=0.3)


save_at_column_width(fig_family_evaluation, "fig_family_evaluation_v26.pdf", 4.0)
save_at_column_width(fig_practice_over_time, "fig_practice_over_time_v26.pdf", 2.8)
