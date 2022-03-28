from Challenge.Pages.BasePage import BaseClass
from Challenge.Locators.Locators_B import Locators


class CA_HomePage(BaseClass, Locators):

    def __init__(self, driver):
        super().__init__(driver)

    #Input methods.
    def click_on_ServicesTab(self):
        self._do_click(Locators.SERVICES_TAB)