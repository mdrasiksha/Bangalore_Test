import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str,Any]={
    "platformName": "ios",
    "automationName": 'XCUITest',
    "deviceName": "iPhone 12 pro",
    "appPackage": "io.appium.android.apis",
    "appActivity": "io.appium.android.apis.ApiDemos",
    "language": "en",
    "locate": "US"
}