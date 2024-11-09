from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver. common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.NAME, "username").send_keys("student")
driver.find_element(By.NAME,"password").send_keys("Password123")
driver.find_element(By.ID,"submit").click()
#actual_title=driver.find_element(By.XPATH,"//*[@id='loop-container']/div/article/div[1]/h1")
actual_title=driver.title
print(actual_title)
expected_title="Logged In Successfully | Practice Test Automation"
if actual_title==expected_title:
    print("pass")
else:
    print("fail")