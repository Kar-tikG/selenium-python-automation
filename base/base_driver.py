import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver():
    def __init__(self, driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)

    def scroll_page(self,driver):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(4)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        list_ele=self.wait.until(
            EC.presence_of_all_elements_located((locator_type, locator)))
        return list_ele

    def wait_until_element_is_clickable(self, locator_type, locator):
        ele=self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return ele

#sample line for github sdet1