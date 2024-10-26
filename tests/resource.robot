*** Settings ***
Library  AppiumLibrary
Variables  ../config/appium_config1.yaml

*** Keywords ***
app_launch
    open application  ${appium_server_url}      ${desired_capabilities}

close application
    close application




close application

click element