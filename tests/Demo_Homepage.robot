*** Settings ***
Library  AppiumLibrary
Variables  ../config/appium_config.py
Resource

*** Variables ***
${URL}  http://localhost:4723/wd/hub
${tile}  xpath=//android.widget.TextView[@text="API Demos"]

*** Test Cases ***
demo home page
    open application  ${URL}    platformName=Android    deviceName=1C091FDF6006K4    automationName=Uiautomator2    appPackage=io.appium.android.apis  appActivity=io.appium.android.apis.ApiDemos
    sleep  5s
    wait until page contains element    ${tile}
    close application

*** Keywords ***
