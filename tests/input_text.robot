*** Settings ***
Library  AppiumLibrary
Variables  ../config/appium_config.py
Resource

*** Variables ***
${URL}      http://localhost:4723
${text_box}     xpath=//android.widget.TextView[@content-desc="Text"]


*** Test Cases ***
input_text_box
    open application  ${URL}    platformName=Android    deviceName=1C091FDF6006K4    automationName=Uiautomator2    appPackage=io.appium.android.apis  appActivity=io.appium.android.apis.ApiDemos
    click element  ${text_box}
    sleep  5s
    click element  xpath=//android.widget.TextView[@content-desc="LogTextBox"]
    click element  xpath=//android.widget.Button[@content-desc="Add"]
    input text  xpath=//android.widget.TextView[@resource-id="io.appium.android.apis:id/text"]      password
    sleep   10s
    ${actual}   get text   xpath=//android.widget.TextView[@resource-id="io.appium.android.apis:id/text"]
    should be equal  ${actual}  password
    clear text  xpath=//android.widget.TextView[@resource-id="io.appium.android.apis:id/text"]
