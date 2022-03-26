from Challenge.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class GoogleAgreementPage(BasePage):

    #locators
    I_AGREE = (By.CSS_SELECTOR,"#L2AGLb")

    def __init__(self, driver):
        super().__init__(driver)

    def click_i_agree(self):
        self.do_click(self.I_AGREE)