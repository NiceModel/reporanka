*** Settings ***
Resource  resource.robot
Test Setup  Open Application

*** Test Cases ***
Start Succeeds
    Output Should Contain  \nLUKUVINKKIKIRJASTO

Function Add Starts
    Input Function  1
    Output Should Contain  \nLUKUVINKKIKIRJASTO
    # Output Should Contain  Lisätään lukuvinkki...

Function List Starts
    Input Function  2
    Output Should Contain  \nLUKUVINKKIKIRJASTO
    # Output Should Contain  Listataan lukuvinkit...

Function Search Not Starting Yet
    Input Function  3
    Output Should Contain  \nLUKUVINKKIKIRJASTO
    # Output Should Contain  Komentoa ei löytynyt, yritä uudelleen.

Unvalid Function
    Input Function  6
    Output Should Contain  \nLUKUVINKKIKIRJASTO
    # Output Should Contain  Komentoa ei löytynyt, yritä uudelleen.

Closing Should Succeed
    Input Function  0
    Output Should Contain  \nLUKUVINKKIKIRJASTO
    # Output Should Contain  Heido!
    Close Application

*** Keywords ***
Open Application
    Main Page Should Be Open

Enter Function
    Input New Command

Close Application
    Exit