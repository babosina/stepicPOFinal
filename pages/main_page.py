from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_btn = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_btn.click()

    def should_be_login_link(self):
        self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
