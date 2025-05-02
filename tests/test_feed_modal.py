import pytest
from pages.feed_page import FeedPage


def test_order_modal_opens(driver, base_url):

    try:
        
        page = FeedPage(driver)
        page.open()
        
        page.click_first_order()
        
        assert page.is_modal_opened(), "Модальное окно не открылось после клика на заказ"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
