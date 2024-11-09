from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()



