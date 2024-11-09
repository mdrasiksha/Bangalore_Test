import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(5)
scroll_test=driver.find_element(By.XPATH,"//*[@id='desktop-2']/div/div/div[1]")
act=ActionChains(driver)
act.scroll_to_element(scroll_test).perform()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='anonCarousel2']/ol/li[1]/div/div/a/div[2]/span/span[2]").click()
time.sleep(5)
expected_title=driver.find_element(By.XPATH,"//*[@id='productTitle']")
actual_title=driver.find_element(By.XPATH,"//*[@id='productTitle']")
if actual_title==expected_title:
    print("pass")

