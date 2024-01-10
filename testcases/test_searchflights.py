import pytest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
import softest
from ddt import ddt,data,unpack,file_data

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlightsAndVerifyFilter(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.obj_lp = LaunchPage(self.driver)
        self.obj_ut = Utils()

    # @data(("New Delhi", "New", "20/12/2023", "1 Stop"),("BOM", "New", "27/12/2023", "2 Stop"))
    # @unpack

    #@file_data("../testdata/testdata.json")

    #@file_data("../testdata/testdata.json")

    # @data(*Utils.read_data_from_excel("D:\\Python_Selenium\\DemoTestFramework\\testdata\\demo_sheet.xlsx","Sheet1"))
    # @unpack

    @data(*Utils.read_date_from_csv("D:\\Python_Selenium\\DemoTestFramework\\testdata\\tcdatacsv.csv"))
    @unpack
    def test_search_flights(self, goingfrom, goingto, date, stops):
        obj_search_flight_result = self.obj_lp.searchFlights(goingfrom, goingto, date)
        obj_search_flight_result.enterFilterButton()
        obj_search_flight_result.scroll_page(self.driver)
        list_ele = obj_search_flight_result.getFilterResults()
        self.obj_ut.assert_ele_from_list(list_ele, stops)





        #Launching the browser

        #provide going from location
        #obj_lp=LaunchPage(self.driver)
        #obj_lp.searchFlights("New Delhi", "New", "20/12/2023")
        #obj_search_flight_result=self.obj_lp.searchFlights("New Delhi", "New", "20/12/2023")

        #obj_lp.departfrom("New Delhi")
        #obj_lp.enterDepartFromLocation("New Delhi")

        #provide going to location
        #obj_lp.goingto("New")
        #obj_lp.enterGoingToLocation("New")

        #select departure date
        #obj_lp.selectdate("20/12/2023")
        #obj_lp.enterDepartureDate("20/12/2023")

        #click on flight search button
        #obj_lp.clicksearch()
        #obj_lp.enterSearchButon()

        #select the filter 1 stop
        #obj_sf=FlightFilterPage(self.driver)
        #obj_sf.clickfilter()
        #obj_sf.enterFilterButton()
        #obj_search_flight_result.enterFilterButton()

        #scroll down
        #obj_sf.scroll_page(self.driver)
        #obj_search_flight_result.scroll_page(self.driver)

        #verify the filtered results show flights having only 1 stop
        #list_ele=obj_lp.wait_for_presence_of_all_elements(By.XPATH, "//span[@class='dotted-borderbtm']")
        #list_ele=obj_sf.getFilterResults()
        #list_ele=obj_search_flight_result.getFilterResults()
        #obj_ut=Utils()
        #self.obj_ut.assert_ele_from_list(list_ele, "1 Stop")

    # def test_search_flights_2_stops(self):
    #     obj_search_flight_result=self.obj_lp.searchFlights("New Delhi", "New", "20/12/2023")
    #     obj_search_flight_result.enterFilterButton()
    #     obj_search_flight_result.scroll_page(self.driver)
    #     list_ele=obj_search_flight_result.getFilterResults()
    #     self.obj_ut.assert_ele_from_list(list_ele, "2 Stops")

