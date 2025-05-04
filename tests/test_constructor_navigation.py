import pytest
import allure
from pages.header_page import HeaderPage


class TestConstructorNavigation:
    @allure.title("Проверка перехода на страницу конструктора")
    def test_navigation_to_constructor(self, driver, base_url):
        header = HeaderPage(driver)
        header.open_feed_page()
        
        header.click_constructor_button()
        
        assert header.is_constructor_page_opened(), "Переход по кнопке 'Конструктор' не удался"
