*** Settings ***
Resource  resource.robot
Test Setup  Clear Data

*** Variables ***
${BOOK}  id: 0000, tyyppi: Book, tiedot: Jonathan Safran Foer: Eating Animals (2009)
${BOOK_TITLE}	Eating Animals
${BOOK_CREATOR}	Jonathan Safran Foer
${BLOG}  id: 0000, tyyppi: Blog, tiedot: Pedro Medeiros: Pixel Grimoire, How to start making pixel art #6, 8.1.2019, (https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-6-a74f562a4056)
${BLOG_TITLE}	How to start making ...
${BLOG_CREATOR}	Pedro Medeiros
${VIDEO}  id: 0000, tyyppi: Video, tiedot: Studio Killers: Jenny (I Wanna Ruin Our Friendship) OFFICIAL MUSIC VIDEO, https://youtu.be/hyj4JFSErrw, (24.12.2015)
${VIDEO_TITLE}	Jenny (I Wanna Ruin ...
${VIDEO_CREATOR}	Studio Killers


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
    Output Should Contain  ${BOOK_TITLE}
    Output Should Contain  ${BOOK_CREATOR}
    Output Should Contain  ${BLOG_TITLE}
    Output Should Contain  ${BLOG_CREATOR}
    Output Should Contain  ${VIDEO_TITLE}
    Output Should Contain  ${VIDEO_CREATOR}

List Does Not Contain Non-Existing Items
    Add Test Book
    Input List Command In Main Menu
    Run App
    Output Should Contain  ${BOOK_TITLE}
    Output Should Contain  ${BOOK_CREATOR}
    Output Should Not Contain  ${BLOG_TITLE}
    Output Should Not Contain  ${BLOG_CREATOR}
    Output Should Not Contain  ${VIDEO_TITLE}
    Output Should Not Contain  ${VIDEO_CREATOR}

List Does Not Contain Deleted Item
    Add Test Items
    Delete Test Book
    Run App
    Clear Outputs
    Input List Command In Main Menu
    Run App
    Output Should Not Contain  ${BOOK_TITLE}
    Output Should Not Contain  ${BOOK_CREATOR}
    Output Should Contain  ${BLOG_TITLE}
    Output Should Contain  ${BLOG_CREATOR}
    Output Should Contain  ${VIDEO_TITLE}
    Output Should Contain  ${VIDEO_CREATOR}

*** Keywords ***
Delete Test Book
    Input Delete Command In Main Menu
    Input	1001
    Input  K
