import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.implicitly_wait(5)
driver.get("https://jqueryui.com/datepicker/")
time.sleep(5)
driver.switch_to.frame(0)

#mm/dd/yyyy
driver.find_element(By.ID,"datepicker").send_keys("05/30/2023")
time.sleep(5)

#
"""year="2025"
month="April"
date="30"
driver.find_element(By.ID,"datepicker").click() #open the date picker element
next_button=driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span")
while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break
    else:
        next_button.click()
time.sleep(5)"""





