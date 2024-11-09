from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
mywait=WebDriverWait(driver,10,ignored_exceptions=[ExceptionGroup])#explicit wait declaration
driver.get("https://www.google.com/")
driver.maximize_window()
searchbox=driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
searchbox.submit()
search_link=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
search_link.click()
driver.quit()