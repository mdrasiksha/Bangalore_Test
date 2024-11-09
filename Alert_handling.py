import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_objc=Service()
driver = webdriver.Chrome(service=serv_objc)
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
driver.switch_to.alert()
