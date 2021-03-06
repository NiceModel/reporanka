# Lukuvinkkisovellus

![Github Actions](https://github.com/NiceModel/reporanka/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/NiceModel/reporanka/branch/main/graph/badge.svg?token=MKB73DT68H)](https://codecov.io/gh/NiceModel/reporanka)


Tästä repositoriosta löytyy lukuvinkkisovellus, joka on kehitetty Helsingin Yliopiston Ohjelmistotuotanto-kurssin miniprojektina syksyllä 2021. Projektin päämääränä on oppia ketterää ohjelmistokehitystä ja ryhmätyöskentelytaitoja. 

Backlogeille ja tuntikirjanpidolle ym. on käytössä Google Sheets, jota pääsee katsomaan [täällä](https://docs.google.com/spreadsheets/d/1F-_b98SG2x79MAu5fpZetq0ALNqiHoFdLUIKrC1T9-I/edit?usp=sharing). Lisäksi ensimmäisen tapaamisen brainstorming-sessiossa käytimme Flingaa, ja brainstromingin tuloksia voi vilkaista [täällä](https://edu.flinga.fi/s/EMA2DL6).

### Asennusohjeet
*Ohjeissa oletetaan, että olet luonut ssh-avaimen koneellesi ja lisännyt sen GitHubiin*

1) Kloonaa repositorio paikalliselle koneelle: `git clone git@github.com:NiceModel/reporanka.git`
    + TAI lataa viimeisin release [täältä](https://github.com/NiceModel/reporanka/releases)
3) Asenna riippuvuudet seuraavalla komennolla: `poetry install` 
4) Käynnistä sovellus: `poetry run invoke start`

### Command line

+ Riippuvuuksien asentaminen: `poetry install`
+ Sovelluksen käynnistäminen: `poetry run invoke start`
+ Testaus:
  + yksikkötestaus (unittest): `poetry run invoke test`
  + hyväksymistestaus (robot framework): `poetry run invoke robot`
+ Yksikkötestien haaraumakattavuusraportti: `poetry run invoke coverage-report`
  + Raportin löydät *htmlcov* -kansiosta
+ Lint: `poetry run invoke lint`


## Definition of Done

+ Yksikkötestit on toteutettu
+ Testien haaraumakattavuus 70%
+ Sovellus toimii oikeilla syötteillä
+ Sovellus antaa järkevät virheilmoitukset yleisimmillä virheellisillä syötteillä
+ Github Actions on otettu käyttöön yksikkötestaukseen
+ Robot Framework on otettu käyttöön

## Loppuraportti
[Linkki loppuraporttiin](https://docs.google.com/document/d/1LOSab8Gh7XG8nHRHQoasI1nv2A6ZAU4luoKl7OryltA/edit?usp=sharing)
