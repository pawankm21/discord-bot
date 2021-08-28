import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
my_secret = os.environ["password"]
username = os.environ["username"]


def createRoom():

    driver = webdriver.Edge("E:\msedgedriver.exe")
    action = ActionChains(driver)
    driver.set_window_size(2000, 694)
    driver.implicitly_wait(10)
    driver.get("https://binarysearch.com/")

    driver.find_element_by_xpath(
        '//button[@class="Button_container__2cIrd Button_secondary__PUVBB Button_compact__3kdU9"]'
    ).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@name='usernameOrEmail']").send_keys(
        username)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(
        "//input[@name='password']").send_keys(my_secret)
    driver.implicitly_wait(10)
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    element = WebDriverWait(driver, 10,)\
        .until(EC.presence_of_element_located(((By.XPATH, "//div[@class='LobbyUsers_create-room-button__3G6v4']"))))
    ActionChains(driver).move_to_element(element).click().perform()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath(
        '//form/div[3]/div[2]/div[2]/div/button').click()

    WebDriverWait(driver, 20).until(EC.url_contains("room"))
    ROOMURL = driver.current_url
    driver.quit()
    return ROOMURL
