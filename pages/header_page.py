from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from selenium.common.exceptions import TimeoutException
from urls import URLs
import allure

class HeaderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке Конструктор')
    def click_constructor_button(self):
        @self.handle_exceptions("Не кликнута кнопка Конструктор")
        def _click_constructor_button(self):
            self.click_element(HeaderLocators.CONSTRUCTOR_BUTTON)
        
        _click_constructor_button(self)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_feed_button(self):
        @self.handle_exceptions("Не кликнута кнопка Лента заказов")
        def _click_order_feed_button(self):
            self.click_element(HeaderLocators.ORDER_FEED_BUTTON)
        
        _click_order_feed_button(self)
            
    @allure.step('Клик по кнопке Войти')
    def click_login_button(self):
        @self.handle_exceptions("Не кликнута кнопка Логина")
        def _click_login_button(self):
            self.click_element(HeaderLocators.LOGIN_BUTTON)
        
        _click_login_button(self)
            
    @allure.step('Открытие страницы ленты заказов')
    def open_feed_page(self):
        self.driver.get(URLs.FEED_URL)
        
    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.driver.get(URLs.BASE_URL)
        
    @allure.step('Проверка перехода на главную страницу')
    def is_constructor_page_opened(self):
        current_url = self.get_current_url().rstrip('/')
        expected_url = URLs.BASE_URL.rstrip('/')
        return current_url == expected_url
        
    @allure.step('Проверка перехода на страницу ленты заказов')
    def is_feed_page_opened(self):
        current_url = self.get_current_url().rstrip('/')
        expected_url = URLs.FEED_URL.rstrip('/')
        return current_url == expected_url
