from selenium import webdriver
import time

import login_page
from report_page import ReportPage

login = input("Login: ")
password = input("Password: ")
start_month = input(int("Start month: "))
start_day = input(int("Start day: "))
end_month = input(int("End month:"))
end_day = input(int("End day: "))
login_page_url = ""
report_generating_page_url = ""

# choosing web browser
driver = webdriver.Chrome()

# fill out login page
login_page.fill_out_form(driver, login_page_url, login, password)

time.sleep(1)

# accessing reports generating page
driver.get(report_generating_page_url)

# checking the number of reports to generate
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[2]').click()
table_len = len(driver.find_elements_by_xpath('//table[@class="content"]/tbody/tr'))

# clicking the first object for which the report is to be generated
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/table/tbody/tr[2]/td[1]/a').click()
time.sleep(1)

# filling in needed information
report_page = ReportPage(driver, start_day, start_month, end_day, end_month)
report_page.fill_in_report_page()
report_page.click_txt_button()

# generating the rest of reports
for row in range(3, table_len + 1):
    # redirecting to the subpage with the list of objects
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[2]').click()
    time.sleep(0.3)
    # choosing the object for which the report is to be generated
    driver.find_element_by_xpath(f"/html/body/div/div[2]/div[1]/form/table/tbody/tr[{row}]/td[1]/a").click()
    time.sleep(0.3)
    report_page.click_txt_button()
    time.sleep(0.3)
