import time
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
serv_obj=Service()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
#driver.execute_script("window.scrollTo(0,500);")
#driver.find_element(By.XPATH,"//*[@id='alertButton']").click()
time.sleep(5)
driver.get_cookies()
driver.add_cookie()
driver.delete_cookie()






