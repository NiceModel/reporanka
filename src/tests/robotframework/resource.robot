*** Settings ***
Library  ./../../libraries/AppLibrary.py

*** Keywords ***
Run App
    Run Application

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
