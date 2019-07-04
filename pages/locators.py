from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_LINK = (By.ID, "registration_link")


class LoginPageLocators:

    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PWD = (By.ID, "id_login-password")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PWD = (By.ID, "id_registration-password1")
    REGISTER_REPEAT_PWD = (By.ID, "id_registration-password2")


class ProductPageLocators:

    ADD_TO_CART = (By.ID, "add_to_basket_form")
    IN_CART_SUCCESS = (By.XPATH, "//div[@id='messages']/div[1]/div")
    PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    BASKET_TOTAL_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p[1]")
