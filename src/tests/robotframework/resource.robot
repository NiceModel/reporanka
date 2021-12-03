*** Settings ***
Library  ./libraries/AppLibrary.py

# *** Variables ***
# ${RUNS}  app._self.running

*** Keywords ***
Run App
    Run Application
    # Input  ${RUNS} == True

Input Quit Command
    Input  0

Input Add Command
    Input  1

Input List Command
    Input  2

Add New Book
    [Arguments]  ${author}  ${title}  ${published}
    Input  ${author}
    Input  ${title}
    Input  ${published}

# Input New Command
#     Input  new

# Exit
#     Input  ${RUNS} == False