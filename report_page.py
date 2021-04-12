import time
from datetime import datetime

class ReportPage:

    def __init__(self, driver, start_day, start_month, end_day, end_month):
        self.driver = driver
        self.days = (start_day, start_month)
        self.months = (start_month, end_month)

    def set_date_calendar(self, calendars):
        today = datetime.today()
        for i in range(len(calendars)):
            calendars[i].click()
            # to-do: set up month picker
            click_cnt = today.month - self.months[i]
            for _ in range(click_cnt):
                self.driver.find_element_by_class_name('ui-datepicker-prev').click()
            time.sleep(0.3)
            table_len = len(self.driver.find_elements_by_xpath('//table[@class="ui-datepicker-calendar"]/tbody/tr'))
            self.driver.find_element_by_xpath(f"//a[text()={self.start_day[i]}]").click()

    def fill_in_report_page(self):
        # finding calendars
        calendars = self.driver.find_elements_by_class_name('ui-datepicker-trigger')
        self.set_date_calendar(calendars)

        # setting up start and end time
        start_time = self.driver.find_element_by_name("startTime")
        start_time.clear()
        start_time.send_keys("8:00")
        end_time = self.driver.find_element_by_name("endTime")
        end_time.clear()
        end_time.send_keys("18:00")

        # clicking city & street button
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[8]/td/div[2]/input').click()

    def click_txt_button(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/table/tbody/tr[9]/td/input[2]').click()

