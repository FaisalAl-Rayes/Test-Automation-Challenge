import unittest
from Challenge.Pages.BasePage import BasePage
from Challenge.Pages.GooglePages import *
from Challenge.Pages.CyberAlpacaPages import *


class Google2CyberAlpacaTest(unittest.TestCase, BasePage):
    
    #Initiation of the driver with the desired options before the start of the testing session.
    @classmethod
    def setUpClass(cls):
        cls.InitiateGoogleDriver(cls)

    def test_Site_Navigation(self):
        driver = self.driver

        driver.get("https://www.google.com/")
    
    #Google - Agreeing on the agreement terms set by Google if the agreements page pops up.
        cookiespage = Google_CookiesAgreementPage.GoogleAgreementPage(driver)
        cookiespage.click_i_agree()
        
    #Google Home page search.
        homepage = Google_HomePage.GoogleHomePage(driver)
        homepage.search_for("CyberAlpaca")

    #Google - Result page checking.
        resultpage = Google_SearchResultPage.GoogleResultPage(driver)
        resultpage.Find_CA_Link()
        assert "www.cyberalpaca.com" in resultpage.Find_CA_Link() , "Result not found"

    #Google - entering www.cyberalpaca.com.
        resultpage.click_on_CA_link()

    #CyberAlpaca - Navigation through the Home Page.
        homepage = CyberAlpaca_HomePage.CA_HomePage(driver)
        homepage.click_on_ServicesTab()
        
    #CyberAlpaca - Entering the Services Page.
        servicespage = CyberAlpaca_ServicesPage.CA_ServicesPage(driver)
        
    #CyberAlpaca - Making sure that Our Services Exists and that the Squish GUI Testing Logo is displayed in the Automated GUI Testing page.
        servicespage.check_for_Our_Services()
        servicespage.click_on_Automated_GUI_testing()
        servicespage.check_for_Squish_GUI_Testing_Logo()
    
    #CyberAlpaca - Navigating to Embedded testing page.
        servicespage.click_on_Embedded_testing()

    #CyberAlpaca - Making sure that the Squish GUI Testing Logo is displayed in Automated GUI Testing page.
        servicespage.check_for_Squish_GUI_Testing_Logo()
    
    #CyberAlpaca - Navigating through the next pages
        servicespage.click_on_Mobile_application_testing()
        servicespage.click_on_Web_testing()
        servicespage.click_on_API_testing()

    #CyberAlpaca - Making sure that the Squish GUI Testing Logo is not displayed in the API testing page.
        servicespage.check_for_missing_Squish_GUI_Testing_Logo()

    #CyberAlpaca - Navigating through the rest of the pages.
        servicespage.click_on_Load_and_Performance_testing()
        servicespage.click_on_Tool_integration_development()

    #Closing the browser and driver after the testing session is over.
    @classmethod
    def tearDownClass(cls):
        cls.ShutDownGoogleDriver(cls)
        print("Test Completed")