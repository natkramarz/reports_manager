from selenium import webdriver
import time
from clicking_functions import click_txt_button, fill_in_report_page
from fill_out_login_page import fill_out_form

login = input("Login: ")
password = input("Password: ")
login_page_url = ""
report_generating_page_url = ""

# choosing web browser
driver = webdriver.Chrome()

# fill out login page
fill_out_form(driver, login_page_url, login, password)

time.sleep(1)

# accessing reports generating page
driver.get(report_generating_page_url)

# checking the number of reports to generate
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[2]').click()
table_len = len(driver.find_elements_by_xpath('//table[@class="content"]/tbody/tr'))

# clicking the first object for which the report is to be generated
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/table/tbody/tr[2]/td[1]/a').click()
time.sleep(1)

# filling needed information
fill_in_report_page(driver)
click_txt_button(driver)

# generating the rest of reports
for row in range(3, table_len + 1):
    # redirecting to the subpage with the list of objects
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[2]').click()
    time.sleep(0.3)
    # choosing the object for which the report is to be generated
    driver.find_element_by_xpath(f"/html/body/div/div[2]/div[1]/form/table/tbody/tr[{row}]/td[1]/a").click()
    time.sleep(0.3)
    click_txt_button(driver)
    time.sleep(0.3)
