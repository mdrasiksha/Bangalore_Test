import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
cap:Dict[str,Any]={
    "platformName": "android",
    "automationName": 'uiautomator2',
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.dialer",
    "appActivity": "com.android.dialer.main.impl.MainActivity",
    "language": "en",
    "locate": "US"
}
url = 'http://localhost:4723'
driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
time.sleep(5)
driver.find_element(by=AppiumBy.CLASS_NAME,value="android.widget.FrameLayout").click()


