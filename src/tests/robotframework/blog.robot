*** Settings ***
Resource  resource.robot
Test Setup  Add Test Blog

*** Test Cases ***

Add Blog With Correct Details
    Add New Blog  Roxy & Ben  SO VEGAN  Butternut Squash Wellington  https://www.wearesovegan.com/butternut-squash-wellington/  5.12.2019
    Run App
    Output Should Contain  \nUusi lukuvinkki lisätty.

Add Duplicate Blog
    Add New Blog  Pedro Medeiros  Pixel Grimoire  How to start making pixel art #6  https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-6-a74f562a4056  8.1.2019
    Run App
    Output Should Contain  \nLukuvinkki on jo tallennettu aiemmin!

Add Blog With No Blogger
    Add New Blog  ${EMPTY}  SO VEGAN  Butternut Squash Wellington  https://www.wearesovegan.com/butternut-squash-wellington/  5.12.2019
    Run App
    Output Should Contain  Blogin kirjoittaja on lisättävä!

Add Blog With No Blog Name
    Add New Blog  Roxy & Ben  ${EMPTY}  Butternut Squash Wellington  https://www.wearesovegan.com/butternut-squash-wellington/  5.12.2019
    Run App
    Output Should Contain  Blogin nimi on lisättävä!

Add Blog With No Post Title
    Add New Blog  Roxy & Ben  SO VEGAN  ${EMPTY}  https://www.wearesovegan.com/butternut-squash-wellington/  5.12.2019
    Run App
    Output Should Contain  Postauksen nimi on lisättävä!

Add Blog With No Url
    Add New Blog  Roxy & Ben  SO VEGAN  Butternut Squash Wellington  ${EMPTY}  5.12.2019
    Run App
    Output Should Contain  Blogin osoite on lisättävä!

Add Blog With No Publishing Date
    Add New Blog  Roxy & Ben  SO VEGAN  Butternut Squash Wellington  https://www.wearesovegan.com/butternut-squash-wellington/  ${EMPTY}
    Run App
    Output Should Contain  Postauksen julkaisupäivä on lisättävä!
