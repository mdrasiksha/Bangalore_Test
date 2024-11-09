import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
cap:Dict[str,Any]={
    "platformName": "android",
    "automationName": 'uiautomator2',
    "deviceName": "emulator-5554",
    "appPackage":"com.android.settings",
    "appActivity": ".Settings",
    "language": "en",
    "locate": "US"
}
url = 'http://localhost:4723'
driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
time.sleep(5)
device_size = driver.get_window_size()
print(device_size)
screen_Width = device_size['width']
screen_Height = device_size['height']
print(screen_Width)
print(screen_Height)
startX = screen_Width/2
endY = screen_Width/2
startY = screen_Height*8/9
endY = screen_Width/9