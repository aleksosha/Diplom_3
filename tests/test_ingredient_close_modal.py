import pytest
import allure
from pages.main_page import MainPage


class TestIngredientCloseModal:
    @allure.title("Проверка закрытия модального окна ингредиента")
    def test_modal_close_on_click(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_first_ingredient()
        
        main_page.wait_for_modal_to_appear()
        
        main_page.close_modal()
        
        main_page.wait_for_modal_to_disappear()
