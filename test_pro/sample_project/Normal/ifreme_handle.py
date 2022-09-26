import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,700)")
driver.switch_to.frame("courses-iframe")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Blog").click()

driver.get("https://locol.partners/")
