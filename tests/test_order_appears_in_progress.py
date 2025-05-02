import pytest
import time
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.header_page import HeaderPage

user_credentials = [
    pytest.param("drobotunalexandra@yandex.ru", "drobotun123", id="valid_user"),
]

@pytest.mark.parametrize("email, password", user_credentials)
def test_order_appears_in_progress(driver, base_url, email, password):

    try:
        driver.get(base_url)
        
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        
        main_page.drag_and_drop_ingredient()
        main_page.wait_for_ingredient_in_basket()
        
        header_page.click_login_button()
        
        login_page = LoginPage(driver)
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()
        
        time.sleep(2)
        
        main_page.click_order_button()
        
        main_page.wait_for_order_confirmation_modal()
        
        time.sleep(5)
        
        order_number = main_page.get_order_number()
        
        main_page.close_modal()
        
        main_page.wait_for_modal_to_disappear()
        
        feed_page = FeedPage(driver)
        feed_page.open()
        
        time.sleep(5)
        
        is_in_progress = feed_page.is_order_in_progress(order_number)
        
        assert is_in_progress, f"Номер заказа {order_number} не появился в работе"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
