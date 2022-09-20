import time

from selenium.webdriver.common.by import By

# import XLutils

from selenium import webdriver

user = input("Enter your song name:- ")
driver = webdriver.Chrome(executable_path=r"C:\Users\Cliffex-Lead\Desktop\chrome\chromedriver.exe")



driver.get("https://www.youtube.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='search_query']").send_keys(user)
driver.find_element(By.CSS_SELECTOR, "#search-icon-legacy").click()

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img").click()