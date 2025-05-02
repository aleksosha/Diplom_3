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
def test_total_today_increase_after_order(driver, base_url, email, password):

    try:
        driver.get(base_url)
        
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        
        feed_page = FeedPage(driver)
        feed_page.open()
        
        time.sleep(2)
        
        initial_total_today = feed_page.get_total_today_counter()
        
        header_page.click_constructor_button()
        
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
        
        time.sleep(3)
        
        main_page.close_modal()
        
        main_page.wait_for_modal_to_disappear()
        
        feed_page.open()
        
        time.sleep(2)
        
        new_total_today = feed_page.get_total_today_counter()
        
        assert new_total_today > initial_total_today, f"Значение не увеличилось. Изначально: {initial_total_today}, Новое: {new_total_today}"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
