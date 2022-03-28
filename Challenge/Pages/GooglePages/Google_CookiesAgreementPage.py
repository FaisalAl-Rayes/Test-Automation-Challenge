from Challenge.Pages.BasePage import BaseClass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class GoogleAgreementPage(BaseClass):

    #locators
    I_AGREE = (By.CSS_SELECTOR,"#L2AGLb")

    def __init__(self, driver):
        super().__init__(driver)

    #Input method.
    def click_i_agree(self):
        try:
            self._do_click(self.I_AGREE)
        except NoSuchElementException:
            pass
