import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from conftest import driver

user_credentials = [
    pytest.param("drobotunalexandra@yandex.ru", "drobotun123", True, id="valid_user"),
]

@pytest.mark.parametrize("email, password, expected_success", user_credentials)
def test_order_ingredient(driver, base_url, email, password, expected_success):

    try:
        login_page = LoginPage(driver)
        login_page.login(email, password)
        
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        
        counter_value = main_page.get_counter_value()
        expected_counter = 2 
        assert counter_value == expected_counter, f"Ожидалось значение {expected_counter}, но было получено {counter_value}"
        
        main_page.click_order_button()
        
        if expected_success:
            main_page.wait_for_order_confirmation_modal()
        else:
            pass
            
    except Exception as e:
        if expected_success:
            pytest.fail(f"Тест упал с ошибкой: {str(e)}")
