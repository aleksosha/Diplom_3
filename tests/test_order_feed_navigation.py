import pytest
import allure
from pages.header_page import HeaderPage


class TestOrderFeedNavigation:
    @allure.title("Проверка перехода на страницу ленты заказов")
    def test_navigation_to_order_feed(self, driver, base_url):
        header = HeaderPage(driver)
        header.open_main_page()
        
        header.click_order_feed_button()
        
        assert header.is_feed_page_opened(), "Переход по кнопке 'Лента заказов' не удался"
