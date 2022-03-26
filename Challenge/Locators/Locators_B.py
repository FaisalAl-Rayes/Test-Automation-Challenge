from selenium.webdriver.common.by import By




'''This module holds the locators needed for automating Test B'''




class Locators():
    SERVICES_TAB = (By.XPATH,'/html/body/div/div/div[1]/a[3]')
    OUR_SERVICES_TEXT = '//h1[text()="Our Services"]'
    SQUISH_GUI_LOGO = '//a[@href="https://www.froglogic.com/squish/"]'
    AUTOMATED_GUI_TESTING = (By.XPATH,'//h4[text()="Automated GUI testing"]')
    EMBEDDED_TESTING = (By.XPATH,'//h4[text()="Embedded testing"]')
    MOBILE_APPLICATION_TESTING = (By.XPATH,'//h4[text()="Mobile application testing"]')
    WEB_TESTING = (By.XPATH,'//h4[text()="Web testing"]')
    API_TESTING = (By.XPATH,'//h4[text()="API testing"]')
    LOAD_AND_PERFORMANCE_TESTING = (By.XPATH,'//h4[text()="Load & Performance testing"]')
    TOOL_INTEGRATION_DEVELOPMENT = (By.XPATH,'//h4[text()="Tool integration development"]')