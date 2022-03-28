from Challenge.Pages.BasePage import BasePage


class GoogleResultPage(BasePage):

    #locators
    CA_LINK = '//a[@href="http://www.cyberalpaca.com/" and @role="button"]'         #XPATH locator.
    
    def __init__(self, driver):
        super().__init__(driver)

    #Checking method.
    def Find_CA_Link(self):
        
        return self.do_find_element_href(self.CA_LINK)
    
    #Click on CyberAlpaca link
    def click_on_CA_link(self):
        self.do_click(self.CA_LINK)
