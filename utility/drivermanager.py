""" 
@auther: Anuj Kumar
@email: cdac.anuj@gmail.com
"""

import logging
import unittest

from selenium import webdriver

                    level=logging.INFO)


class DriverManager(unittest.TestCase):
    """
    This class is for instantiating web driver instances.
    """

    def setUp(self):
        logging.info("## SETUP METHOD ##")
        logging.info("# Initializing the webdriver.")
        self.driver = webdriver.Firefox(executable_path="E:\\automation\drivers\geckodriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://the-internet.herokuapp.com/")

    def tearDown(self):
        logging.info("## TEARDOWN METHOD ##")

        if sys.exc_info()[0]:
            logging.info("# Taking screenshot.")
            test_method_name = self._testMethodName
            self.driver.save_screenshot("./../screenshots/%s.png" % test_method_name)

        if self.driver is not None:
            logging.info("# Removing the webdriver.")
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
