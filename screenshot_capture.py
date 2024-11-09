from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.save_screenshot("C:\\Users\\10720021\\PycharmProjects\\selenium\\test1\\homepage.png")  #save the file
driver.save_screenshot(os.getcwd()+"\\homepage1.png") #current location
driver.get_screenshot_as_png()
driver.get_screenshot_as_base64()
driver.quit()
