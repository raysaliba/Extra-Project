import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get('https://myportal.lau.edu.lb/')

username = sys.argv[1]
password = sys.argv[2]
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(username)
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)


login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
login_btn.click()
courses_btn = driver.find_element(By.XPATH, '//[@id="zz4_TopNavigationMenuV4"]/div/ul/li/ul/li[3]/a')
courses_btn.click()
course_offerings_btn = driver.find_element(By.XPATH, '//[@id="cbqwpctl00_m_g_df4e4cc9_291f_48af_90eb_524811091537"]/div/div[2]/a[4]')
course_offerings_btn.click()
driver.get("https://banweb.lau.edu.lb/prod/bwckschd.p_disp_dyn_sched")