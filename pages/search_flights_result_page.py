import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class FlightFilterPage(BaseDriver):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    #locators
    FILTER_BUTTON="//label[2]//p[1]"
    FILTER_RESULTS="//span[@class='dotted-borderbtm']"

    def getFilterButton(self):
        return self.driver.find_element(By.XPATH,self.FILTER_BUTTON)

    def getFilterResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.FILTER_RESULTS)

    def enterFilterButton(self):
        self.getFilterButton().click()

    # def clickfilter(self):
    #     self.driver.find_element(By.XPATH, "//label[2]//p[1]").click()
    #     time.sleep(2)