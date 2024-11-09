import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://demoqa.com/alerts")
driver.execute_script(0,500)