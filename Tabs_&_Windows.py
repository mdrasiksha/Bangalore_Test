from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.action_chains import ActionChains
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
#driver.get("https://www.dummyticket.com/")
#loginlink = Keys.CONTROL+keys.RETURN
#driver.find_element(By.LINK_TEXT,"BUY TICKET").send_keys(loginlink)

##same browser_two tab
driver.get("https://www.opencart.com")
driver.switch_to.new_window('tab')
driver.get("https://www.orangehrm.com")

##double browser
driver.get("https://www.opencart.com")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com")


