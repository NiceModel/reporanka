*** Settings ***
Resource  resource.robot
Test Setup  Add Test Items And Input Clear Command

*** Test Cases ***
Choose Delete All Command  
    Run App
    Input Clear Command In Main Menu
    Output Should Contain  \nTallennetut vinkit:\n

App Verifies Delete All
    Verify Delete All
    Run App
    Output Should Contain  Poistetaan kaikkia vinkkejä. Hyvästi!

Items Are Not Deleted Without Verification
    Do Not Verify Delete All
    Run App
    Output Should Contain  Vinkkejä ei poistettu.

*** Keywords ***
Add Test Items And Input Clear Command
    Clear Data
    Add Test Items
    Input Clear Command In Main Menu

Verify Delete All
    Input  K

Do Not Verify Delete All
    Input  E
