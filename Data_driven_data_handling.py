import time
import excelutility
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_objc=Service()
driver = webdriver.Chrome(service=serv_objc)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
file = "C:\\Users\\10720021\\Downloads\\calculator.xlsx"
rows=excelutility.getRowCount()
for r in range(2,rows+1):
    price=excelutility.readData(file,"Sheet1",r,1)
    rateofinterest=excelutility.readData(file,"Sheet1",r,3)
    per1 = excelutility.readData(file,"Sheet1",r,3)
    per2 = excelutility.readData(file,"Sheet1",r,4)

    driver.find_element(By.ID,"principal").send_keys(per1)


