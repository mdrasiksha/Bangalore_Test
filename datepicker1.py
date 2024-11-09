import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import select
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.implicitly_wait(5)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.NAME,"dob").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='dob']").click()
date_picker_month= select("driver.find_element(By.XPATH,'//input[@id='dob']').click()")
date_picker_month.select_by_visible_text("Dec")  #month

