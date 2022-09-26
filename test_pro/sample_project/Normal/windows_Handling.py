import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=opt)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Open Tab").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)
time.sleep(2)
driver.switch_to.window(windows[0])
print(driver.title)
time.sleep(2)
# driver.execute_script("window.scrollTO(0,300)")
driver.execute_script("window.scrollTo(0,300)")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()




