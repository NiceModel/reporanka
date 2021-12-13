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

Choose Search Command
    Input Search Command In Main Menu
    Run App
    Output Should Contain  \nVoit etsiä vinkkiä tekijän ja nimen perusteella syöttämällä hakusanan

Search Existing Item
    Add Test Items
    Input Search Command In Main Menu
    Search Test Book
    Run App
    Output Should Contain  \nHakusanalla löytyvät vinkit:\n

Search Non-Existing Item
    Add Test Items
    Input Search Command In Main Menu
    Search NonTest Book
    Run App
    Output Should Contain  Teosta ei löytynyt.

Search Items When List Is Empty
    Input Search Command In Main Menu
    Run App
    Output Should Contain  Sovellukseen ei ole tallennettu vinkkejä :(

*** Keywords ***

Search Test Book
    Input  Animals

Search NonTest Book
    Input  Testi