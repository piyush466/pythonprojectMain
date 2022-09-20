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

prod = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for all in prod:
    name = all.find_element(By.XPATH, "div/h4/a").text
    if name == 'Nokia Edge':
        all.find_element(By.XPATH, "div/button").click()

driver.execute_script("window.scrollTo(1000,0)")

driver.find_element(By.XPATH, "//div[@id='navbarResponsive']/ul/li/a").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(1)

#input value india
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, "India")))
time.sleep(1)
driver.find_element(By.LINK_TEXT,"India").click()

#click on checkbox
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

#click on purches
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#assertion
success = driver.find_element(By.CLASS_NAME, "alert-success").text

assert " Thank you!" in success




    





