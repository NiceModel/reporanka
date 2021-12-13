*** Settings ***
Resource  resource.robot
Test Setup  Add Test Items And Input Clear Command

*** Test Cases ***
Choose Clear Command  
    Run App
    Input Clear Command In Main Menu
    Output Should Contain  \nTallennetut vinkit:\n

App Verifies Deletion
    Verify Clear
    Run App
    Output Should Contain  Tyhjennetään tiedosto kaikista vinkeistä. Hyvästi!

Item Is Not Deleted Without Verification
    Do Not Verify Clear
    Run App
    Output Should Contain  Tiedostoa ei tyhjennetty.

*** Keywords ***
Add Test Items And Input Clear Command
    Clear Data
    Add Test Items
    Input Clear Command In Main Menu

Verify Clear
    Input  K

Do Not Verify Clear
    Input  E