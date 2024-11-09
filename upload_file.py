import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
driver.maximize_window()
driver.find_element(By.NAME,"upfile").click()
time.sleep(5)