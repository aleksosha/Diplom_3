from selenium.webdriver.common.by import By

class HeaderLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
