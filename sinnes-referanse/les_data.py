"""Felles avtale: én ordbok per kalenderdag, sortert etter dato."""
import csv
import math
from datetime import datetime, timedelta

KOLONNER = {
    "temperatur": "Middeltemperatur (døgn)",
    "maks": "Maksimumstemperatur (døgn)",
    "nedbor": "Nedbør (døgn)",
    "vind": "Høyeste middelvind (døgn)",
    "sno": "Snødybde",
}


def les_data(filnavn):
    dager = {}
    with open(filnavn, encoding="utf-8-sig", newline="") as fil:
        leser = csv.DictReader(fil, delimiter=";")
        krav = {"Stasjon", "Tid(norsk normaltid)"} | {
            navn for felt, navn in KOLONNER.items() if felt != "maks"
        }
        if not krav.issubset(leser.fieldnames or []):
            raise ValueError("CSV-fila mangler nødvendige kolonner.")
        for rad in leser:
            if not any(rad.values()) or rad.get("Navn", "").startswith("Data er gyldig per"):
                continue  # Kildemerknaden nederst er ikke en måling.
            if rad["Stasjon"] != "SN42940":
                raise ValueError("Forventet bare Sinnes, SN42940.")
            dato = datetime.strptime(rad["Tid(norsk normaltid)"], "%d.%m.%Y")
            if dato in dager:
                raise ValueError(f"Duplikatdato: {dato:%d.%m.%Y}")
            dag = {"dato": dato}
            for felt, kolonne in KOLONNER.items():
                tekst = (rad.get(kolonne) or "").strip()
                verdi = None if tekst in ("", "-") else float(tekst.replace(",", "."))
                if verdi is not None and not math.isfinite(verdi):
                    raise ValueError(f"Ugyldig måling: {dato}, {kolonne}")
                dag[felt] = verdi
            dager[dato] = dag
    return [dager[d] for d in sorted(dager)]


def periode(data, start, slutt):
    """Ta med begge endepunkter. Legg inn None hvis en hel dato mangler."""
    oppslag = {dag["dato"]: dag for dag in data}
    resultat = []
    dato = start
    while dato <= slutt:
        tom = {felt: None for felt in KOLONNER}
        resultat.append(oppslag.get(dato, {"dato": dato, **tom}))
        dato += timedelta(days=1)
    return resultat


def velg_aar(data, aar):
    return periode(data, datetime(aar, 1, 1), datetime(aar, 12, 31))
