import pytest
import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TestLogout:
    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self, driver, base_url):
        email = "drobotunalexandra@yandex.ru"
        password = "drobotun123"
        
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        
        login_page.wait_for_login_completion()
        
        account_page = login_page.click_account_button()
        
        assert account_page.is_account_page_opened(), "Не открылась страница личного кабинета"
        
        account_page.click_logout_button()
        
        assert account_page.is_login_page_opened(), "Не произошёл переход на страницу логина после выхода"
