import pytest

# Тестовые данные для страницы сброса пароля
reset_password_test_data = [
    pytest.param("testemail@example.com", True, id="valid_email"),
    pytest.param("invalid-email", False, id="invalid_email_format"),
    pytest.param("", False, id="empty_email"),
    pytest.param("very.long.email.address.that.exceeds.normal.length.limits.and.might.cause.issues.with.form.validation@example.com", False, id="very_long_email")
]
