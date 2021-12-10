*** Settings ***
Library  ./../../libraries/AppLibrary.py

*** Keywords ***
Run App
    Run Application

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
    Input Add Command In Main Menu
    Input Add Book Command In Add Menu
    Input  ${author}
    Input  ${title}
    Input  ${published}

Add New Video
    [Arguments]  ${creator}  ${title}  ${url}  ${published}
    Input Add Command In Main Menu
    Input Add Video Command In Add Menu
    Input  ${creator}
    Input  ${title}
    Input  ${url}
    Input  ${published}

Add New Blog
    [Arguments]  ${blogger}  ${blog}  ${post}  ${url}  ${published}
    Input Add Command In Main Menu
    Input Add Blog Command In Add Menu
    Input  ${blogger}
    Input  ${blog}
    Input  ${post}
    Input  ${url}
    Input  ${published}

Add Test Book
    Add New Book  Jonathan Safran Foer  Eating Animals  2009

Add Test Video
    Add New Video  Studio Killers  Jenny (I Wanna Ruin Our Friendship) OFFICIAL MUSIC VIDEO  https://youtu.be/hyj4JFSErrw  24.12.2015

Add Test Blog
    Add New Blog  Pedro Medeiros  Pixel Grimoire  How to start making pixel art #6  https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-6-a74f562a4056  8.1.2019

Add Test Items
    Add Test Book
    Add Test Video
    Add Test Blog

Clear Data
    Clear Test File
