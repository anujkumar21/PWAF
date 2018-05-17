""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 16-Apr-18
"""
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class Services:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=20):
        """
        This method is to wait for presence of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param_type: string

        param timeout: maximum wait timeout
        param_type: number
        """

        logging.info("# Wait for element to appear... %s" % locator)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))

    def assert_and_click_by_xpath(self, locator):
        """
        This method is to assert and click on the web element.

        param locator: XPATH of given element
        param_type: string
        """

        self.wait_for_element(locator)
        logging.info("# Click on element %s" % locator)
        ele = self.driver.find_element_by_xpath(locator)
        ele.click()

    def get_text_by_xpath(self, locator):
        """
        This method is get the text present within given web element.

        param locator: XPATH of given element
        param_type: string
        """

        return self.driver.find_element_by_xpath(locator).text

    def is_element_present(self, locator):
        """
        This method to is verify element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
        try:
            self.driver.find_element_by_xpath(locator)
            return True
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % locator)
            return False
