from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
