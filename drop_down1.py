import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
cap:Dict[str,Any]={
    "platformName": "android",
    "automationName": 'uiautomator2',
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.android.contacts.activities.PeopleActivity",
    "language": "en",
    "locate": "US"
}
url = 'http://localhost:4723'
driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
time.sleep(5)
driver.find_element(by=AppiumBy.ID,value="android:id/button2").click()
driver.find_element(by=AppiumBy.ID,value="com.google.android.contacts:id/floating_action_button").click()
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.Spinner[@content-desc='Mobile Phone']").click()
time.sleep(5)
driver.find_element(by=AppiumBy.XPATH,value="//android.widget.CheckedTextView[@text='Home Fax']").click()
time.sleep(5)
