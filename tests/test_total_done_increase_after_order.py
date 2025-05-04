import pytest
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.header_page import HeaderPage


class TestTotalDoneIncreaseAfterOrder:
    @allure.title("Проверка увеличения счетчика выполненных заказов после заказа")
    def test_total_done_increase_after_order(self, driver, base_url):
        email = "drobotunalexandra@yandex.ru"
        password = "drobotun123"
        
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        header_page = HeaderPage(driver)
        
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        
        feed_page.wait_for_total_done_counter()
        
        initial_total_done = feed_page.get_total_done_counter()
        
        header_page.click_constructor_button()

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
        
        main_page.close_order_modal()
        
        main_page.wait_for_element_invisible(main_page.locators.ORDER_CONFIRMATION_MODAL)
        
        feed_page.open_feed_page()
        
        new_total_done = feed_page.wait_for_total_done_increase(initial_total_done)
        
        assert new_total_done > initial_total_done, f"Значение не увеличилось. Изначально: {initial_total_done}, Новое: {new_total_done}"
