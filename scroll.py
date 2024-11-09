import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


cap:Dict[str,Any]={
    "platformName": "android",
    "automationName": 'uiautomator2',
    "deviceName": "PD21ADD464007181",
    "appPackage":"io.appium.android.apis",
    "appActivity": "io.appium.android.apis.ApiDemos",
    "language": "en",
    "locate": "US"
}
url = 'http://localhost:4723'
driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="Views").click()
time.sleep(5)

#test = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value = "Date Widgets").click()
#driver.execute_script("mobile: scroll”, {‘direction’: ‘down’})



