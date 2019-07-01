import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_product_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()
