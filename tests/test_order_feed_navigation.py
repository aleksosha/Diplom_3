import pytest
from pages.header_page import HeaderPage

def test_navigation_to_order_feed(driver, base_url):

    try:
        driver.get(base_url)
        
        header = HeaderPage(driver)
        header.click_order_feed_button()
        
        feed_url = f"{base_url}/feed"
        expected_url = feed_url.rstrip("/")
        actual_url = driver.current_url.rstrip("/")
        
        assert actual_url == expected_url, f"Переход по кнопке 'Лента заказов' не удался. Ожидался URL: {expected_url}, получен: {actual_url}"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
