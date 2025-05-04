import pytest
import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from conftest import driver


class TestAccountPage:
    @allure.title("Проверка успешного перехода на страницу личного кабинета")
    def test_successful_account_page_navigation(self, driver):
        email = "drobotunalexandra@yandex.ru"
        password = "drobotun123"
        
        login_page = LoginPage(driver)
        login_page.login(email, password)
        
        login_page.wait_for_login_completion()
        
        account_page = login_page.click_account_button()
        is_account_page_opened = account_page.is_account_page_opened()
        
        assert is_account_page_opened, "Переход на страницу Личного кабинета не выполнен"
    
    @allure.title("Проверка невозможности перехода на страницу личного кабинета с неверными учетными данными")
    @pytest.mark.parametrize("email, password", [
        pytest.param("invalid@example.com", "wrongpassword", id="invalid_credentials"),
        pytest.param("", "drobotun123", id="empty_email"),
        pytest.param("drobotunalexandra@yandex.ru", "", id="empty_password")
    ])
    def test_unsuccessful_account_page_navigation(self, driver, email, password):
        login_page = LoginPage(driver)
        login_page.login(email, password)
 
        with pytest.raises(Exception):
            account_page = login_page.click_account_button()
            assert not account_page.is_account_page_opened(), f"Логин должен быть не успешен с: {email} и паролем: {password}, но был успешен"
