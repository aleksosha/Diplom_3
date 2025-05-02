import pytest
from pages.main_page import MainPage

test_data = [
    pytest.param(2, id="add_two_ingredients")
]

@pytest.mark.parametrize("num_ingredients", test_data)
def test_add_ingredient_in_basket(driver, base_url, num_ingredients):

    try:
        driver.get(base_url)
        main_page = MainPage(driver)
        
        initial_counter = 0
        
        for i in range(num_ingredients):
            main_page.drag_and_drop_ingredient()
            main_page.wait_for_ingredient_in_basket()
        
        counter_value = main_page.get_counter_value()
        
        expected_value = initial_counter + num_ingredients
        assert counter_value == expected_value, f"Ожидалось число {expected_value}, но пришло {counter_value}"
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
