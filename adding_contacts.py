import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
cap:Dict[str,Any]={
    "platformName": "android",
    "automationName": 'uiautomator2',
    "deviceName": "emulator-5554",
    "appPackage":"com.google.android.dialer",
    "appActivity": "com.android.dialer.main.impl.MainActivity",
    "language": "en",
    "locate": "US"
}
url = 'http://localhost:4723'
driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
time.sleep(5)
driver.find_element(by=AppiumBy.XPATH,value="(//android.widget.ImageView[@resource-id='com.google.android.dialer:id/navigation_bar_item_icon_view'])[2]").click()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located(AppiumBy.ACCESSIBILITY_ID, value="Create contact")
el1 = driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/permission_allow_button")
el1.click()