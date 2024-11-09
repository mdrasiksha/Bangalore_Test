import time

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
#driver.find_element(By.ID,"sunday").click()
#time.sleep(5)
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox'and contains(@id,'day')]")
#for i in checkboxes:
#    weekname=i.get_attribute('id')
#    if weekname=="Monday" or weekname=="Friday":
#        i.click()
#time.sleep(10)
#
#select last 2 checkboxes
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()




