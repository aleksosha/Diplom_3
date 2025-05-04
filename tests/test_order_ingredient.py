import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestOrderIngredient:
    @allure.title("Проверка оформления заказа")
    def test_order_ingredient(self, driver, base_url):
        email = "drobotunalexandra@yandex.ru"
        password = "drobotun123"
        
        login_page = LoginPage(driver)
        login_page.login(email, password)
        
        login_page.wait_for_login_completion()
        
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        
        counter_value = main_page.get_counter_value()
        expected_counter = 2 
        assert counter_value == expected_counter, f"Ожидалось значение {expected_counter}, но было получено {counter_value}"
        
        main_page.click_order_button()
        
        main_page.wait_for_order_confirmation_modal()
