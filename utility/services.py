""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class Services:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        logging.info("# Wait for element to appear... %s" % locator)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, locator)))

    def assert_and_click_by_xpath(self, locator):
        self.wait_for_element(locator)
        logging.info("# Click on element %s" % locator)
        ele = self.driver.find_element_by_xpath(locator)
        ele.click()

    def get_text_by_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator).text
