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
    "\n (0) lopeta\n")

ADD_MENU = (
    "\nMitä lisätään?"
    "\n (6) kirja"
    "\n (7) video"
    "\n (8) blogi"
    "\n (9) takaisin valikkoon")

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
             ]
}
