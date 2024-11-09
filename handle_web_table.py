import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)
driver.maximize_window()
#count number of rows and columns
rows=len(driver.find_element(By.NAME,"BookTable")
print(rows)