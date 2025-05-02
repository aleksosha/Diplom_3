from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/login")

    def click_forgot_password_link(self):
     
        try:
            self.click_element(ForgotPasswordPageLocators.FORGOT_PASSWORD_LINK)
        except Exception as e:
            raise Exception(f"Не кликнута ссылка Восстановить пароль: {str(e)}") from e

    def reset_password(self, email):
      
        try:
            self.enter_text(ForgotPasswordPageLocators.EMAIL_FIELD, email)
            self.click_element(ForgotPasswordPageLocators.RESET_BUTTON)
            
            self.wait_for_url_contains("/reset-password")
        except Exception as e:
            raise Exception(f"Не получилось восстановить пароль: {str(e)}") from e

    def click_eye_icon(self):
     
        try:
            self.click_element(ForgotPasswordPageLocators.EYE_ICON)
        except Exception as e:
            raise Exception(f"Не кликнута иконка глаза: {str(e)}") from e

    def is_password_field_visible(self):
     
        try:
            field_type = self.get_element_attribute(ForgotPasswordPageLocators.PASSWORD_FIELD, 'type')
            return field_type == 'text'
        except Exception as e:
            raise Exception(f"Не проверено, что поле пароля доступно: {str(e)}") from e
