from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
#login_ele=driver.find_element(By.LINK_TEXT,"Log in")
#login_ele.click()
element=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(element))
print(element[0].text)
for i in element:
    print(i.text)



