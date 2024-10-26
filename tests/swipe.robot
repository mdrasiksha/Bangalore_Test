*** Settings ***
Library  AppiumLibrary
Library  AppiumLibrary
#Variables  ../config/appium_config.py

*** Variables ***
${URL}  http://localhost:4723
${source}    xpath=//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_1"]
${target}   xpath=//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_2"]
${views}    xpath=//android.widget.TextView[@content-desc="Views"]
${drag}     xpath=//android.widget.TextView[@content-desc="Drag and Drop"]

*** Test Cases ***
swipe_function_check
    open application  ${URL}    platformName=Android    deviceName=1C091FDF6006K4    automationName=Uiautomator2    appPackage=io.appium.android.apis  appActivity=io.appium.android.apis.ApiDemos
    click element  ${views}
    sleep   5s
    swipe       start_x=0    start_y=0       end_x=500     end_y=0       duration=1000
