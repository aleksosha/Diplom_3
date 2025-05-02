from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage(BasePage):
 
    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/login")

    def enter_email(self, email):

        try:
            self.enter_text(LoginPageLocators.EMAIL_FIELD, email)
        except Exception as e:
            raise Exception(f"Не введен email: {str(e)}") from e

    def enter_password(self, password):

        try:
            self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
        except Exception as e:
            raise Exception(f"Не введен пароль: {str(e)}") from e

    def click_login_button(self):
 
        try:
            self.click_element(LoginPageLocators.LOGIN_BUTTON)
        except Exception as e:
            raise Exception(f"Не кликнута кнопка Логина: {str(e)}") from e

    def click_account_button(self):
  
        try:
            self.click_element(AccountPageLocators.ACCOUNT_BUTTON)
            
            self.wait_for_url_to_be(AccountPageLocators.ACCOUNT_PAGE_URL)
            
            # Import here to avoid circular import
            from pages.account_page import AccountPage
            return AccountPage(self.driver)
        except Exception as e:
            raise Exception(f"Нет перехода на страницу Личного кабинета: {str(e)}") from e
            
    def login(self, email, password):

        try:
            self.open()
            self.enter_email(email)
            self.enter_password(password)
            self.click_login_button()
            return self
        except Exception as e:
            raise Exception(f"Логин не удался: {str(e)}") from e
