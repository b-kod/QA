from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
	def add_item_to_basket(self):
		basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
		basket_button.click()

	def add_promo_code(self):
		self.solve_quiz_and_get_code()

	def should_be_add_to_basket_button(self):
		assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Button is nor presented"

	def should_be_book_price(self):
		book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
		basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
		assert book_price == basket_price, "Price is not the same"

	def should_be_book_name(self):
		book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
		book_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
		assert book_name == book_basket, "Name is not the same"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"

	def is_dissappeared(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"
