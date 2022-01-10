from selenium import webdriver
import time
from dotenv import load_dotenv 
# from webdriver_manager.chrome import ChromeDriverManager

import login_page
from report_page import ReportPage
import os


class ReportsManager:
    def __init__(self, login, password, start_date, end_date):
        self.login = login
        self.password = password
        self.start_date = start_date
        self.end_date = end_date
        load_dotenv()
        self.login_page_url = os.environ.get("LOGIN_PAGE_URL")
        self.report_generating_page_url = os.environ.get("REPORT_GENERATING_PAGE_URL")

    def generate_reports(self):
        try:
            # choosing web browser
            driver = webdriver.Chrome()

            # fill out login page
            login_page.fill_out(driver, self.login_page_url, self.login, self.password)

            time.sleep(1)

            # accessing reports generating page
            driver.get(self.report_generating_page_url)

            # checking the number of reports to generate
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[1]/td/input[2]').click()
            table_len = len(driver.find_elements_by_xpath('//table[@class="content"]/tbody/tr'))

            # clicking the first object for which the report is to be generated
            driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/table/tbody/tr[2]/td[1]/a').click()
            time.sleep(1)

            # filling in needed information
            report_page = ReportPage(driver, self.start_date, self.end_date)
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
        except Exception as e:
            print(e)
        else:
            print("Reports generated succesfully")