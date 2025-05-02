import pytest
from pages.forgot_password_page import ForgotPasswordPage
from conftest import driver

test_data = [
    pytest.param("testemail@example.com", id="valid_email"),
]

@pytest.mark.parametrize("email", test_data)
def test_password_visibility_on_eye_icon_click(driver, base_url, email):

    try:
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        
        forgot_password_page.click_forgot_password_link()
        
        forgot_password_page.reset_password(email)
        
        forgot_password_page.click_eye_icon()
        
        assert forgot_password_page.is_password_field_visible(), "Пароль не стал видимым после клика на иконку глаза"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
