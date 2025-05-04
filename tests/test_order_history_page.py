import pytest
import allure
from pages.login_page import LoginPage


class TestOrderHistoryPage:
    @allure.title("Проверка перехода на страницу истории заказов")
    def test_order_history_page(self, driver, base_url):
        email = "drobotunalexandra@yandex.ru"
        password = "drobotun123"
        
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        
        login_page.wait_for_login_completion()
        
        account_page = login_page.click_account_button()
        
        assert account_page.is_account_page_opened(), "Переход на страницу Личного кабинета не выполнен"
        
        account_page.click_order_history_link()
        
        assert account_page.is_order_history_page_opened(), "Переход на страницу Истории заказов не выполнен"
