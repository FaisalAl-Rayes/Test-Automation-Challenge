from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



'''This file holds the necessary imports and methods'''

    
    
class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def InitiateGoogleDriver(self):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")

        driver = webdriver.Chrome(options=options)
        self.driver = driver

    def ShutDownGoogleDriver(self):
        self.driver.close()
        self.driver.quit()

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def do_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH,locator)

    def affirm_absence_of_element(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            x = "Element not present"
        assert "not present" in x, "Element found!"

    def do_find_element_href(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH,locator).get_attribute('href')

    def search_for(self, locator_SearchBar, locator_SearchButton, searchtext):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator_SearchBar)).send_keys(searchtext)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator_SearchButton)).click()