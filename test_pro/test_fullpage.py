import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#radio Buttons
# radio = driver.find_elements(By.NAME, "radioButton")
#
# def test_radioBtn():
#     print("Radio button is exicute one by one")
#     for btn in radio:
#             print("!!!!!!!!!!!!!!!!!!")
#             time.sleep(1)
#             btn.click()


#suggesion drop down with using implisitly wait and explicitly wait

driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys("ind")
driver.implicitly_wait(10)

contry = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")

for con in contry:
    name = con.find_element(By.XPATH, "div").text
    if name == "India":
        con.click()



















