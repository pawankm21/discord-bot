import os
from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

my_secret = "aiswarika21"
username = "pawan994567@gmail.com"

driver = webdriver.Edge("E:\msedgedriver.exe")
action = ActionChains(driver)
driver.set_window_size(2000, 694)
driver.implicitly_wait(2)
driver.get("https://binarysearch.com/")
driver.implicitly_wait(2)

driver.find_element_by_xpath(
    '//button[@class="Button_container__2cIrd Button_secondary__PUVBB Button_compact__3kdU9"]'
).click()
driver.implicitly_wait(2)
driver.find_element_by_xpath("//input[@name='usernameOrEmail']").send_keys(
    username)
driver.implicitly_wait(2)
driver.find_element_by_xpath("//input[@name='password']").send_keys(my_secret)
driver.implicitly_wait(2)
action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
driver.implicitly_wait(5)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='Button_container__2cIrd Button_primary__3lv4c Button_compact__3kdU9']")))
ActionChains(driver).move_to_element(element).click().perform()

driver.implicitly_wait(3)

action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

driver.implicitly_wait(4)

currentUrl = driver.current_url
print(currentUrl)

driver.quit()

