*** Settings ***
Resource  resource.robot

*** Test Cases ***
Start Application Succesfully
    Run App
    Output Should Contain  \nValitse toiminto\n (1) lisää\n (2) listaa\n (3) poista\n (0) lopeta\n

Choose Function Add
    Input Add Command In Main Menu
    Run App
    Output Should Contain  \nMitä lisätään?\n (1) kirja\n (2) video\n (3) blogi\n (4) takaisin valikkoon\n (0) lopeta

Choose Function List
    Input List Command In Main Menu
    Run App
    Output Should Contain  Sovellukseen ei ole tallennettu vinkkejä :(

Invalid Input In Main Menu
    Input  666
    Run App
    Output Should Contain  Komentoa ei löytynyt, yritä uudelleen.
