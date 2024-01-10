import logging
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_flights_result_page import FlightFilterPage
from utilities.utils import Utils

class LaunchPage(BaseDriver):
    obj_log=Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver=driver
        super().__init__(driver)

    #Locators
    DEPART_FROM_FIELD='//input[@id="BE_flight_origin_city"]'
    GOING_TO_FIELD='//input[@id="BE_flight_arrival_city"]'
    GOING_TO_FIELD_LIST="//div[@class='viewport']//div[1]//li"
    DATE_FIELD="//input[@id='BE_flight_origin_date']"
    ALL_DATES_LIST="//div[@id='monthWrapper']//td[@class!='inActiveTD']"
    SEARCH_BUTTON="//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.GOING_TO_FIELD)

    def getGoingToFieldList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.GOING_TO_FIELD_LIST)

    def getDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.DATE_FIELD)

    def getAllDatesList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.ALL_DATES_LIST)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH,self.SEARCH_BUTTON)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.obj_log.info("Clicked on Depart Form")
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        self.obj_log.warning("Clicked on Going to")
        self.getGoingToField().send_keys(goingtolocation)
        search_results=self.getGoingToFieldList()
        for result in search_results:
            if "New York (JFK)" in result.text:
                result.click()
                break

    def enterDepartureDate(self, departdate):
        self.getDateField().click()
        self.obj_log.info("clicked on date")
        all_dates=self.getAllDatesList()
        for date in all_dates:
            if date.get_attribute("data-date")==departdate:
                date.click()
                break

    def enterSearchButon(self):
        self.getSearchButton().click()
        self.obj_log.info("Clicked on Search button")

    def searchFlights(self, departform, goingto, date):
        self.enterDepartFromLocation(departform)
        self.enterGoingToLocation(goingto)
        self.enterDepartureDate(date)
        self.enterSearchButon()
        obj_search_flight_result=FlightFilterPage(self.driver)
        return obj_search_flight_result

    # def departfrom(self, departlocation):
    #     #depart=self.wait_until_element_is_clickable(By.XPATH,'//input[@id="BE_flight_origin_city"]')
    #     depart = self.driver.find_element(By.XPATH, '//input[@id="BE_flight_origin_city"]')
    #     depart.click()
    #     depart.send_keys(departlocation)
    #     depart.send_keys(Keys.ENTER)

    # def goingto(self, endlocaiton):
    #     going_to = self.driver.find_element(By.XPATH, '//input[@id="BE_flight_arrival_city"]')
    #     going_to.click()
    #     going_to.send_keys(endlocaiton)
    #     search_results = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
    #     for result in search_results:
    #         if "New York (JFK)" in result.text:
    #             result.click()
    #             break

    # def selectdate(self, departdate):
    #     ele=self.wait_until_element_is_clickable(By.XPATH,"//input[@id='BE_flight_origin_date']")
    #     ele.click()
    #     all_dates=self.wait_for_presence_of_all_elements(By.XPATH, "//div[@id='monthWrapper']//td[@class!='inActiveTD']")
    #     for date in all_dates:
    #         if date.get_attribute("data-date") == departdate:
    #             date.click()
    #             break

    # def clicksearch(self):
    #     self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()