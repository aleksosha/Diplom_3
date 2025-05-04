from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from urls import URLs
import allure


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=URLs.LOGIN_URL)

    @allure.step('Клик по ссылке Восстановить пароль')
    def click_forgot_password_link(self):
        @self.handle_exceptions("Не кликнута ссылка Восстановить пароль")
        def _click_forgot_password_link(self):
            self.click_element(ForgotPasswordPageLocators.FORGOT_PASSWORD_LINK)
        
        _click_forgot_password_link(self)

    @allure.step('Восстановление пароля с email {email}')
    def reset_password(self, email):
        @self.handle_exceptions("Не получилось восстановить пароль")
        def _reset_password(self, email):
            self.enter_text(ForgotPasswordPageLocators.EMAIL_FIELD, email)
            self.click_element(ForgotPasswordPageLocators.RESET_BUTTON)
            self.wait_for_url_contains("/reset-password")
        
        _reset_password(self, email)

    @allure.step('Клик по иконке глаза')
    def click_eye_icon(self):
        @self.handle_exceptions("Не кликнута иконка глаза")
        def _click_eye_icon(self):
            self.click_element(ForgotPasswordPageLocators.EYE_ICON)
        
        _click_eye_icon(self)

    @allure.step('Проверка видимости поля пароля')
    def is_password_field_visible(self):
        @self.handle_exceptions("Не проверено, что поле пароля доступно")
        def _is_password_field_visible(self):
            field_type = self.get_element_attribute(ForgotPasswordPageLocators.PASSWORD_FIELD, 'type')
            return field_type == 'text'
        
        return _is_password_field_visible(self)
            
    @allure.step('Проверка перехода на страницу восстановления пароля')
    def is_forgot_password_page_opened(self):
        current_url = self.get_current_url()
        return "/forgot-password" in current_url
        
    @allure.step('Проверка перехода на страницу сброса пароля')
    def is_reset_password_page_opened(self):
        current_url = self.get_current_url()
        return "/reset-password" in current_url
