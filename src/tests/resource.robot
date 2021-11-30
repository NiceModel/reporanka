*** Settings ***
Library  ../AppLibrary.py

*** Variables ***
${RUNS}  app._self.running

*** Keywords ***
Main Page Should Be Open
    Run Application
    Input  ${RUNS} == True

Input Function
    [Arguments]  ${vastaus}
    Input  ${vastaus}

Input New Command
    Input  new

Exit
    Input  ${RUNS} == False