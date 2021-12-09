*** Settings ***
Resource  resource.robot
Test Setup  Add Items And Input Delete Command

*** Test Cases ***
Delete Command Can Be Chosen
    Run App
    Output Should Contain  \nVinkit:\n

Delete Existing Book
    Delete Book
    Output Should Contain  Poistetaan vinkki...

*** Keywords ***
Delete Book
    Input  Meemikirja
    Input  K
    Run App

Add Items And Input Delete Command
    Input Add Command In Main Menu
    Input Add Book Command In Add Menu
    Add New Book  Meri  Meemikirja  2021
    Input Delete Command In Main Menu
