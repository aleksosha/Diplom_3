import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from conftest import driver



test_data = [
    pytest.param("drobotunalexandra@yandex.ru", "drobotun123", True, id="valid_credentials"),
    pytest.param("invalid@example.com", "wrongpassword", False, id="invalid_credentials"),
    pytest.param("", "drobotun123", False, id="empty_email"),
    pytest.param("drobotunalexandra@yandex.ru", "", False, id="empty_password")
]

@pytest.mark.parametrize("email, password, expected_success", test_data)
def test_account_page(driver, email, password, expected_success):

    login_page = LoginPage(driver)
    login_page.login(email, password)
    
    try:

        account_page = login_page.click_account_button()

        is_account_page_opened = account_page.is_account_page_opened()
        
        if expected_success:
            assert is_account_page_opened, "Переход на страницу Личного кабинета не выполнен"
        else:
            pytest.fail(f"Логин должен быть не успешен с: {email} и паролем: {password}, но был успешен")
    except Exception as e:
        if expected_success:
            pytest.fail(f"Логин должен быть успешен, но упала ошибка: {str(e)}")
