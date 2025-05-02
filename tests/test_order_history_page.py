import pytest
from pages.login_page import LoginPage

user_credentials = [
    pytest.param("drobotunalexandra@yandex.ru", "drobotun123", id="valid_user"),
]

@pytest.mark.parametrize("email, password", user_credentials)
def test_order_history_page(driver, base_url, email, password):

    try:
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.enter_email(email)
        
        login_page.enter_password(password)
        
        login_page.click_login_button()
        
        account_page = login_page.click_account_button()
        
        assert account_page.is_account_page_opened(), "Переход на страницу Личного кабинета не выполнен"
        
        account_page.click_order_history_link()
        
        assert account_page.is_order_history_page_opened(), "Переход на страницу Истории заказов не выполнен"
        
    except Exception as e:
        pytest.fail(f"Тест упал с ошибкой: {str(e)}")
