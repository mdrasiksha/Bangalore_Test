import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import os
from selenium.webdriver.common.action_chains import ActionChains
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://testautomationpractice.blogspot.com/")
country=driver.find_element(By.ID,"country")
drop_down=Select(country)
drop_down.select_by_visible_text("India")
time.sleep(5)
drop_down.select_by_index(3)
time.sleep(5)
list= drop_down.options
for i in list:
    print(i.text)