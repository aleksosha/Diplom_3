import pytest
from pages.forgot_password_page import ForgotPasswordPage

def test_navigate_to_forgot_password_page(driver, base_url):

    try:
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        
        forgot_password_page.click_forgot_password_link()
        
        current_url = driver.current_url
        expected_url_part = "/forgot-password"
        
        assert expected_url_part in current_url, f"Переход на страницу восстановления пароля не выполнен. URL не содержит {expected_url_part}"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
