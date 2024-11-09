import time
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
serv_obj=Service()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu")
drop_country=driver.find_element(By.XPATH,"//*[@id='post-2646']/div[2]/div/div/div/p/select")
time.sleep(5)
act= ActionChains(driver)
act.context_click(drop_country).perform()
