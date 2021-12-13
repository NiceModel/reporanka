# template for details view user story acceptance criteria

*** Settings ***
Resource  resource.robot
# Test Setup  Clear Test File
# Test Setup  Add Test Items With Ids
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

*** Keywords ***
Clear And Add Items
    Clear Test File
    Add Test Items

Id Search
    Input Search By Id In Main Menu
    Input  1a1a
