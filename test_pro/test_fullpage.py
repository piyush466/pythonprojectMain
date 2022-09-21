import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#radio Buttons
radio = driver.find_elements(By.NAME, "radioButton")

def test_radioBtn():
    print("Radio button is exicute one by one")
    for btn in radio:
            print("!!!!!!!!!!!!!!!!!!")
            time.sleep(1)
            btn.click()


#suggesion drop down






