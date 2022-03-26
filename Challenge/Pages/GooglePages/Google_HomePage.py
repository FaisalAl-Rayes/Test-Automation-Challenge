from Challenge.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class GoogleHomePage(BasePage):

    #locators
    SEARCH_BAR = (By.NAME,"q")
    SEARCH_BUTTON = (By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_for(self, searchtext):
        self.do_send_keys(self.SEARCH_BAR, searchtext)
        self.do_click(self.SEARCH_BUTTON)