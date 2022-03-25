import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from Challange.Locators.Locators_B import Locators


class CyberAlpacaSurfTest(unittest.TestCase,Locators):
    
    #Initiation of the driver with the desired options before the start of the testing session.
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_Site_Navigation(self):
        driver = self.driver

        
        driver.get('http://www.cyberalpaca.com/')

    #Navigation through the website.
        driver.find_element(By.XPATH,Locators.SERVICES_TAB).click()
        driver.find_element(By.XPATH,Locators.AUTOMATED_GUI_TESTING).click()

    #Making sure that Our Services Exists and that the Squish GUI Testing Logo is displayed in the Automated GUI Testing page.
        assert "Our Services" in driver.find_element(By.XPATH,Locators.OUR_SERVICES_TEXT).text, "Not Found"
        assert "www.froglogic.com/squish/" in driver.find_element(By.XPATH,Locators.SQUISH_GUI_LOGO).get_attribute('href')
    
    #Navigating to Embedded testing page.
        driver.find_element(By.XPATH,Locators.EMBEDDED_TESTING).click()

    #Making sure that the Squish GUI Testing Logo is displayed in Automated GUI Testing page.
        assert "www.froglogic.com/squish/" in driver.find_element(By.XPATH,Locators.SQUISH_GUI_LOGO).get_attribute('href')

    #Navigating through the next pages
        driver.find_element(By.XPATH,Locators.MOBILE_APPLICATION_TESTING).click()
        driver.find_element(By.XPATH,Locators.WEB_TESTING).click()
        driver.find_element(By.XPATH,Locators.API_TESTING).click()

    #Making sure that the Squish GUI Testing Logo is not displayed in the API testing page.
        try:
            driver.find_element(By.XPATH,Locators.SQUISH_GUI_LOGO)
        except NoSuchElementException:
            x = "Squish GUI Testing Logo is not present in the API testing page"
        assert "not present in the API testing" in x, "Squish GUI Testing Logo Found"

    #Navigating through the rest of the pages.
        driver.find_element(By.XPATH,Locators.LOAD_AND_PERFORMANCE_TESTING).click()
        driver.find_element(By.XPATH,Locators.TOOL_INTEGRATION_DEVELOPMENT).click()

    #Closing the browser and driver after the testing session is over.
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")