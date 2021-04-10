from selenium import webdriver
import time

def click_txt_button():
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[9]/td/input[2]').click()

def fill_in_report_page():
    # finding calendars
    calendars = browser.find_elements_by_class_name('ui-datepicker-trigger')

    # setting date on the first calendar
    calendars[0].click()
    browser.find_element_by_class_name('ui-datepicker-prev').click()
    time.sleep(0.3)
    browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[1]/a').click()

    # setting date on the second calendar
    calendars[1].click()
    browser.find_element_by_class_name('ui-datepicker-prev').click()
    browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]/a').click()
    time.sleep(0.3)

    # setting up start and end time
    start_time = browser.find_element_by_name("startTime")
    start_time.clear()
    start_time.send_keys("8:00")
    end_time = browser.find_element_by_name("endTime")
    end_time.clear()
    end_time.send_keys("18:00")

    # clicking city & street button
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[8]/td/div[2]/input').click()

login = input("Login: ")
password = input("Password: ")
login_page_url = ""
report_generating_page_url = ""

# choosing web browser
driver = webdriver.Chrome()

# login page
browser.get(login_page_url)
l = browser.find_element_by_name("username")
l.send_keys(login)
p = browser.find_element_by_name("password")
p.send_keys(password)
browser.find_element_by_xpath("/html/body/div/div[2]/div/form/div/div[4]/div[2]/input").click()

time.sleep(1)

# accessing reports generating page
browser.get(report_generating_page_url)

# checking the number of reports to generate
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[2]').click()
table_len = len(browser.find_elements_by_xpath('//table[@class="content"]/tbody/tr'))

# clicking the first object for which the report is to be generated
browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/table/tbody/tr[2]/td[1]/a').click()
time.sleep(1)

# filling needed information
fill_in_report_page()
click_txt_button()

# generating the rest of reports
for row in range(3, table_len + 1):
    # redirecting to the subpage with the list of objects
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[2]').click()
    time.sleep(0.3)
    # choosing the object for which the report is to be generated
    browser.find_element_by_xpath(f"/html/body/div/div[2]/div[1]/form/table/tbody/tr[{row}]/td[1]/a").click()
    time.sleep(0.3)
    click_txt_button()
    time.sleep(0.3)