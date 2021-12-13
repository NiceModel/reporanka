# template for details view user story acceptance criteria

*** Settings ***
Resource  resource.robot
Test Setup  Clear And Add Items

*** Test Cases ***
Details Can Be Fetched With Id Number
    Clear Test File
    Id Search
    Run App
    Output Should Contain  \nVinkin tarkemmat tiedot:\n

Details Contain Item Author And Title
    Clear Test File
    Id Search
    Run App
    Output Should Cover  Jonathan Safran Foer  Eating Animals

Returns From Details To Main Menu Succesfully
    Clear Test File
    Id Search
    Run App
    Run App
    Input  0
    Output Should Contain  Kiitti & moi!

*** Keywords ***
Clear And Add Items
    Clear Test File
    Add Test Items

Id Search
    Input Search By Id In Main Menu
    Input  1a1a
