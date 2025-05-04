import pytest
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.header_page import HeaderPage


class TestOrderAppearsInProgress:
    @allure.title("Проверка появления заказа в ленте в работе")
    def test_order_appears_in_progress(self, driver, base_url):
        email = "drobotunalexandra@yandex.ru"
        password = "drobotun123"
        
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        header_page = HeaderPage(driver)
        
        main_page.drag_and_drop_ingredient()
        main_page.wait_for_ingredient_in_basket()
        
        header_page.click_login_button()
        
        login_page = LoginPage(driver)
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        
        login_page.wait_for_login_completion()
        
        main_page.click_order_button()
        
        main_page.wait_for_order_confirmation_modal()
        
        main_page.wait_for_order_processing()
        
        order_number = main_page.get_order_number()
        
        main_page.close_order_modal()
        
        main_page.wait_for_element_invisible(main_page.locators.ORDER_CONFIRMATION_MODAL)
        
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()

        is_in_progress = feed_page.wait_for_order_in_progress(order_number)
        
        assert is_in_progress, f"Номер заказа {order_number} не появился в работе"
