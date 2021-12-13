# template for details view user story acceptance criteria

*** Settings ***
Resource  resource.robot
Test Setup  Clear Test File
Test Setup  Add Test Items With Ids

*** Test Cases ***
Details Can Be Fetched With Id Number
    Input Search By Id In Main Menu
    Input  1a1a
    Run App
    Output Should Contain  \nVinkin tarkemmat tiedot:\n
