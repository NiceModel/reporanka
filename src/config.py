"""Module for specifying the environmental variables."""
import os

DIRNAME = os.path.dirname(__file__)

DB_NAME = "items.csv"
DB_PATH = os.path.join(DIRNAME, "data", DB_NAME)

TEST_DB = "test_items.csv"
TEST_DB_PATH = os.path.join(DIRNAME, "data", TEST_DB)

INSTRUCTIONS = (
    "\nValitse toiminto"
    "\n (1) lisää"
    "\n (2) listaa"
    "\n (3) poista"
    "\n (0) lopeta\n")

ADD_MENU = (
    "\nMitä lisätään?"
    "\n (1) kirja"
    "\n (2) video"
    "\n (3) blogi"
    "\n (4) takaisin valikkoon"
    "\n (0) lopeta")

CMD_PROMPTS = {
    "book": [("Kirjailijan/kirjailijoiden nimet: ", "Kirjailijan nimi on lisättävä!"),
             ("Kirjan nimi: ", "Kirjan nimi on lisättävä!"),
             ("Julkaisuvuosi: ", "Julkaisuvuosi ei ole kelvollinen!")
             ],
    "video": [("Videon tekijä: ", "Videon tekijä on lisättävä!"),
              ("Videon nimi: ", "Videon nimi on lisättävä!"),
              ("Videon osoite: ", "Videon osoite on lisättävä!"),
              ("Videon julkaisupäivä: ", "Videon julkaisupäivä on lisättävä!")
              ],
    "blog": [("Blogin kirjoittaja: ", "Blogin kirjoittaja on lisättävä!"),
             ("Blogin nimi: ", "Blogin nimi on lisättävä!"),
             ("Postaus: ", "Postauksen nimi on lisättävä!"),
             ("Blogin osoite: ", "Blogin osoite on lisättävä!"),
             ("Postauksen julkaisupäivä: ", "Postauksen julkaisupäivä on lisättävä!")
             ],
    "delete": [("\nAnna poistettavan teoksen nimi: ", "Teoksen nimi on annettava!")
              ]
}

OUTPUTS = {
    "already in list": "\nLukuvinkki on jo tallennettu aiemmin!",
    "added": "\nUusi lukuvinkki lisätty.",
    "empty list": "Sovellukseen ei ole tallennettu vinkkejä :(",
    "choice": "\nValinta: ",
    "list": "\nTallennetut vinkit:\n",
    "item not found": "Teosta ei löytynt.",
    "confirm": "\nOletko varma (K/E)? ",
    "deleting": "Poistetaan vinkki...",
    "not deleted": "Vinkkiä ei poistettu.",
    "unknown command": "Komentoa ei löytynyt, yritä uudelleen.",
    "quit": "Kiitti & moi!"
}

TITLE = "\nLUKUVINKKIKIRJASTO"
YES = 'K'
NO = 'E'
