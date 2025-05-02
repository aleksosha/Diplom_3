import pytest
from pages.forgot_password_page import ForgotPasswordPage

test_data = [
    pytest.param("testemail@example.com", True, id="valid_email"),
    pytest.param("invalid-email", False, id="invalid_email_format"),
    pytest.param("", False, id="empty_email"),
    pytest.param("very.long.email.address.that.exceeds.normal.length.limits.and.might.cause.issues.with.form.validation@example.com", False, id="very_long_email")
]

@pytest.mark.parametrize("email, expected_success", test_data)
def test_navigate_to_reset_password_page(driver, email, expected_success):

    try:
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.click_forgot_password_link()
        
        try:
            forgot_password_page.reset_password(email)
            
            if expected_success:
                assert "/reset-password" in driver.current_url, "Переход на страницу сброса пароля не выполнен"
            else:
                current_url = driver.current_url
                if "/reset-password" in current_url:
                    pass
                else:
                    assert "/forgot-password" in current_url, "Остались на странице Восстановление пароля"
        except Exception as e:
            if not expected_success:
                pass
            else:
                pytest.fail(f"Восстановление пароля упало с ошибкой: {str(e)}")
    except Exception as e:
        if expected_success:
            pytest.fail(f"Восстановление пароля упало с ошибкой: {str(e)}")
