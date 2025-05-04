import pytest
import allure
from pages.main_page import MainPage


class TestAddIngredient:
    @allure.title("Проверка добавления двух ингредиентов в корзину")
    def test_add_two_ingredients_in_basket(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        initial_counter = 0
        num_ingredients = 2
        
        for i in range(num_ingredients):
            main_page.drag_and_drop_ingredient()
            main_page.wait_for_ingredient_in_basket()
        
        counter_value = main_page.get_counter_value()
        
        expected_value = initial_counter + num_ingredients
        assert counter_value == expected_value, f"Ожидалось число {expected_value}, но пришло {counter_value}"
