from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from Challenge.Pages.Google_HomePage import GoogleHomePage
from Challenge.Pages.Google_SearchResultPage import GoogleResultPage
from Challenge.Pages.Google_CookiesAgreementPage import GoogleAgreementPage
from selenium.common.exceptions import NoSuchElementException
import unittest


class GoogleSearchTest(unittest.TestCase):
    
    #Initiation of the driver with the desired options before the start of the testing session.
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--disable-notifications")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()

    def test_Search_Result_Found(self):
        driver = self.driver

        driver.get("https://www.google.com/")
    
    #Agreeing on the agreement terms set by Google if the agreements page pops up.
        try:
            cookiespage = GoogleAgreementPage(driver)
            cookiespage.click_i_agree()
        except NoSuchElementException:
            pass
        
    #Home page search.
        homepage = GoogleHomePage(driver)
        homepage.search_for("CyberAlpaca")

    #Result page checking.
        '''  ideally you would use a method defined in the BasePage class found in the BasePage module and 
                use it for a method in the GoogleResultPage class found in the Google_SearchResultPage module
                    to be able to seperate the locators from the test methods. The preffered approch is commented 
                        out of the code below this text but is there to show the better methodology in creating test cases.  '''

        #resultpage = GoogleResultPage(driver)
        #resultpage.Find_CA_Link()
        #assert "www.cyberalpaca.com" in resultpage.Find_CA_Link() , "Result not found"

        website_element = driver.find_element(By.XPATH,'//a[@href="http://www.cyberalpaca.com/" and @role="button"]').get_attribute('href')
        assert "www.cyberalpaca.com" in website_element , "Result not found"

    #Closing the browser and driver after the testing session is over.
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")