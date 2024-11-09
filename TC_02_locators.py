from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service()
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://www.automationpractice.pl/index.php")
count = driver.find_element(By.CLASS_NAME,"homeslider-container")
print(len("count"))
link_count = driver.find_element(By.CLASS_NAME,"row")
print(len("link_count"))