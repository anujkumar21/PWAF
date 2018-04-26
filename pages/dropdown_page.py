"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 16-Apr-18
"""
import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.header = "Dropdown List"
        self.xpathHeading = "//h3"
        self.xpathCheckboxes = "//input[@type='checkbox'][%d]"

    def verify_dropdown_page(self):
        """
        This method is to verify Dropdown page.

        return: instance of Dropdown page
        rtype: DropdownPage instance
        """

        logging.info("## Verifying Dropdown page ##")
        self.services.wait_for_element(self.xpathHeading)
        actual_heading = self.services.get_text_by_xpath(self.xpathHeading)
        logging.info("# Actual heading on Dropdown page: %s" % actual_heading)
        assert actual_heading == self.header, "Actual header (%s), should be same as expected header (%s)." % (
            actual_heading, self.header)
