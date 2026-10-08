# Samarbeidsoppsett: to personer som er nye i Git

Målet er at begge skal klone, gjøre en egen endring, lagre den med Git, laste den opp og få den gjennomgått av den andre. Bruk referansekoden til å sammenlikne resultater og forstå funksjonsdelingen. Når dere skriver deres egen løsning, gjør det i små steg dere begge kan forklare.

## 1. Ordene dere trenger

| Ord | Betydning i øvingen |
|---|---|
| Git | Holder historikk over endringer på datamaskinen |
| GitHub | Nettstedet hvor dere deler prosjektet |
| Repository / repo | Prosjektmappa med Git-historikken |
| Clone | Hente repoet til egen datamaskin, vanligvis én gang |
| Branch / grein | En egen arbeidslinje i samme prosjekt |
| Main | Den felles greina med ferdige, gjennomgåtte endringer |
| Commit | Et lokalt lagringspunkt med en forklarende melding |
| Push | Laste opp lokale commits til GitHub |
| Pull | Hente og innarbeide endringer fra GitHub |
| Pull request / PR | Be den andre se gjennom endringene før fletting |
| Merge | Flette endringer fra en grein inn i en annen |

Å lagre en fil i editoren, lage en commit og pushe er tre forskjellige handlinger.

## 2. Fordel arbeidet

| Arbeidsøkt | Medlem 1 | Medlem 2 | Ferdig når |
|---|---|---|---|
| Felles oppstart | Oppretter repo og inviterer | Godtar invitasjon | Begge har klonet og kan kjøre eksemplet |
| Felles datamodell | Leser CSV sammen med medlem 2 | Kontrollerer datoer og ukjente verdier | Begge forstår ordbøkene fra `les_data` |
| Eget arbeid | d og e: plotting og skiføre | f og h: plantevekst og varme dager | Hver har en PR med én avgrenset endring |
| Kryssjekk | Leser og prøver medlem 2s kode | Leser og prøver medlem 1s kode | Begge PR-er er gjennomgått og flettet |
| Felles logikk | Skriver g mens medlem 2 kontrollerer | Kontrollerer g, skriver deretter test | Tørkeperioder håndterer datoer og hull |
| Frivillig | Kontrollerer i og forklarer resultatene | Skriver i sammen med medlem 1 | Begge er enige om start/slutt-tolkningen |
| Avslutning | Kjører fra oppdatert main | Sammenlikner med referansetall | Begge får samme resultat |

Opprett gjerne GitHub Issues med titlene «d/e: plotting og skiføre», «f/h: vekst og varme» og «g: tørkeperiode». Sett ansvarlig medlem på de to første. Hver PR beskriver hva som er endret og hvordan dere har prøvd det.

## 3. Opprett repoet én gang

1. Begge lager hver sin GitHub-konto og installerer Git og Python. Bruk gjerne VS Code som editor.
2. Medlem 1 oppretter repoet `sinnes-vaerdata` på GitHub. Velg privat hvis øvingen bare skal deles med gruppa. Huk av for å lage en README slik at `main` finnes.
3. Medlem 1 åpner repoets **Settings → Collaborators → Add people**, velger medlem 2 og sender invitasjonen. Medlem 2 godtar den. Se [GitHubs veiledning om samarbeidspartnere](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).
4. På repoets forside velger dere **Code → HTTPS** og kopierer URL-en.

## 4. Begge kloner hver sin lokale kopi

Åpne en terminal i mappa hvor dere vil ha prosjektet. Bytt ut `DITT_NAVN`, `DIN_EPOST` og `EIER` med egne verdier. Begge bruker samme repo-URL, men sitt eget navn og sin egen e-post i Git-oppsettet.

```sh
git config --global user.name "DITT_NAVN"
git config --global user.email "DIN_EPOST"
git clone https://github.com/EIER/sinnes-vaerdata.git
cd sinnes-vaerdata
git status
```

Bruk e-post knyttet til GitHub-kontoen, eventuelt GitHubs private noreply-adresse fra kontoinnstillingene. Ved innlogging fra Git følger dere nettleservinduet som åpnes. GitHub-passordet brukes ikke som passord for HTTPS-operasjoner i terminalen.

Medlem 1 kopierer innholdet i referansemappa inn i den klonede mappa, inkludert `.gitignore` og `data`. Ikke kopier `.venv` eller `__pycache__`. Overskriv den tomme README-en fra GitHub med den vedlagte. Dette gir dere et felles, kjørbart utgangspunkt:

```sh
git status
git add .
git commit -m "Legg til referanseprosjekt og vaerdata"
git push origin main
```

