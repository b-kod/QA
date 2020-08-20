# базовая страница с вспомогательными методами работы с драйвером, от которой будут унаследованы все остальные классы
from selenium.common.exceptions import NoSuchElementException

class BasePage():
	# метод-конструктор, которвый вызывается, когда создается новый объект
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	# метод, открывающий нужную страницу в браузере
	def open(self):
		self.browser.get(self.url)

	# метод поиска элемента, возвращающий True / False
	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True