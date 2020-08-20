# связан с главной страницей сайта
from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
	def go_to_login_page(self):
		login_link = self.browser_find_element(*MainPageLocators.LOGIN_LINK)
		login_link.click()
		return LoginPage(browser=self.browser, url=self.browser.current_url)

	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

	def should_be_login_form(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented"

	def should_be_register_form(self):
		assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not presented"