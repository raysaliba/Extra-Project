import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import csv
from selenium.webdriver.common.keys import Keys

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

select_term_box = driver.find_element(By.XPATH, '//[@id="term_input_id"]')
select_term = Select(select_term_box)
select_term.select_by_value("202410")
submit_btn = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]")
submit_btn.click()
subject_select_element = driver.find_element(By.XPATH, '//[@id="subj_id"]')
subject_select = Select(subject_select_element)
subject_select.select_by_value("CSC")
campus_select_element = driver.find_element(By.XPATH, '//*[@id="camp_id"]')
campus_select = Select(campus_select_element)
campus_select.select_by_value("2")
course_offerings_btn = driver.find_element(By.XPATH, '/html/body/div[3]/form/input[12]')
course_offerings_btn.click()
name_elements = driver.find_elements(By.CSS_SELECTOR, ".ddtitle > a")
names = [element.text for element in name_elements]
instructor_elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(7)")
instructors = [element.text for element in instructor_elements]
time_elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(2)")
times = [element.text for element in time_elements]
day_elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(3)")
days = [element.text for element in day_elements]
location_elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(4)")
locations = [element.text for element in location_elements]
data = list(zip(names, instructors, locations, times, days))


Updated variable names

login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
login_btn.click()
my_courses_btn = driver.find_element(By.XPATH, '//[@id="zz4_TopNavigationMenuV4"]/div/ul/li/ul/li[3]/a')
my_courses_btn.click()
course_offerings_btn = driver.find_element(By.XPATH, '//[@id="cbqwpctl00_m_g_df4e4cc9_291f_48af_90eb_524811091537"]/div/div[2]/a[4]')
course_offerings_btn.click()
driver.get("https://banweb.lau.edu.lb/prod/bwckschd.p_disp_dyn_sched")

term_select_element = driver.find_element(By.XPATH, '//[@id="term_input_id"]')
term_select = Select(term_select_element)
term_select.select_by_value("202410")
submit_btn = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]")
submit_btn.click()
subject_select_element = driver.find_element(By.XPATH, '//[@id="subj_id"]')
subject_select = Select(subject_select_element)
subject_select.select_by_value("CSC")
campus_select_element = driver.find_element(By.XPATH, '//*[@id="camp_id"]')
campus_select = Select(campus_select_element)
campus_select.select_by_value("2")
course_offerings_btn = driver.find_element(By.XPATH, '/html/body/div[3]/form/input[12]')
course_offerings_btn.click()
name_elements = driver.find_elements(By.CSS_SELECTOR, ".ddtitle > a")
names = [element.text for element in name_elements]
instructor_elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(7)")
instructors = [element.text for element in instructor_elements]
time_elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(2)")
times = [element.text for element in time_elements]
day_elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(3)")
days = [element.text for element in day_elements]
location_elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(4)")
locations = [element.text for element in location_elements]
data = list(zip(names, instructors, locations, times, days))

file_path = os.path.join(os.path.dirname(os.path.realpath(os.getcwd())), 'course_data.csv')

with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Instructor", "Location", "Time", "Day"])
    writer.writerows(data)

driver.quit()



