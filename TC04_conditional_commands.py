from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.orangehrm.com/")
title1=driver.find_element(By.NAME,"action_request")
print(title1.is_displayed())
search_box=driver.find_element(By.NAME,"EmailHomePage")
print(search_box.is_enabled())
select_box=

