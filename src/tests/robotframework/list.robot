*** Settings ***
Resource  resource.robot
Test Setup  Clear Data

*** Variables ***
${BOOK}  id: 0000, tyyppi: Book, tiedot: Jonathan Safran Foer: Eating Animals (2009)
${BLOG}  id: 0000, tyyppi: Blog, tiedot: Pedro Medeiros: Pixel Grimoire, How to start making pixel art #6, 8.1.2019, (https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-6-a74f562a4056)
${VIDEO}  id: 0000, tyyppi: Video, tiedot: Studio Killers: Jenny (I Wanna Ruin Our Friendship) OFFICIAL MUSIC VIDEO, https://youtu.be/hyj4JFSErrw, (24.12.2015)


*** Test Cases ***
List Items When List Is Not Empty
    Add Test Items
    Input List Command In Main Menu
    Run App
    Output Should Contain  \nTallennetut vinkit:\n

List Items When List Is Empty
    Input List Command In Main Menu
    Run App
    Output Should Contain  Sovellukseen ei ole tallennettu vinkkejä :(

List Contains Existing Items
    Add Test Items
    Input List Command In Main Menu
    Run App
    Output Should Contain  ${BOOK}
    Output Should Contain  ${BLOG}
    Output Should Contain  ${VIDEO}

List Does Not Contain Non-Existing Items
    Add Test Book
    Input List Command In Main Menu
    Run App
    Output Should Contain  ${BOOK}
    Output Should Not Contain  ${BLOG}
    Output Should Not Contain  ${VIDEO}

List Does Not Contain Deleted Item
    Add Test Items
    Delete Test Book
    Input List Command In Main Menu
    Run App
    Output Should Not Contain  ${BOOK}
    Output Should Contain  ${BLOG}
    Output Should Contain  ${VIDEO}

*** Keywords ***
Delete Test Book
    Input Delete Command In Main Menu
    Input  Eating Animals
    Input  K
