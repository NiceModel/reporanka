*** Settings ***
Resource  resource.robot

*** Test Cases ***
Application Starts Succesfully
    Run App
    Output Should Contain  \nLUKUVINKKIKIRJASTO

Main Menu Starts Successfully
    Run App
    Output Should Contain  \nValitse toiminto\n (1) lisää\n (2) listaa\n (3) poista\n (0) lopeta\n

Add Command Can Be Chosen
    Input Add Command In Main Menu
    Run App
    Output Should Contain  \nMitä lisätään?\n (1) kirja\n (2) video\n (3) blogi\n (4) takaisin valikkoon\n (0) lopeta

Back To Main Menu Succesfully
    Input Add Command In Main Menu
    Input Back To Main Menu Command In Add Menu
    Run App
    Output Should Contain  \nValitse toiminto\n (1) lisää\n (2) listaa\n (3) poista\n (0) lopeta\n

Invalid Input In Main Menu
    Input  666
    Run App
    Output Should Contain  Komentoa ei löytynyt, yritä uudelleen.

Quit Application Succesfully From Main Menu
    Input Quit Command
    Run App
    Output Should Contain  Kiitti & moi!

Quit Application Succesfully From Add Menu
    Input Add Command In Main Menu
    Input Quit Command
    Run App
    Output Should Contain  Kiitti & moi!
