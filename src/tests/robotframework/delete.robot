*** Settings ***
Resource  resource.robot
Test Setup  Add Test Items And Input Delete Command

*** Test Cases ***
Choose Delete Command
    Run App
    Output Should Contain  \nTallennetut vinkit:\n

App Verifies Deletion
    Delete Test Book
    Verify Delete
    Run App
    Output Should Contain  Poistetaan vinkki...

Item Is Not Deleted Without Verification
    Delete Test Book
    Do Not Verify Delete
    Run App
    Output Should Contain  Vinkkiä ei poistettu.

Delete Non-Existing Item
    Input  Trainspotting
    Run App
    Output Should Contain  Teosta ei löytynyt.

*** Keywords ***
Add Test Items And Input Delete Command
    Clear Data
    Add Test Items
    Input Delete Command In Main Menu

Delete Test Book
    Input  Eating Animals

Verify Delete
    Input  K

Do Not Verify Delete
    Input  E
