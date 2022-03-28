import unittest
from Challenge.Pages.BasePage import BaseClass
from Challenge.Pages.CyberAlpacaPages import *


class CyberAlpacaSurfTest(unittest.TestCase, BaseClass):
    
    #Initiation of the driver with the desired options before the start of the testing session.
    @classmethod
    def setUpClass(cls):
        cls.InitiateGoogleDriver(cls)

    def test_Site_Navigation(self):
        driver = self.driver

    #Accessing www.cyberalpaca.com.(1)
        driver.get('http://www.cyberalpaca.com/')

    #Navigation through the Home Page and entering the services page.(2)
        homepage = CyberAlpaca_HomePage.CA_HomePage(driver)
        homepage.click_on_ServicesTab()

    #Making sure that Our Services Exists (3)
        servicespage = CyberAlpaca_ServicesPage.CA_ServicesPage(driver)
        servicespage.check_for_Our_Services()

    #Navigating through all the services pages and checking for Squish GUI Testing Logo in the Automated GUI testing and Embedded testing pages.(4)
    #Checking for absence of the Squish GUI Testing Logo in the API testing page.(4)
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