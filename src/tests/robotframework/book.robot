*** Settings ***
Resource  resource.robot
Test Setup  Add Test Book And Add Command

*** Test Cases ***

Add Book With Correct Details Published In Common Era
    Add New Book  TESTIKIRJAILIJA  TESTIKIRJA  2021
    Run App
    Output Should Contain  \nUusi lukuvinkki 'TESTIKIRJAILIJA: TESTIKIRJA (2021)' lisätty.

Add Book With Correct Details Published Before Common Era
    Add New Book  Tuntematon  Rakkausrunoja  127 eaa.
    Run App
    Output Should Contain  \nUusi lukuvinkki 'Tuntematon: Rakkausrunoja (127 eaa.)' lisätty.

Add Duplicate Book
    Add New Book  Meri  Meemikirja  2021
    Run App
    Output Should Contain  \nLukuvinkki 'Meri: Meemikirja (2021)' on jo listassa!

Add Book With No Author
    Add New Book  ${EMPTY}  Kirja  1990
    Run App
    Output Should Contain  Kirjailijan nimi on lisättävä!

Add Book With No Title
    Add New Book  Marius Pontmercy  ${EMPTY}  1789
    Run App
    Output Should Contain  Kirjan nimi on lisättävä!

Add Book With No Year
    Add New Book  Meri  Meemikirja  ${EMPTY}
    Run App
    Output Should Contain  Julkaisuvuosi ei ole kelvollinen!

Add Book With Invalid Year
    Add New Book  Meri  Meemikirja  27000
    Run App
    Output Should Contain  Julkaisuvuosi ei ole kelvollinen!

*** Keywords ***
Add Test Book And Add Command
    Input Add Command
    Add New Book  Meri  Meemikirja  2021
    Input Add Command
