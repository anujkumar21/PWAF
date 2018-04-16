"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class DropdownPageTest(DriverManager):
    def test_dropdown_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dropdown")
