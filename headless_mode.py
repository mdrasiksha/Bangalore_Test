from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_objc=Service()
    #driver=webdriver.Chrome(service=serv_objc)
    ops=webdriver.ChromeOptions()
    ops.headless()
    driver=webdriver.Chrome(service=serv_objc,option=ops)
    return driver

mydriver = headless_chrome()
mydriver.get("https://demo.nopcommerce.com/")
print("pass")
print(mydriver.current_url)