import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys("in")
driver.implicitly_wait(10)

contry = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")

for con in contry:
    name = con.find_element(By.XPATH, "div").text
    if name == "India":
        con.click()
