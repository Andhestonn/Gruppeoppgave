"""MEDLEM B: hovedprogram/meny som binder alt sammen."""
from data import les_data
from plotting import plott_aar
from ski import skifore_dager
from vekst import total_plantevekst, maks_vekst_fra_start, beste_startdato
from perioder import lengste_toerre_periode
from statistikk import antall_varme_dager

FILNAVN = "sinnes.csv"  # endre til riktig filnavn


def hent_aar():
    """Spør brukeren om et årstall (med feilhåndtering)."""
    pass


def main():
    """Meny-løkke: 1 plott, 2 skiføre, 3 plantevekst, 4 tørr periode,
    5 varme dager, 6 (valgfri) avansert vekst, 0 avslutt."""
    pass


if __name__ == "__main__":
    main()