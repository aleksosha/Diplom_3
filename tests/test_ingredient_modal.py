import pytest
import allure
from pages.main_page import MainPage


class TestIngredientModal:
    @allure.title("Проверка открытия модального окна ингредиента")
    def test_ingredient_modal_opens(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_first_ingredient()
        
        assert main_page.is_ingredient_modal_visible(), "Модальное окно не открылось после клика на ингредиент"
        
        expected_title = "Детали ингредиента"
        actual_title = main_page.get_modal_title_text()
        assert actual_title == expected_title, f"Заголовок модального окна некорректен. Ожидалось: {expected_title}, получено: {actual_title}"
