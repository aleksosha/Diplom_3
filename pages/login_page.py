from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from urls import URLs
import allure


class LoginPage(BasePage):
 
    def __init__(self, driver):
        super().__init__(driver, url=URLs.LOGIN_URL)
        
    @allure.step('Ожидание завершения процесса авторизации')
    def wait_for_login_completion(self):
        self.wait_for_url_contains(URLs.BASE_URL)
        self.wait_for_element_invisible(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Ввод email')
    def enter_email(self, email):
        @self.handle_exceptions("Не введен email")
        def _enter_email(self, email):
            self.enter_text(LoginPageLocators.EMAIL_FIELD, email)
        
        _enter_email(self, email)

    @allure.step('Ввод пароля')
    def enter_password(self, password):
        @self.handle_exceptions("Не введен пароль")
        def _enter_password(self, password):
            self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
        
        _enter_password(self, password)

    @allure.step('Клик по кнопке Войти')
    def click_login_button(self):
        @self.handle_exceptions("Не кликнута кнопка Логина")
        def _click_login_button(self):
            self.click_element(LoginPageLocators.LOGIN_BUTTON)
        
        _click_login_button(self)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_account_button(self):
        @self.handle_exceptions("Нет перехода на страницу Личного кабинета")
        def _click_account_button(self):
            self.click_element(AccountPageLocators.ACCOUNT_BUTTON)
            self.wait_for_url_to_be(URLs.ACCOUNT_PROFILE_URL)

            from pages.account_page import AccountPage
            return AccountPage(self.driver)
        
        return _click_account_button(self)
            
    @allure.step('Логин с email {email}')
    def login(self, email, password):
        @self.handle_exceptions("Логин не удался")
        def _login(self, email, password):
            self.open()
            self.enter_email(email)
            self.enter_password(password)
            self.click_login_button()
            return self
        
        return _login(self, email, password)
