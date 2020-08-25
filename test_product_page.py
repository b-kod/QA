import pytest
import time
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = BasePage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = BasePage(browser, link)
	page.open()
	page.go_to_login_page()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)
	page.open()
	page.add_item_to_basket()
	page.add_promo_code()

def test_quest_should_see_basket_button(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_add_to_basket_button()

def test_guest_should_see_the_same_book_price(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_item_to_basket()
	page.should_be_book_price()

def test_guest_should_see_the_same_product_name(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_item_to_basket()
	page.should_be_book_name()

@pytest.mark.xfail(reason="message is presented")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_item_to_basket()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.xfail(reason="message is not disappearing")
def test_guest_see_succes_message_dissapeared(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_item_to_basket()
	page.is_dissappeared()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
	page = BasePage(browser, link)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, link)
	basket_page.should_be_empty_basket()

class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		self.login_page = LoginPage(browser, link)
		self.login_page.open()
		email = str(time.time()) + "@fakemail.org"
		password = str(time.time()) + "winry123456"
		self.login_page.register_new_user(email, password)
		self.login_page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
		page = ProductPage(browser, link)
		page.open()
		page.add_item_to_basket()

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()
