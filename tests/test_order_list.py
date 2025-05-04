import pytest
import allure
from pages.feed_page import FeedPage


class TestOrderList:
    @allure.title("Проверка отображения списка заказов на странице ленты")
    def test_order_list_visible_on_feed_page(self, driver, base_url):
        page = FeedPage(driver)
        page.open_feed_page()
        
        assert page.is_order_list_displayed(), "Список заказов не отображается на странице /feed"
