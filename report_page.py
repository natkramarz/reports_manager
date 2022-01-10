import time
from datetime import datetime

class ReportPage:

    def __init__(self, driver, start_date, end_date):
        self.driver = driver
        self.dates = (start_date, end_date)

    def set_date_calendar(self, calendars):
        today = datetime.today()
        for i in range(len(calendars)):
            calendars[i].click()
            click_cnt = (today.year - self.dates[i].year) * 12 + (today.month - self.dates[i].month)
            for _ in range(click_cnt):
                self.driver.find_element_by_class_name('ui-datepicker-prev').click()
            time.sleep(0.3)
            self.driver.find_element_by_xpath(f"//a[text()={self.dates[i].day}]").click()
            time.sleep(0.3)

    def fill_in_report_page(self):
        # finding calendars
        calendars = self.driver.find_elements_by_class_name('ui-datepicker-trigger')
        self.set_date_calendar(calendars)

        # setting up start and end time
        start_time = self.driver.find_element_by_name("fromTime")
        start_time.clear()
        start_time.send_keys("8:00")
        end_time = self.driver.find_element_by_name("toTime")
        end_time.clear()
        end_time.send_keys("18:00")

        # clicking city & street button
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[8]/td/div[2]/input').click()

    def click_txt_button(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[9]/td/input[2]').click()

