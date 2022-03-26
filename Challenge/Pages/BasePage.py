from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


'''This file holds the necessary imports and methods'''


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator,text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def do_find_element(self,locator):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def search_for(self, locator_SearchBar, locator_SearchButton, searchtext):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator_SearchBar)).send_keys(searchtext)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator_SearchButton)).click()