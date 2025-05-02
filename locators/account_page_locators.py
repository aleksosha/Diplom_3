from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a')
    ACCOUNT_PAGE_URL = "https://stellarburgers.nomoreparties.site/account/profile"
    ORDER_HISTORY_LINK = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
