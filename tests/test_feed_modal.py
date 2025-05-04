import pytest
import allure
from pages.feed_page import FeedPage


class TestFeedModal:
    @allure.title("Проверка открытия модального окна заказа в ленте")
    def test_order_modal_opens(self, driver, base_url):
        page = FeedPage(driver)
        page.open_feed_page()
        
        page.click_first_order()
        
        assert page.is_modal_opened(), "Модальное окно не открылось после клика на заказ"
