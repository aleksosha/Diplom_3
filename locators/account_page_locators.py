from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX[href="/account"]')
    ORDER_HISTORY_LINK = (By.CSS_SELECTOR, 'a.Account_link__2ETsJ[href="/account/order-history"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'button.Account_button__14Yp3')
