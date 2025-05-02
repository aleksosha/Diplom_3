import pytest
from pages.main_page import MainPage

def test_modal_close_on_click(driver, base_url):

    try:
        driver.get(base_url)
        
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        
        main_page.wait_for_modal_to_appear()
        
        main_page.close_modal()
        
        main_page.wait_for_modal_to_disappear()
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
