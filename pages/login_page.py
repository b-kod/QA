# страница авторизации/регистрации
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # заглушки для методов проверок
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_user_email = self.browser.find_element(*LoginPageLocators.REGISTER_USER_EMAIL).send_keys(email)
        register_user_password = self.browser.find_element(*LoginPageLocators.REGISTER_USER_PASSWORD).send_keys(password)
        register_user_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_USER_PASSWORD_CONFIRM).send_keys(password)
        register_user_submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_USER_SUBMIT_BUTTON).click()