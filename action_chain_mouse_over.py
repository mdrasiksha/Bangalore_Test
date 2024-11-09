import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://omayo.blogspot.com/")
act = ActionChains(driver)
menu=driver.find_element(By.ID,"blogsmenu")
act.move_to_element(menu).perform()
time.sleep(5)