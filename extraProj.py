import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

username = sys.argv[1]
password = sys.argv[2]

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get('https://myportal.lau.edu.lb/')

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(username)
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)