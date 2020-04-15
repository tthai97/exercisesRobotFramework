*** Settings ***
Library    ../../../apps/web_apps/web_functions.py       WITH NAME    browser_01
Library    ../../../apps/web_apps/web_functions.py       WITH NAME    browser_02        

*** Variables ***
*** Test Cases ***

ADA010 create new project - Login and create new project- WIN1
    Log To Console    Hello    
    browser_01.Open Browser       http://11.11.7.10/login
    browser_01.Input Username Password Login Page    hai    hai
    browser_01.Click Login Button
    sleep    5
    browser_01.Click New Project Button Dash Board Page
    browser_01.Input Project Name Dash Board Page    hai
    browser_01.Input Project Description Dash Board Page    hai
    sleep    2
    browser_01.Click Cancel Project Button Dash Board Page
    sleep    2
    browser_01.Add New Project Dash Board Page    hai    hai
    browser_01.Close Browser
    
ADA011 create new project with emty name - Login and create new project- WIN1
    Log To Console    Hello    
    browser_01.Open Browser       http://11.11.7.10/login
    browser_01.Input Username Password Login Page    hai    hai
    browser_01.Click Login Button
    sleep    5
    browser_01.Click New Project Button Dash Board Page
    browser_01.Click Create Project Button Dash Board Page
    #Verify 'you must ne enter project name'
    browser_01.Input Project Description Dash Board Page    hai
    browser_01.Click Create Project Button Dash Board Page
    #Verify 'you must ne enter project name'
    #Result Create unsuccessfully and you must be enter project name
    
    browser_01.Close Browser