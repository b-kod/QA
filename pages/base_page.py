# базовая страница с вспомогательными методами работы с драйвером, от которой будут унаследованы все остальные классы
import math
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
	# метод-конструктор, которвый вызывается, когда создается новый объект
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	# метод, открывающий нужную страницу в браузере
	def open(self):
		self.browser.get(self.url)

	# переход на страницу авторизации
	def go_to_login_page(self):
		login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		login_link.click()

	# переход на страницу корзины с товарами
	def go_to_basket_page(self):
		basket_page_link = self.browser.find_element(*BasePageLocators.BASKET_PAGE_LINK)
		basket_page_link.click()

	# проверяем, если ли на странице ссылка для авторизации
	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

	# проверяет, залогинен ли пользователь 
	def should_be_authorized_user(self):
		assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
			" probably unauthorised user"

	# метод поиска элемента, возвращающий True / False
	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True

	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True

		return False

	def is_disappeared(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).\
				until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
			
		return True

	# реализация подсчета задачи на странице с товаром для получения промо-кода
	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")