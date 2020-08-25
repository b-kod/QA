# связан с главной страницей сайта
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
	def __init__(self, *args, **kwargs):
		super(MainPage, self).__init__(*args, **kwargs)