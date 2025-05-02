from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from selenium.common.exceptions import TimeoutException

class HeaderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_constructor_button(self):
 
        try:
            self.click_element(HeaderLocators.CONSTRUCTOR_BUTTON)
        except Exception as e:
            raise Exception(f"Не кликнута кнопка Конструктор: {str(e)}") from e

    def click_order_feed_button(self):
 
        try:
            self.click_element(HeaderLocators.ORDER_FEED_BUTTON)
        except Exception as e:
            raise Exception(f"Не кликнута кнопка Лента заказов: {str(e)}") from e
            
    def click_login_button(self):

        try:
            self.click_element(HeaderLocators.LOGIN_BUTTON)
        except Exception as e:
            raise Exception(f"Не кликнута кнопка Логина: {str(e)}") from e
