import time

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://demo.nopcommerce.com/")
driver.get("https://amazon.com/")
driver.back()
time.sleep(6)
driver.forward()
driver.refresh()
driver.quit()

