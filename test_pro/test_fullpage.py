import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#radio Buttons
radio = driver.find_elements(By.NAME, "radioButton")

# def test_radioBtn():
print("Radio button is exicute one by one")
for btn in radio:
    print("!!!!!!!!!!!!!!!!!!")
    time.sleep(1)
    btn.click()

time.sleep(2)
#dropdown list
def dropdown():
    sel = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
    sel.select_by_visible_text("Option2")
dropdown()

#scroll down
driver.execute_script("window.scrollTo(0,300)")

#mouse hover
action = ActionChains(driver)
mouse = driver.find_element(By.XPATH, "//button[@id='mousehover']")
action.move_to_element(mouse).perform()
time.sleep(2)
driver.execute_script("window.scrollTo(300,0)")




#multiple checkbox selecting
def checkboxx():
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    print("!!!!!!!!!!!!!!!!!!!!!")
    for check in checkboxes:
        print("!!!!!!!!!!!!!!!!!!!!!")
        check.click()
checkboxx()

#alerts handle
def alert():
    driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()
    time.sleep(2)
    alert.dismiss()

alert()



#suggesion drop down with using implisitly wait and explicitly wait

# driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys("in")
# driver.implicitly_wait(10)
#
# contry = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")
#
# def test_contry():
#     print("Radio button is exicute one by one")
#     for con in contry:
#         name = con.find_element(By.XPATH, "div").text
#         if name == "India":
#             con.click()

time.sleep(3)
#
# #handle new window
driver.find_element(By.LINK_TEXT, "Open Tab").click()
window = driver.window_handles

driver.switch_to.window(window[1])
print(driver.title)
time.sleep(2)
driver.switch_to.window(window[0])
print(driver.title)






























