import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
act = ActionChains(driver)
act.context_click(button).perform()
time.sleep(5)