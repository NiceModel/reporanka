*** Settings ***
Resource  resource.robot

*** Variables ***
${BOOK}         Book - Meri: Meemikirja (2021)

*** Test Cases ***
Start Application Succesfully
    Run App
    Output Should Contain   \nLUKUVINKKIKIRJASTO
    # Input   ${RUNS} == True

Main Menu Starts Successfully
    Run App
    Output Should Contain  \nValitse toiminto\n (1) lisää\n (2) listaa\n (3) poista\n (0) lopeta\n

Choose Function Add
    Input Add Command In Main Menu
    Run App
    Output Should Contain  \nMitä lisätään?\n (1) kirja\n (2) video\n (3) blogi\n (4) takaisin valikkoon\n (0) lopeta

Choose Function List With Empty List
    Input List Command In Main Menu
    Run App
    Output Should Contain  Sovellukseen ei ole tallennettu vinkkejä :(

Choose Function List With Some List
    Add Book
    Input List Command In Main Menu
    Run App
    Output Should Contain   \nLukuvinkkilista:\n

Function List Lists Existing Item
    Add Test Book And Add Command
    Input List Command In Main Menu
    Run App
    Output Should Contain   ${BOOK}

Function List Does Not List Non-existing Item
    Input List Command In Main Menu
    Run App
    Output Should Not Contain   ${BOOK}

# Function List Should Not List Deleted Item
#     Delete Book
#     Input List Command In Main Menu
#     Run App
#     Output Should Not Contain   ${BOOK}

Choose Function Remove
    Add Book
    Input Delete Command In Main Menu
    Run App
    Output Should Contain   \nVinkit:\n

Remove With Existing Item
    Delete Book

Back To Main Menu Succesfully
    Input Add Command In Main Menu
    Input Back To Main Menu Command In Add Menu
    Run App
    Output Should Contain   \nValitse toiminto\n (1) lisää\n (2) listaa\n (3) poista\n (0) lopeta\n

Quit In Add Menu Successfully
    Input Add Command In Main Menu
    Input Quit Command
    Run App
    Output Should Contain   Kiitti & moi!

Invalid Input In Main Menu
    Input  666
    Run App
    Output Should Contain  Komentoa ei löytynyt, yritä uudelleen.

Quit Application Succesfully
    Input Quit Command
    Run App
    Output Should Contain   Kiitti & moi!

Should Not Quit Application With False Command
    Input Add Command In Main Menu
    Input Back To Main Menu Command In Add Menu
    Output Should Not Contain   Kiitti & moi!

*** Keywords ***
Add Book
    Add New Book  Meri  Meemikirja  2021

Add Test Book And Add Command
    Input Add Command In Main Menu
    Input Add Book Command In Add Menu
    Add New Book  Meri  Meemikirja  2021
    Input Add Command In Main Menu
    Input Add Book Command In Add Menu
    Add New Book  TESTIKIRJAILIJA  TESTIKIRJA  2021
    Run App
    Output Should Contain  \nUusi lukuvinkki lisätty.

Delete Book
    Add Test Book And Add Command
    Input Delete Command In Main Menu
    Input   Meemikirja
    Input   K
    Run App
    Output Should Contain   Poistetaan vinkki...