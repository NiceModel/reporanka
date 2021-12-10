*** Settings ***
Resource  resource.robot
Test Setup  Add Test Video

*** Test Cases ***

Add Video With Correct Details
    Add New Video  Team StarKid  A Very Potter Musical Act 1 Part 1  https://youtu.be/wmwM_AKeMCk  5.7.2009
    Run App
    Output Should Contain  \nUusi lukuvinkki lisätty.

Add Duplicate Video
    Add New Video  Studio Killers  Jenny (I Wanna Ruin Our Friendship) OFFICIAL MUSIC VIDEO  https://youtu.be/hyj4JFSErrw  24.12.2015
    Run App
    Output Should Contain  \nLukuvinkki on jo tallennettu aiemmin!

Add Video With No Creator
    Add New Video  ${EMPTY}  A Very Potter Musical Act 1 Part 1  https://youtu.be/wmwM_AKeMCk  5.7.2009
    Run App
    Output Should Contain  Videon tekijä on lisättävä!

Add Video With No Title
    Add New Video  Team StarKid  ${EMPTY}  https://youtu.be/wmwM_AKeMCk  5.7.2009
    Run App
    Output Should Contain  Videon nimi on lisättävä!

Add Video With No Url
    Add New Video  Team StarKid  A Very Potter Musical Act 1 Part 1  ${EMPTY}  5.7.2009
    Run App
    Output Should Contain  Videon osoite on lisättävä!

Add Video With No Publishing Date
    Add New Video  Team StarKid  A Very Potter Musical Act 1 Part 1  https://youtu.be/wmwM_AKeMCk  ${EMPTY}
    Run App
    Output Should Contain  Videon julkaisupäivä on lisättävä!

*** Keywords ***
Clear Data And Add Test Video
    Clear Data
    Add Test Video