Dette er felles oppstartscommit. Videre arbeid skjer på greiner. Medlem 2 kjører nå:

```sh
git pull --ff-only origin main
```

Begge setter opp Python-miljøet slik README beskriver. `.venv` finnes bare lokalt; den deles ikke gjennom Git.

## 5. Første trygge øvelse på hver deres grein

Start med rene arbeidsmapper: `git status` skal ikke vise ulagrede Git-endringer. Medlem 1:

```sh
git switch main
git pull --ff-only origin main
git switch -c medlem1-ski-plot
```

Medlem 2 gjør tilsvarende, men bruker `git switch -c medlem2-vekst-varme`. Kommandoen oppretter og bytter til en ny grein. Neste gang greina skal brukes, er det bare `git switch medlem1-ski-plot`, uten `-c`. Se [Git: switch](https://git-scm.com/docs/git-switch).

For en første Git-øvelse lager medlem 1 `notat_medlem1.md` med en forklaring på hvorfor sesongen 2020 begynner i 2019. Medlem 2 lager `notat_medlem2.md` med en forklaring på hvorfor 31 °C teller i tre kategorier. Da øver begge på hele flyten uten å måtte endre fungerende beregninger.

Medlem 1 lagrer fila og kjører:

```sh
git status
git add notat_medlem1.md
git commit -m "Forklar hvordan skisesongen avgrenses"
git push -u origin medlem1-ski-plot
```

Medlem 2 bruker sitt eget filnavn, sin egen melding og grein. `-u` kobler den lokale greina til greina på GitHub. Senere opplastinger fra samme grein trenger bare `git push`.

Når dere endrer Python-koden, prøv programmet før hver commit. Bruk `git diff` for å lese endringer i filer Git allerede sporer, og `git status` for også å se nye filer. Legg til de aktuelle filene med `git add filnavn.py`.

## 6. Gjennomgå og flett

1. Den som har pushet, åpner GitHub og lager en PR. Velg **base: main**, og egen grein som **compare**. Skriv hva som er endret og hvordan det er kontrollert.
2. Den andre leser **Files changed**. For kodeendringer kan vedkommende prøve greina lokalt fra en ren arbeidsmappe:

```sh
git fetch origin
git switch --track origin/medlem1-ski-plot
```

Dette eksemplet er for medlem 2 som prøver medlem 1s grein første gang. Finnes greina allerede lokalt, bruk `git switch medlem1-ski-plot` og `git pull --ff-only`. Bytt navn når medlem 1 prøver medlem 2s grein.

3. Kjør program og tester fra README. Gi konkret tilbakemelding i PR-en. Forfatteren retter på samme grein, committer og pusher; PR-en oppdateres.
4. Når begge er fornøyde, velg **Merge pull request** og bekreft på GitHub. Se [GitHubs PR-veiledning](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).
5. Begge går tilbake til main og henter resultatet:

```sh
git switch main
git pull --ff-only origin main
```

Lag en ny grein fra oppdatert main for neste avgrensede oppgave. Ikke fortsett en gammel, ferdig flettet grein. Det gjør historikken lettere å forstå.

## 7. Hvis begge har endret samme linje

En konflikt betyr at Git trenger deres hjelp til å velge innhold. Commit egne endringer før dere starter. På arbeidsgrenen, for eksempel medlem 1s:

```sh
git switch medlem1-ski-plot
git fetch origin
git merge origin/main
```

Hvis det oppstår konflikt, viser `git status` filene. Åpne dem sammen. Mellom `<<<<<<<`, `=======` og `>>>>>>>` ligger de konkurrerende versjonene. Skriv den riktige kombinasjonen og fjern markørene. Prøv programmet, og fullfør:

```sh
git add filen_dere_rettet.py
git commit -m "Los konflikt med main"
git push
```

Bytt ut filnavnet med den faktiske fila. Hvis dere vil avbryte akkurat denne pågående flettingen, bruk `git merge --abort`. Unngå å løse usikkerhet ved å slette repoet eller tvinge opplasting med force.

## 8. Ferdigkriterier

- Begge har en lokal klone og egne commits med eget navn.
- Begge har laget minst én PR og kontrollert den andres arbeid.
- Alle deloppgavene d–h kjører fra main; i er tydelig merket frivillig.
- Dere kan forklare forskjellen på dato, målt null og ukjent måling.
- Referanseåret 2020 gir tallene i README, og tester består.
- Et år med manglende data, for eksempel 2021, viser usikkerheten.
- README forklarer oppsett, arbeidsdeling og valgt tolkning av i.
