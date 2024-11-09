import time

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://admin-demo.nopcommerce.com/Admin/Store/List")
driver.maximize_window()
#click on the link
driver.find_element(By.PARTIAL_LINK_TEXT,"nopCommerce").click()
time.sleep(5)
