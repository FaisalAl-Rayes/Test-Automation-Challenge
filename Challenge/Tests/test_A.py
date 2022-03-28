import unittest
from Challenge.Pages.BasePage import BaseClass
from Challenge.Pages.GooglePages import *


class GoogleSearchTest(unittest.TestCase, BaseClass):
    
    #Initiation of the driver with the desired options before the start of the testing session.
    @classmethod
    def setUpClass(cls):
        cls.InitiateGoogleDriver(cls)

    def test_Search_Result_Found(self):
        driver = self.driver

    #Accessing www.google.com.(1)
        driver.get("https://www.google.com/")
    
    #Agreeing on the agreement terms set by Google if the agreements page pops up.
        cookiespage = Google_CookiesAgreementPage.GoogleAgreementPage(driver)
        cookiespage.click_i_agree()
        
    #Home page search.(2)
        homepage = Google_HomePage.GoogleHomePage(driver)
        homepage.search_for("CyberAlpaca")

    #Result page checking.(3)
        resultpage = Google_SearchResultPage.GoogleResultPage(driver)
        resultpage.check_for_CA_Link()

    #Closing the browser and driver after the testing session is over.
    @classmethod
    def tearDownClass(cls):
        cls.ShutDownGoogleDriver(cls)
        print("Test Completed")