import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
username = input("Enter your username:- ")
password = input("Enter your password:- ")
# webdriver.ChromeOptions()
chrome = webdriver.ChromeOptions()
chrome.add_argument("--start-maximized")
object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver= webdriver.Chrome(service=object,options=chrome)

driver.get("https://www.facebook.com/")


driver.find_element(By.CSS_SELECTOR,"#email").send_keys(username)
driver.find_element(By.CSS_SELECTOR,"#pass").send_keys(password)
tex = driver.find_element(By.XPATH,"//h2").text
print(tex)
driver.find_element(By.NAME,"login").click()
time.sleep(4)
assert tex == "Facebook helps you connect and share with the people in your life."

# driver.find_element(By.NAME,"login").click()

driver.close()