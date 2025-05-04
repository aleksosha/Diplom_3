import pytest

# Тестовые данные для страницы аккаунта
account_test_data = [
    pytest.param("drobotunalexandra@yandex.ru", "drobotun123", True, id="valid_credentials"),
    pytest.param("invalid@example.com", "wrongpassword", False, id="invalid_credentials"),
    pytest.param("", "drobotun123", False, id="empty_email"),
    pytest.param("drobotunalexandra@yandex.ru", "", False, id="empty_password")
]
