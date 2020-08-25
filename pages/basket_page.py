from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
	def should_be_empty_basket(self):
		message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
		assert message == "Your basket is empty. Continue shopping", "Basket is not empty"
