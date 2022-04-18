from Challenge.Pages.BasePage import BaseClass


class GoogleResultPage(BaseClass):

    #locators
    CA_LINK = '//div[@class="yuRUbf"]/a[@href="http://www.cyberalpaca.com/"]'         #XPATH locator.
    
    def __init__(self, driver):
        super().__init__(driver)

    #Checking method.
    def check_for_CA_Link(self):
        assert "www.cyberalpaca.com" in self._do_find_element_href(self.CA_LINK) , "Result not found"
    
    #Click on CyberAlpaca link
    def click_on_CA_link(self):
        self._do_click(self.CA_LINK)
