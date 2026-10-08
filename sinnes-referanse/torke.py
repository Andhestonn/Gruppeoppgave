"""Del g: skriv sammen, med én ved tastaturet og én som kontrollerer."""
from datetime import timedelta


def lengste_torke(data):
    beste = (0, None, None)
    lengde = 0
    start = None
    forrige = None
    for dag in sorted(data, key=lambda d: d["dato"]):
        dato = dag["dato"]
        if dag["nedbor"] == 0:
            if lengde == 0 or dato != forrige + timedelta(days=1):
                start = dato
                lengde = 1
            else:
                lengde += 1
            if lengde > beste[0]:
                beste = (lengde, start, dato)
        else:
            lengde = 0  # Også ukjent nedbør bryter den bekreftede perioden.
        forrige = dato
    return beste
