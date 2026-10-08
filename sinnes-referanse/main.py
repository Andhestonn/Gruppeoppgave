"""Kjør: python main.py 2020, eller python main.py for spørsmål om årstall."""
import argparse
from pathlib import Path
from les_data import les_data
from ski_og_plot import skidager, plott_aar
from vekst_og_varme import plantevekst, varme_dager, avansert_vekst
from torke import lengste_torke

ROT = Path(__file__).resolve().parent


def dato(d):
    return d.strftime("%d.%m.%Y") if d else "ingen positiv vekst / ingen dato"


def rapport(data, aar):
    ski, ukjent, forventet = skidager(data, aar)
    print(f"År: {aar}")
    print(f"e) Skisesong 01.11.{aar-1}–31.05.{aar}: {ski} bekreftede skidager; "
          f"{ukjent} av {forventet} dager mangler snømåling.")
    vekst, ukjent = plantevekst(data, aar)
    print(f"f) Vekst på målte dager: {vekst:.1f} graddøgn; {ukjent} dager mangler temperatur.")
    if ukjent:
        print("   Full årssum er ukjent. Summen over er en nedre grense i denne modellen.")
    lengde, start, slutt = lengste_torke(data)
    print(f"g) Hele fila: lengste bekreftede tørkeperiode = {lengde} dager, {dato(start)}–{dato(slutt)}.")
    print("   Manglende nedbør bryter perioden; en lengre faktisk periode kan ikke utelukkes.")
    varme, ukjent = varme_dager(data, aar)
    print(f"h) Sommerdager >20: {varme[0]}, høysommerdager >25: {varme[1]}, tropedager >30: {varme[2]}.")
    print(f"   {ukjent} dager mangler maksimaltemperatur. Kategoriene overlapper.")
    try:
        april, beste, aarslutt = avansert_vekst(data, aar)
        print(f"i) Start 01.04: maksimal vekst {april[0]:.1f} den {dato(april[1])}; ved årsslutt {april[2]:.1f}.")
        print(f"   Fri start og slutt: {beste[0]:.1f}, start {dato(beste[1])}, slutt {dato(beste[2])}.")
        print(f"   Alternativ med fast slutt 31.12: {aarslutt[0]:.1f}, start {dato(aarslutt[1])}.")
    except ValueError as feil:
        print(f"i) Ikke beregnet: {feil}")


def main():
    parser = argparse.ArgumentParser(description="Værdata fra Sinnes")
    parser.add_argument("aar", type=int, nargs="?")
    parser.add_argument("--fil", type=Path, default=ROT / "data/sinnes_2014_2025_med_makstemperatur.csv")
    parser.add_argument("--uten-plott", action="store_true")
    parser.add_argument("--lagre-plott", type=Path)
    args = parser.parse_args()
    try:
        data = les_data(args.fil)
        tilgjengelig = sorted({d["dato"].year for d in data})
        print("Tilgjengelige år:", ", ".join(map(str, tilgjengelig)))
        aar = args.aar if args.aar is not None else int(input("Skriv inn årstall: "))
        if aar not in tilgjengelig:
            raise ValueError("Velg et år som finnes i fila.")
        rapport(data, aar)
        if not args.uten_plott or args.lagre_plott:
            plott_aar(data, aar, lagre=args.lagre_plott, vis=not args.uten_plott)
    except (ValueError, OSError) as feil:
        parser.exit(1, f"Feil: {feil}\n")


if __name__ == "__main__":
    main()
