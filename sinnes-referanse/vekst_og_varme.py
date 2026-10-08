"""Medlem 2: del f og h. Del i gjennomgås sammen."""
from datetime import datetime
from les_data import velg_aar


def plantevekst(data, aar):
    dager = velg_aar(data, aar)
    mangler = sum(d["temperatur"] is None for d in dager)
    total = sum(max(d["temperatur"] - 5, 0) for d in dager if d["temperatur"] is not None)
    return total, mangler


def varme_dager(data, aar):
    dager = velg_aar(data, aar)
    antall = [sum(d["maks"] is not None and d["maks"] > grense for d in dager)
              for grense in (20, 25, 30)]
    return antall, sum(d["maks"] is None for d in dager)


def dagsvekst(temperatur):
    if temperatur < 0:
        return temperatur
    return max(temperatur - 5, 0)


def vekst_fra_start(dager, start):
    """Største akkumulerte vekst fra start; fri sluttdato innen året."""
    total = 0.0
    beste = 0.0
    sluttdato = None  # Null vekst før første døgn er et tillatt utgangspunkt.
    for dag in dager:
        if dag["dato"] >= start:
            total += dagsvekst(dag["temperatur"])
            if total > beste:
                beste = total
                sluttdato = dag["dato"]
    return beste, sluttdato, total


def avansert_vekst(data, aar):
    dager = velg_aar(data, aar)
    if any(d["temperatur"] is None for d in dager):
        raise ValueError("Del i krever temperatur for alle dager i året.")
    april = vekst_fra_start(dager, datetime(aar, 4, 1))
    beste = (0.0, dager[0]["dato"], None)
    beste_ved_aarslutt = (float("-inf"), dager[0]["dato"])
    # En enkel dobbel løkke er lett å forstå og liten nok for 365/366 dager.
    for dag in dager:
        maksimum, slutt, total = vekst_fra_start(dager, dag["dato"])
        if maksimum > beste[0]:
            beste = (maksimum, dag["dato"], slutt)
        if total > beste_ved_aarslutt[0]:
            beste_ved_aarslutt = (total, dag["dato"])
    return april, beste, beste_ved_aarslutt
