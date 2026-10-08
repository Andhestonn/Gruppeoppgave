# Sinnes: referanseprosjekt for to medlemmer

Dette er et ferdig eksempel dere kan kjøre og sammenlikne deres egen løsning med. Start med `SAMARBEID.md` for Git og oppgavefordeling. Begge CSV-filene følger med uendret. Det er ikke opprettet noe faktisk GitHub-repository eller sendt invitasjoner.

## Kom i gang

Bruk Python 3.10 eller nyere. Åpne en terminal i denne mappa. På Windows:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe main.py
```

Skriv for eksempel `2020` når programmet spør. Fire diagrammer åpnes i ett vindu. Lukk vinduet når dere er ferdige. Hvis `py` ikke finnes, prøv `python` i første kommando. Python må være installert.

På macOS/Linux:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

Eksempler på Windows etter oppsett:

```powershell
.venv\Scripts\python.exe main.py 2020 --uten-plott
.venv\Scripts\python.exe main.py 2020 --lagre-plott sinnes_2020.png
.venv\Scripts\python.exe -m unittest -v
.venv\Scripts\python.exe main.py 2020 --fil data/sinnes_2014_2025.csv --uten-plott
```

Den siste kommandoen bruker grunnfila. Del h vil da ha ukjent maksimaltemperatur for alle dagene. Null bekreftede dager er ikke det samme som at ingen slike dager forekom.

## Hvor finner dere deloppgavene?

| Del | Fil/funksjon | Hovedansvar |
|---|---|---|
| a–c | `SAMARBEID.md` | Begge, medlem 1 oppretter repo |
| Felles innlesing | `les_data.py`: `les_data`, `velg_aar` | Begge |
| d | `ski_og_plot.py`: `plott_aar` | Medlem 1 |
| e | `ski_og_plot.py`: `skidager` | Medlem 1 |
| f | `vekst_og_varme.py`: `plantevekst` | Medlem 2 |
| g | `torke.py`: `lengste_torke` | Begge, bytt på tastaturet |
| h | `vekst_og_varme.py`: `varme_dager` | Medlem 2 |
| i | `vekst_og_varme.py`: `avansert_vekst` | Begge, frivillig |
| Kjøring og kontroll | `main.py`, `test_referanse.py` | Begge |

## Felles avtale om data

`les_data(filnavn)` gir en liste med én ordbok per dag. Nøklene er `dato`, `temperatur`, `maks`, `nedbor`, `vind`, `sno`. Dato er et `datetime`-objekt, målinger er `float`, og ukjente målinger er `None`. Alle analysefunksjoner får denne samme lista. Ingen av dem endrer den. Dermed kan dere utvikle del d/e og f/h uavhengig etter at innlesingen er avtalt.

Innlesingen bruker kolonnenavn, siden maksimaltemperatur er lagt inn før middeltemperatur i den utvidede fila. Semikolon skiller kolonner; komma i et tall blir til punktum før `float`. Kildeteksten nederst hoppes over. Dagene sorteres, og duplikatdatoer avvises.

## Regler og tolkninger

- **d:** Hele kalenderåret plottes i fire deldiagrammer, med separate enheter. Ukjente målinger gir brudd i kurvene.
- **e:** År 2020 betyr 1. november 2019 til og med 31. mai 2020. Snødybde **minst 20 cm** teller. Ukjente dager oppgis separat. De 61 dagene i november/desember 2013 mangler når 2014 velges.
- **f:** Dagsvekst er `max(middeltemperatur - 5, 0)`. Resultatet er en temperaturbasert vekstindeks i graddøgn, ikke centimeter plante. Når temperatur mangler, vises bare summen for målte dager og antall ukjente dager.
- **g:** Oppgaven angir ikke år, så referansen søker i hele fila. Nedbør må være nøyaktig 0. Ukjent nedbør eller en manglende kalenderdag bryter den bekreftede perioden. Begge endepunktene teller. Ved lik lengde velges første periode.
- **h:** Bruk maksimaltemperatur, aldri middeltemperatur som erstatning. Grensene er strengt **over** 20, 25 og 30 °C. Kategoriene overlapper: 31 °C teller i alle tre.
- **i:** Dagsvekst er `T` når `T < 0`, null når `0 ≤ T ≤ 5`, og `T - 5` når `T > 5`. Oppsamlet vekst nullstilles ikke ved frost. Hovedtolkningen er den høyeste oppsamlede veksten på noe tidspunkt i året, først med start 1. april, deretter med valgfri start i året. Startdagen er med. Programmet viser også alternativet med fast slutt 31. desember, siden oppgaveteksten kan tolkes slik. Ved like resultater beholdes tidligste start/slutt. Null vekst før første døgn er tillatt for maksimum; ingen positiv vekst gir ingen sluttdato. Del i beregnes ikke for år med ukjent temperatur.

## Tall dere kan sammenlikne med

Kjør `main.py 2020 --uten-plott` med fila som inneholder maksimaltemperatur:

| Beregning | Referanse |
|---|---:|
| Skidager i sesongen 2019/2020 | 77 |
| Ukjente snødager i den sesongen | 0 av 213 |
| Plantevekst i 2020, del f | 936,7 |
| Sommerdager / høysommerdager / tropedager | 31 / 8 / 0 |
| Lengste bekreftede tørkeperiode i hele fila | 24 dager, 05.05.2018–28.05.2018 |
| Maksimal vekst fra 01.04.2020 | 931,9, nådd 18.11.2020 |
| Beste frie start/slutt | 18.04.2020–18.11.2020, vekst 936,5 |
| Beste start med fast slutt 31.12.2020 | 18.04.2020, vekst 905,6 |

Den utvidede fila har 4 383 unike datoer fra 01.01.2014 til 31.12.2025. Grunnfila har 4 335 datoer og stopper 13.11.2025; de siste 48 dagene i året mangler. Målingene i de felles kolonnene samsvarer for felles datoer. I den utvidede fila mangler 43 middeltemperaturer, 7 maksimaltemperaturer, 144 nedbørsmålinger, 47 vindmålinger og 898 snømålinger. Enkelte rader ligger ute av datorekkefølge. Kalenderdekning betyr derfor ikke at alle målingene finnes.

## Datakilde

Vedlagte CSV-filer fra brukeren, stasjon Sirdal – Sinnes, SN42940. Filenes kildemerknad oppgir Meteorologisk institutt (MET), data gyldig per 28.09.2026, CC BY 4.0. Originalfilene er beholdt; analysen sorterer og tolker manglende verdier i minnet. Behold denne krediteringen ved videre bruk. Lisensinformasjon: https://creativecommons.org/licenses/by/4.0/.
