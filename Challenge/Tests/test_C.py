import unittest
from Challenge.Pages.BasePage import BaseClass
from Challenge.Pages.GooglePages import *
from Challenge.Pages.CyberAlpacaPages import *


class Google2CyberAlpacaTest(unittest.TestCase, BaseClass):
    
    #Initiation of the driver with the desired options before the start of the testing session.
    @classmethod
    def setUpClass(cls):
        cls.InitiateGoogleDriver(cls)

    def test_Site_Navigation(self):
        driver = self.driver

    #Google - Accessing www.google.com.
        driver.get("https://www.google.com/")
    
    #Google - Agreeing on the agreement terms set by Google if the agreements page pops up.
        cookiespage = Google_CookiesAgreementPage.GoogleAgreementPage(driver)
        cookiespage.click_i_agree()
        
    #Google - Home page search.
        homepage = Google_HomePage.GoogleHomePage(driver)
        homepage.search_for("CyberAlpaca")

    #Google - Result page checking.
        resultpage = Google_SearchResultPage.GoogleResultPage(driver)
        resultpage.check_for_CA_Link()

    #Google - entering www.cyberalpaca.com.
        resultpage.click_on_CA_link()

    #CyberAlpaca - Navigation through the Home Page and entering the services page.
        homepage = CyberAlpaca_HomePage.CA_HomePage(driver)
        homepage.click_on_ServicesTab()

    #CyberAlpaca - Making sure that Our Services Exists 
        servicespage = CyberAlpaca_ServicesPage.CA_ServicesPage(driver)
        servicespage.check_for_Our_Services()

    #CyberAlpaca - Navigating through all the services pages and checking for Squish GUI Testing Logo 
    #              in the Automated GUI testing and Embedded testing pages.
    #CyberAlpaca - Checking for absence of the Squish GUI Testing Logo in the API testing page.
        servicespage.click_on_Automated_GUI_testing()
        servicespage.check_for_Squish_GUI_Testing_Logo()
    
        servicespage.click_on_Embedded_testing()
        servicespage.check_for_Squish_GUI_Testing_Logo()
    
        servicespage.click_on_Mobile_application_testing()
        servicespage.click_on_Web_testing()

        servicespage.click_on_API_testing()
        servicespage.check_for_missing_Squish_GUI_Testing_Logo()

        servicespage.click_on_Load_and_Performance_testing()
        servicespage.click_on_Tool_integration_development()


    #Closing the browser and driver after the testing session is over.
    @classmethod
    def tearDownClass(cls):
        cls.ShutDownGoogleDriver(cls)
        print("Test Completed")