import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=object)
driver.get("https://locol.partners/")
driver.maximize_window()
driver.find_element(By.ID, "identifier").send_keys("piyush.dravyakar@gmail.com")
driver.find_element(By.ID, "password").send_keys("piyush@123")
time.sleep(2)
tex = driver.find_element(By.XPATH, "//button[text()='Sign In']").text
driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
time.sleep(8)
print(tex)
time.sleep(2)

def waittime():
    time.sleep(2)

allname = driver.find_elements(By.XPATH,"//div[@class='table_user d-flex align-items-center']")
for all in allname:
    name = all.find_element(By.XPATH,"p").text
    print(name)
    if name == "Chilly Burger":
        print("yes")
        all.find_element(By.XPATH, "(//td/label/div/span)").click()
        # break
        # all.find_element(By.XPATH,"(//td/label/div/span)").click()
waittime()
driver.find_element(By.XPATH,"//button[@type='button']").click()
waittime()
driver.find_element(By.CSS_SELECTOR,"#up_file").send_keys(r"C:\Users\Cliffex-Lead\Downloads\udta-punjab.jpg")
waittime()
driver.find_element(By.CSS_SELECTOR,"#up_thumbnail_file").send_keys(r"C:\Users\Cliffex-Lead\Downloads\udta-punjab.jpg")
waittime()
driver.find_element(By.XPATH,"//button[text()='Save Changes']").click()
waittime()
driver.find_element(By.XPATH,"(//a)[5]").click()






























# document.getElementById("6321cc3ac4243e7439930336").click()









# for names in allname:
#     print(names)































# name = driver.find_elements(By.XPATH, "//div[@class='table_user d-flex align-items-center']")
# # //label[@class='wrap_checkbox unset_position']/span
# for n in name:
#     # print(n.text)
#     matck = n.find_element(By.XPATH,"p").text
#     print(matck)
#     if matck == "chicken":
#         n.find_element(By.XPATH, "//label[@class='wrap_checkbox unset_position']/span").click()





