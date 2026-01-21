# import selenium.webdriver as webdriver

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url="https://www.saucedemo.com/"
driver.get(url)


username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(10)

driver.quit()

