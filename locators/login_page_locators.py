from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa')
