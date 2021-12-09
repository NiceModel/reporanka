*** Settings ***
Resource  resource.robot
Test Setup  Add Test Book

*** Test Cases ***

Add Book With Correct Details
    Add New Book  Victor Hugo  Les Misérables  1862
    Run App
    Output Should Contain  \nUusi lukuvinkki lisätty.

Add Duplicate Book
    Add New Book  Jonathan Safran Foer  Eating Animals  2009
    Run App
    Output Should Contain  \nLukuvinkki on jo tallennettu aiemmin!

Add Book With No Author
    Add New Book  ${EMPTY}  Les Misérables  1862
    Run App
    Output Should Contain  Kirjailijan nimi on lisättävä!

Add Book With No Title
    Add New Book  Victor Hugo  ${EMPTY}  1862
    Run App
    Output Should Contain  Kirjan nimi on lisättävä!

Add Book With No Year
    Add New Book  Victor Hugo  Les Misérables  ${EMPTY}
    Run App
    Output Should Contain  Julkaisuvuosi ei ole kelvollinen!
