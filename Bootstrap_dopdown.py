import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_objc=Service()
driver = webdriver.Chrome(service=serv_objc)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='select2-billing_country-container']").click()
country_list = driver.find_elements(By.XPATH,"//*[@id='select2-billing_country-results']/li")
print(len(country_list))

for country in country_list:
    if country.text=="India":
        country.click()
        break
time.sleep(5)