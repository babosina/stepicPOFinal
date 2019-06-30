from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'BABA' in self.browser.current_url

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no Login form on the page"

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no Registration form on the page"
