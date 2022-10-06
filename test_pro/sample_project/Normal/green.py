import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")

driver = webdriver.Chrome(service=object)

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Shop").click()
time.sleep(2)

newbox = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for boxes in newbox:
    name = boxes.find_element(By.XPATH,"div/h4/a").text
    print(name)
    if name == "Blackberry":
        boxes.find_element(By.XPATH,"div/button").click()
