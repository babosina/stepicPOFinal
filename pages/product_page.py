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

    def assert_product_added_to_cart(self):
        in_cart_text = self.browser.find_element(*ProductPageLocators.IN_CART_SUCCESS).text
        assert in_cart_text == "The shellcoder's handbook has been added to your basket.", f"Actual text {in_cart_text}"

    def assert_basket_price(self):
        basket_total_price_text = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert basket_total_price_text == "Your basket total is now £9.99", f"Actual text is {basket_total_price_text}"
