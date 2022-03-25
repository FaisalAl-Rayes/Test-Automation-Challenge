from Challange.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  
from selenium import webdriver  


class GoogleResultPage(BasePage):

    #locators
    CA_XPATH = (By.XPATH, '//a[@href="http://www.cyberalpaca.com/" and @role="button"]')
    
    def __init__(self, driver):
        super().__init__(driver)

    def Find_CA_Link(self):
        
        return self.do_find_element(self.CA_XPATH)
