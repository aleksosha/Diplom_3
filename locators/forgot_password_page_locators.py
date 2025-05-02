from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/forgot-password']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    EYE_ICON = (By.CSS_SELECTOR, "div.input__icon-action svg")
