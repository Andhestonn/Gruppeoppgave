"""Medlem 1: del d og e."""
from datetime import datetime
from les_data import periode, velg_aar


def skidager(data, aar):
    dager = periode(data, datetime(aar - 1, 11, 1), datetime(aar, 5, 31))
    antall = sum(d["sno"] is not None and d["sno"] >= 20 for d in dager)
    mangler = sum(d["sno"] is None for d in dager)
    return antall, mangler, len(dager)


def plott_aar(data, aar, lagre=None, vis=True):
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    dager = velg_aar(data, aar)
    datoer = [d["dato"] for d in dager]
    fig, akser = plt.subplots(4, 1, figsize=(11, 10), sharex=True)
    felt = [("sno", "Snødybde (cm)"), ("nedbor", "Nedbør (mm)"),
            ("temperatur", "Middeltemperatur (°C)"), ("vind", "Høyeste middelvind (m/s)")]
    for akse, (navn, etikett) in zip(akser, felt):
        verdier = [float("nan") if d[navn] is None else d[navn] for d in dager]
        akse.plot(datoer, verdier, linewidth=0.9)
        akse.set_ylabel(etikett)
        akse.grid(alpha=0.25)
        mangler = sum(d[navn] is None for d in dager)
        akse.set_title(f"{mangler} dager uten måling", fontsize=9, loc="right")
    akser[-1].xaxis.set_major_locator(mdates.MonthLocator())
    akser[-1].xaxis.set_major_formatter(mdates.DateFormatter("%d.%m"))
    fig.suptitle(f"Sinnes – {aar}")
    fig.tight_layout()
    if lagre:
        fig.savefig(lagre, dpi=150)
    if vis:
        plt.show()
    plt.close(fig)
