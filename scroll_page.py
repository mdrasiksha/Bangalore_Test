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
#driver.execute_script("window.scrollBy(0,500)")
#time.sleep(5)
cat=driver.find_element(By.XPATH,"//*[@id='navBackToTop']/div/span")
driver.execute_script("arguments[0].scrollIntoView",cat)
