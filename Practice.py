from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver. common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
el=driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[2]/div[2]/div/div/div/div/img")
el.click()
el.send_keys(Keys.DOWN)
