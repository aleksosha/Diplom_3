import pytest
from pages.feed_page import FeedPage

def test_order_list_visible_on_feed_page(driver, base_url):

    try:
        page = FeedPage(driver)
        page.open()
        
        assert page.is_order_list_displayed(), "Список заказов не отображается на странице /feed"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
