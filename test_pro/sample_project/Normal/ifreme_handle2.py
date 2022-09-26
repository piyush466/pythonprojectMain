from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#Option Class
options = webdriver.ChromeOptions()
# options.add_argument("headless")
print("this is --start-maximized")
options.add_argument("--start-maximized")

object = Service(r"C:\Users\Cliffex-Lead\Desktop\New-folder\chromedriver.exe")
driver = webdriver.Chrome(service=object,options=options)
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
# driver.maximize_window()

driver.execute_script("window.scrollTo(0,350)")
driver.switch_to.frame("frm1")

driver.find_element(By.CSS_SELECTOR, "#selectnav1").click()
option = Select(driver.find_element(By.ID, "selectnav1"))
option.select_by_visible_text("-- Core Java")
print(driver.title)
title = (driver.title)

assert title in "Frames Practice - H Y R Tutorials"
print("Execution complete")
driver.quit()




