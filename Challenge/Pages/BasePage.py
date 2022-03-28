from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



'''This file holds the necessary imports and methods'''

    
    
class BaseClass():
    
    def __init__(self, driver):
        self.driver = driver
        
    #-Set explicit wait.
        self.wait10 = WebDriverWait(self.driver, 10)
        self.wait5 = WebDriverWait(self.driver, 5)

    #Driver initiation method.
    def InitiateGoogleDriver(self):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")

        driver = webdriver.Chrome(options=options)
        self.driver = driver

    #Driver shutting down method.
    def ShutDownGoogleDriver(self):
        self.driver.close()
        self.driver.quit()

    #Base input methods.    
    def _do_click(self, locator):
        try:
            self.wait5.until(ec.element_to_be_clickable(locator)).click()
        except TypeError:
            self.driver.find_element(By.XPATH,locator).click()

    def _do_send_keys(self, locator, text):
        self.wait5.until(ec.visibility_of_element_located(locator)).send_keys(text)

    #Base locating and extracting methods.
    def _do_find_element(self, locator):
        self.wait10.until(ec.presence_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH,locator)

    def _do_find_element_href(self, locator):
        self.wait10.until(ec.presence_of_element_located((By.XPATH, locator)))
        return self.driver.find_element(By.XPATH,locator).get_attribute('href')

    #Base checking methods
    def _affirm_absence_of_element(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            x = "Element not present"
        assert "not present" in x, "Element found!"