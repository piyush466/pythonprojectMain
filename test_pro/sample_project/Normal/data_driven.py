from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import XLutils

option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
# option.add_argument("headless")

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=object,options=option)

driver.get("https://demo.guru99.com/test/newtours/")
path = r"C:\Users\Cliffex-Lead\Documents\piyushexcel.xlsx"
row = XLutils.getRowCount(path,'Sheet1')
for r in range(2,row+1):
    username = XLutils.readData(path,'Sheet1',r,1)
    password = XLutils.readData(path,'Sheet1',r,2)

    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.XPATH, "//input[@name='submit']").click()

    if driver.title == "Login: Mercury Tours" :
        print("test is passes")
        XLutils.writeData(path,"Sheet1",r,3,"test passed")

    else:
        print("test failed")
        XLutils.writeData(path, "Sheet1", r, 3, "test failed")

    driver.find_element(By.LINK_TEXT, "Home").click()






