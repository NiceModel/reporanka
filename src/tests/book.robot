*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command

*** Test Cases ***

Add Book With Correct Details Published In Common Era
    Add New Book  Meri  Meemikirja  2021
    Run App
    Output Should Contain  Uusi lukuvinkki lisätty.

Add Book With Correct Details Published Before Common Era
    Add New Book  Tuntematon  Rakkausrunoja  127 eaa.
    Run App
    Output Should Contain  Uusi lukuvinkki lisätty.

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

