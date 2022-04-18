from Challenge.Pages.BasePage import BaseClass
from selenium.webdriver.common.by import By


class GoogleHomePage(BaseClass):

    #locators
    SEARCH_BAR = (By.NAME,"q")
    SEARCH_BUTTON = (By.CSS_SELECTOR,"div.FPdoLc.lJ9FBc input.gNO89b")

    def __init__(self, driver):
        super().__init__(driver)

    #Input method.
    def search_for(self, searchtext):
        self._do_send_keys(self.SEARCH_BAR, searchtext)
        self._do_click(self.SEARCH_BUTTON)