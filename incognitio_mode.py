import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
ops= Options()
ops.add_argument("--incognito")
#serv_objc=Service()
driver=webdriver.Chrome(options=ops)
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(5)