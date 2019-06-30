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
