from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from selenium.common.exceptions import TimeoutException
from urls import URLs
import allure

class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=URLs.ACCOUNT_PROFILE_URL)

    @allure.step('Проверка открытия страницы личного кабинета')
    def is_account_page_opened(self):
  
        return self.get_current_url() == URLs.ACCOUNT_PROFILE_URL

    @allure.step('Клик по ссылке История заказов')
    def click_order_history_link(self):
        @self.handle_exceptions("Нет перехода на страницу Заказов")
        def _click_order_history_link(self):
            self.click_element(AccountPageLocators.ORDER_HISTORY_LINK)
            self.wait_for_url_to_be(URLs.ORDER_HISTORY_URL)
        
        _click_order_history_link(self)

    @allure.step('Проверка открытия страницы истории заказов')
    def is_order_history_page_opened(self):
    
        return self.get_current_url() == URLs.ORDER_HISTORY_URL

    @allure.step('Клик по кнопке Выход')
    def click_logout_button(self):
        @self.handle_exceptions("Не вышло разлогиниться")
        def _click_logout_button(self):
            self.click_element(AccountPageLocators.LOGOUT_BUTTON)
            self.wait_for_url_to_be(URLs.LOGIN_URL)
        
        _click_logout_button(self)

    @allure.step('Проверка открытия страницы логина')
    def is_login_page_opened(self):
      
        return self.get_current_url() == URLs.LOGIN_URL
