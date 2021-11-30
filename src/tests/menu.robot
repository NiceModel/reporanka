*** Settings ***
Resource  resource.robot

*** Test Cases ***
Start Application Succesfully
    Run App
    Output Should Contain  \nLUKUVINKKIKIRJASTO

Choose Function Add
    Input Add Command
    Run App
    Output Should Contain  Lisätään lukuvinkki...

Choose Function List
    Input List Command
    Run App
    Output Should Contain  Listataan lukuvinkit...

Invalid Input In Main Menu
    Input  666
    Run App
    Output Should Contain  Komentoa ei löytynyt, yritä uudelleen.
