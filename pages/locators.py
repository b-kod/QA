# файл для вынесения селекторов во внешнюю переменную
from selenium.webdriver.common.by import By

class BasePageLocators():
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGON_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_PAGE_LINK = (By.XPATH, '//span/a[contains(@class, "btn")]')

class LoginPageLocators():
	LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_USER_EMAIL = (By.NAME, "registration-email")
	REGISTER_USER_PASSWORD = (By.NAME, "registration-password1")
	REGISTER_USER_PASSWORD_CONFIRM = (By.NAME, "registration-password2")
	REGISTER_USER_SUBMIT_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
	BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
	BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
	BOOK_NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
	BOOK_PRICE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")

class BasketPageLocators():
	EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")