import pytest
import allure
from pages.forgot_password_page import ForgotPasswordPage


class TestResetPassword:
    @allure.title("Проверка успешного перехода на страницу сброса пароля")
    def test_successful_reset_password_navigation(self, driver):
        email = "testemail@example.com"
        
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.click_forgot_password_link()
        forgot_password_page.reset_password(email)
        
        assert forgot_password_page.is_reset_password_page_opened(), "Переход на страницу сброса пароля не выполнен"
