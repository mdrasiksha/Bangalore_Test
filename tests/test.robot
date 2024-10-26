*** Settings ***
Library  AppiumLibrary

*** Variables ***
${tille}    xpath=//android.widget.TextView[@text="API Demos"]
${app_icon}     xpath=//android.widget.TextView[@content-desc="App"]
${search}   xpath=//android.widget.TextView[@content-desc="Search"]
${search_result}    xpath=//android.widget.TextView[@content-desc="Invoke Search"]
${query}    xpath=//android.widget.EditText[@resource-id="io.appium.android.apis:id/txt_query_prefill"]
${views}    xpath=//android.widget.TextView[@content-desc="Views"]
*** Test Cases ***
open_app
    open application    http://localhost:4723    platformName=Android    deviceName=1C091FDF6006K4    automationName=Uiautomator2    appPackage=io.appium.android.apis  appActivity=io.appium.android.apis.ApiDemos
    wait until page contains element    ${tille}
    click element  ${views}
