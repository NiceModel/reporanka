# Lukuvinkkisovellus

Tästä repositoriosta löytyy lukuvinkkisovellus, joka on kehitetty Helsingin Yliopiston Ohjelmistotuotanto-kurssin miniprojektina syksyllä 2021. Projektin päämääränä on oppia ketterää ohjelmistokehitystä ja ryhmätyöskentelytaitoja. 

Backlogeille ja tuntikirjanpidolle ym. on käytössä Google Sheets, jota pääsee katsomaan [täällä](https://docs.google.com/spreadsheets/d/1F-_b98SG2x79MAu5fpZetq0ALNqiHoFdLUIKrC1T9-I/edit?usp=sharing). Lisäksi ensimmäisen tapaamisen brainstorming-sessiossa käytimme Flingaa, ja brainstromingin tuloksia voi vilkaista [täällä](https://edu.flinga.fi/s/EMA2DL6).

### Asennusohjeet
*Ohjeissa oletetaan, että olet luonut ssh-avaimen koneellesi ja lisännyt sen GitHubiin*

1) Kloonaa repositorio paikalliselle koneelle: `git clone git@github.com:NiceModel/reporanka.git`
2) Asenna riippuvuudet seuraavalla komennolla: `poetry install` 
3) Käynnistä sovellus: `poetry run invoke start`

### Command line

+ Riippuvuuksien asentaminen: `poetry install`
+ Sovelluksen käynnistäminen: `poetry run invoke start`
+ Yksikkötestaus: `poetry run invoke test`
+ Yksikkötestien haaraumakattavuusraportti: `poetry run invoke coverage-report`
  + Raportin löydät *htmlcov* -kansiosta
+ Lint: `poetry run invoke lint`