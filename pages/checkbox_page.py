"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class CheckboxPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Checkboxes"
        self.xpathHeading = "//h3"
        self.xpathCheckboxes = "//input[@type='checkbox'][%d]"

    def verify_checkbox_page(self):
        logging.info("## Verifying checkbox page ##")
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on checkbox page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)

    def select_checkbox(self, index, to_select=True):
        logging.info("# Select or un-select checkbox.")
        xpath = self.xpathCheckboxes % index
        self.services.wait_for_element(xpath)
        checkbox_ele = self.driver.find_element_by_xpath(xpath)
        if to_select:
            if not checkbox_ele.is_selected():
                logging.info("# Selecting checkbox.")
                checkbox_ele.click()
        else:
            if checkbox_ele.is_selected():
                logging.info("# Un-selecting checkbox.")
                checkbox_ele.click()

        import time
        time.sleep(5)
