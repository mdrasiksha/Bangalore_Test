import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://text-compare.com/")
box1=driver.find_element(By.NAME,"text1")
box2=driver.find_element(By.NAME,"text2")
box1.send_keys("welcome to my world")
act = ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(5)
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
box2.click()
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(5)
