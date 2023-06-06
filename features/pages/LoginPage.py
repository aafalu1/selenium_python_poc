import this

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    elements = {
        'btn_myaccount': (By.XPATH, "//span[text()='My Account']"),
        'lnk_login': (By.LINK_TEXT, 'Login')
    }
    def click_myaccount(self):
        self.click_element(LoginPage.elements['btn_myaccount'])

    def click_on_login_link_option(self):
        self.click_element(LoginPage.elements['lnk_login'])

    def enter_email(self, text_to_enter):
        self.enter_value()