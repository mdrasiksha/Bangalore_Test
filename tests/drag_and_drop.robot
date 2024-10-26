*** Settings ***
Library  AppiumLibrary
#Variables  ../config/appium_config.py

*** Variables ***
${URL}  http://localhost:4723
${source}    xpath=//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_1"]
${target}   xpath=//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_2"]
${views}    xpath=//android.widget.TextView[@content-desc="Views"]
${drag}     xpath=//android.widget.TextView[@content-desc="Drag and Drop"]

*** Test Cases ***
drag_and_drop function
    open application  ${URL}    platformName=Android    deviceName=1C091FDF6006K4    automationName=Uiautomator2    appPackage=io.appium.android.apis  appActivity=io.appium.android.apis.ApiDemos
    click element  ${views}
    click element   ${drag}
    drag and drop   ${source}   ${target}
    sleep  5s
    close application
*** Keywords ***
