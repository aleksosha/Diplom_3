import pytest
from pages.header_page import HeaderPage

def test_navigation_to_constructor(driver, base_url):

    try:
        feed_url = f"{base_url}/feed"
        driver.get(feed_url)
        
        header = HeaderPage(driver)
        header.click_constructor_button()
        
        expected_url = base_url.rstrip('/')
        actual_url = driver.current_url.rstrip('/')
        
        assert actual_url == expected_url, f"Переход по кнопке 'Конструктор' не удался. Ожидался URL: {expected_url}, получен: {actual_url}"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
