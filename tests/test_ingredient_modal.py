import pytest
from pages.main_page import MainPage

def test_ingredient_modal_opens(driver, base_url):

    try:
        driver.get(base_url)
        
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        
        assert main_page.is_ingredient_modal_visible(), "Модальное окно не открылось после клика на ингредиент"
        
        expected_title = "Детали ингредиента"
        actual_title = main_page.get_modal_title_text()
        assert actual_title == expected_title, f"Заголовок модального окна некорректен. Ожидалось: {expected_title}, получено: {actual_title}"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
