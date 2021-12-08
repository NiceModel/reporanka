*** Settings ***
Library  ./../../libraries/AppLibrary.py

*** Keywords ***
Run App
    Run Application

Input Empty
    Input   ''

Input Quit Command
    Input  0

Input Add Command In Main Menu
    Input  1

Input List Command In Main Menu
    Input  2

Input Delete Command In Main Menu
    Input  3

Input Add Book Command In Add Menu
    Input  1

Input Add Video Command In Add Menu
    Input  2

Input Add Blog Command In Add Menu
    Input  3

Input Back To Main Menu Command In Add Menu
    Input  4

Add New Book
    [Arguments]  ${author}  ${title}  ${published}
    Input  ${author}
    Input  ${title}
    Input  ${published}