from Challenge.Pages.BasePage import BasePage
from Challenge.Locators.Locators_B import Locators


class CA_ServicesPage(BasePage, Locators):

    def __init__(self, driver):
        super().__init__(driver)

    #Input methods.
    def click_on_Automated_GUI_testing(self):
        self.do_click(Locators.AUTOMATED_GUI_TESTING)
    
    def click_on_Embedded_testing(self):
        self.do_click(Locators.EMBEDDED_TESTING)
    
    def click_on_Mobile_application_testing(self):
        self.do_click(Locators.MOBILE_APPLICATION_TESTING)
    
    def click_on_Web_testing(self):
        self.do_click(Locators.WEB_TESTING)
    
    def click_on_API_testing(self):
        self.do_click(Locators.API_TESTING)
    
    def click_on_Load_and_Performance_testing(self):
        self.do_click(Locators.LOAD_AND_PERFORMANCE_TESTING)
    
    def click_on_Tool_integration_development(self):
        self.do_click(Locators.TOOL_INTEGRATION_DEVELOPMENT)

    #Checking methods.
    def check_for_Our_Services(self):
        self.do_find_element(Locators.OUR_SERVICES_TEXT)
        assert "Our Services" in self.do_find_element(Locators.OUR_SERVICES_TEXT).text, "Not Found"

    def check_for_Squish_GUI_Testing_Logo(self):
        self.do_find_element(Locators.SQUISH_GUI_LOGO)
        assert "www.froglogic.com/squish/" in self.do_find_element_href(Locators.SQUISH_GUI_LOGO)

    def check_for_missing_Squish_GUI_Testing_Logo(self):
        self.affirm_absence_of_element(Locators.SQUISH_GUI_LOGO)

    