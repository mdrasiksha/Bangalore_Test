"""from selenium import webdriver
from selenium.webdriver.chrome.service import service
serv_obj=Service
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.google.com")"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-1.html")
driver.maximize_window()
test = ActionChains(driver)
time.sleep(5)
source = driver.find_element(By.ID,"box1")
target = driver.find_element(By.ID,"dropBox")
test.drag_and_drop(source,target).perform()
time.sleep(5)



