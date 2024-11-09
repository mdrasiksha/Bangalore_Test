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
time.sleep(5)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value = "Views").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value = "Date Widgets").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value = "1. Dialog").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value = "change the date").click()
#driver.find_element(by=AppiumBy.ID,value = "android:id/month_view").click()
#ayear = driver.find_element(by=AppiumBy.ID,value="android:id/date_picker_header_year")
amonth = driver.find_element(by=AppiumBy.ID,value="android:id/date_picker_header_date")
while amonth == "Aug":
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Previous month").click()
    print("pass")

