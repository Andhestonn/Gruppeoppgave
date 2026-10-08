# Gruppeoppgave
Oppgavene:
a) GitHub-repo: Én lager repoet, de andre inviteres.

b) Samarbeid: Alle kloner repoet lokalt og pusher koden dit. Bruk gjerne egne grener (branches) og merge inn i main.

c) Oppgavefordeling: Planlegg hvilke funksjoner som kan skrives uavhengig av hverandre, og hva som gjøres felles.

d) Plotting: Bruker skriver inn et årstall. Plott snødybde, nedbør, middeltemperatur og maks vind per dag. Tips: gjør om datostrenger til datetime-objekter.

e) Skiføre: Skiføre = snødybde ≥ 20 cm. Tell dager med skiføre i skisesongen (november året før til mai i valgt år).

f) Plantevekst: Vekst per dag = temperatur − 5 (planten trenger minst 5 °C). Beregn total vekst for et år.

g) Lengste tørre periode: Finn lengste sammenhengende periode med 0 nedbør. Skriv ut lengde, startdato og sluttdato.

h) Antall pr. år: Tell sommerdager (>20 °C), høysommerdager (>25 °C) og tropedager (>30 °C) i et gitt år. Oppgaven sier «maksimaltemperatur», men filen har bare middeltemperatur, så dette bør dere avklare eller bruke middeltemperaturen.

i) Frivillig, avansert: Nå skader minusgrader planten (negativ vekst lik antall minusgrader). Finn maks vekst hvis planten starter 1. april, og finn deretter startdato som gir høyest vekst gjennom året.

gruppeprosjekt/
├── data.py         ← FELLES: les_data, filtrer_periode, filtrer_aar
├── plotting.py     ← B: plott_aar (d)
├── main.py         ← B: meny som kaller alt
├── ski.py          ← C: skifore_dager (e)
├── statistikk.py   ← C: antall_varme_dager (h)
├── vekst.py        ← D: total_plantevekst (f), A: i)-funksjonene
└── perioder.py     ← A: lengste_toerre_periode (g)

# Hvorfor det fungerer

Én fil per person (nesten): Ingen redigerer samme fil samtidig, så Git-merging går smertefritt. Unntaket er vekst.py, der D skriver én funksjon og A to. Dere kan la A lage en egen fil, vekst_avansert.py, hvis dere vil unngå konflikter helt.

Felles «kontrakt»: Docstringen i data.py beskriver nøyaktig hvordan dataene ser ut. Alle funksjoner tar data (liste av dicts) og eventuelt aar som argumenter.

Uavhengig testing: Alle trenger bare les_data for å teste sin egen del. Til å begynne med kan dere lage en liten testliste for hånd.

# Anbefalt rekkefølge

A (eller den som kan mest) skriver les_data først og pusher til main. Det bør ta under en time. Alle andre venter ikke og kan sette opp Git og lese oppgaven mens de venter.

Alle lager hver sin gren, for eksempel ski, plotting og vekst, og kloner/pull'er data.py fra main.

Hver person skriver sine funksjoner og tester dem med en if __name__ == "__main__":-blokk nederst i egen fil.

Når en funksjon er ferdig, lager dere en pull request, en annen i gruppa leser gjennom, og så merges den til main.

B kobler til slutt alt sammen i main.py.

# Ting å være obs på i data.py

Sjekk hvordan manglende verdier er skrevet i CSV-fila (ofte -), og om desimaltegnet er komma eller punktum.

Konverter datoene til datetime med datetime.strptime, og sjekk datoformatet i fila først.

Alle de andre funksjonene må tåle None-verdier, så avtal sammen hvordan de skal håndteres, for eksempel å hoppe over dagen.