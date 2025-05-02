import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage

user_credentials = [
    pytest.param("drobotunalexandra@yandex.ru", "drobotun123", id="valid_user"),
]

@pytest.mark.parametrize("email, password", user_credentials)
def test_logout(driver, base_url, email, password):

    try:
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.enter_email(email)
        
        login_page.enter_password(password)
        
        login_page.click_login_button()
        
        account_page = login_page.click_account_button()
        
        assert account_page.is_account_page_opened(), "Не открылась страница личного кабинета"
        
        account_page.click_logout_button()
        
        assert account_page.is_login_page_opened(), "Не произошёл переход на страницу логина после выхода"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
