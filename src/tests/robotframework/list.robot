*** Settings ***
Resource  resource.robot

*** Variables ***
${BOOK}  Book - Meri: Meemikirja (2021)

*** Test Cases ***
Choose Function List With Empty List
    Input List Command In Main Menu
    Run App
    Output Should Contain  Sovellukseen ei ole tallennettu vinkkejä :(

Choose Function List With Some List
    Add Test Book
    Input List Command In Main Menu
    Run App
    Output Should Contain  \nLukuvinkkilista:\n

Function List Lists Existing Item
    Add Test Book And Add Command
    Input List Command In Main Menu
    Run App
    Output Should Contain  ${BOOK}

Function List Does Not List Non-existing Item
    Input List Command In Main Menu
    Run App
    Output Should Not Contain  ${BOOK}

# Function List Should Not List Deleted Item
#     Delete Book
#     Input List Command In Main Menu
#     Run App
#     Output Should Not Contain   ${BOOK}