from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_objc=Service()
driver=webdriver.Chrome(service=serv_objc)
driver.get("https://www.linkedin.com/in/ajeykulkarni/details/experience/")
cookies=driver.get_cookies()
print("size of cookies",len(cookies))
driver.add_cookie({"name":"test data","value":"123456"})
print("size of cookies",len(cookies))
#delete=driver.delete_cookie()
driver.quit()
#deleting specfic cookies from the browser
driver.delete_cookie("test data")
print("size of cookies",len(cookies))


