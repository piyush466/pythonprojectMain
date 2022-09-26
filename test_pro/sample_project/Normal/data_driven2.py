from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import XLutils

ser = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://demo.guru99.com/test/newtours/")
path = r"C:\Users\Cliffex-Lead\Documents\practise.xlsx"
row = XLutils.getRowCount(path, "Sheet1")

for i in range(2,row+1):
    username = XLutils.readData(path,'Sheet1',i,1)
    password = XLutils.readData(path,'Sheet1',i,2)

    driver.find_element(By.NAME, "userName").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)

    driver.find_element(By.NAME, "submit").click()

    if driver.title == "Login: Mercury Tours":
        print("test passed")
        XLutils.writeData(path,'Sheet1',i,3,"test pass")

    else:
        print("test fail")
        XLutils.writeData(path,'Sheet1',i,3,'test fail')

    driver.find_element(By.LINK_TEXT, "Home").click()


