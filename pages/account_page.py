from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from selenium.common.exceptions import TimeoutException

class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=AccountPageLocators.ACCOUNT_PAGE_URL)

    def is_account_page_opened(self):
  
        return self.get_current_url() == AccountPageLocators.ACCOUNT_PAGE_URL

    def click_order_history_link(self):

        try:
            self.click_element(AccountPageLocators.ORDER_HISTORY_LINK)
            
            order_history_url = "https://stellarburgers.nomoreparties.site/account/order-history"
            self.wait_for_url_to_be(order_history_url)
        except Exception as e:
            raise Exception(f"Нет перехода на страницу Заказов: {str(e)}") from e

    def is_order_history_page_opened(self):
    
        order_history_url = "https://stellarburgers.nomoreparties.site/account/order-history"
        return self.get_current_url() == order_history_url

    def click_logout_button(self):
    
        try:
            self.click_element(AccountPageLocators.LOGOUT_BUTTON)
            
            login_url = "https://stellarburgers.nomoreparties.site/login"
            self.wait_for_url_to_be(login_url)
        except Exception as e:
            raise Exception(f"Не вышло разлогиниться: {str(e)}") from e

    def is_login_page_opened(self):
      
        login_url = "https://stellarburgers.nomoreparties.site/login"
        return self.get_current_url() == login_url
