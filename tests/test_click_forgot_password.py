import pytest
import allure
from pages.forgot_password_page import ForgotPasswordPage


class TestClickForgotPassword:
    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_navigate_to_forgot_password_page(self, driver, base_url):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        
        forgot_password_page.click_forgot_password_link()
        
        assert forgot_password_page.is_forgot_password_page_opened(), "Переход на страницу восстановления пароля не выполнен"
