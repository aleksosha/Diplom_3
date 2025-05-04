from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from urls import URLs
import allure

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url=URLs.BASE_URL)
        self.locators = MainPageLocators
        
    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.open()
        
    @allure.step('Ожидание завершения процесса оформления заказа')
    def wait_for_order_processing(self):
        self.wait_for_element_visible(self.locators.ORDER_CONFIRMATION_MODAL)
        self.wait_for_element_visible(self.locators.ORDER_NUMBER)
        
    @allure.step('Ожидание полной загрузки модального окна подтверждения заказа')
    def wait_for_order_modal_fully_loaded(self):
        self.wait_for_element_visible(self.locators.ORDER_CONFIRMATION_MODAL)
        self.wait_for_element_visible(self.locators.ORDER_NUMBER)
        self.wait_for_element_clickable(self.locators.ORDER_MODAL_CLOSE_BUTTON)
    
    @allure.step('Закрытие модального окна подтверждения заказа')
    def close_order_modal(self):
        @self.handle_exceptions("Не удалось закрыть модальное окно подтверждения заказа")
        def _close_order_modal(self):
            self.wait_for_order_modal_fully_loaded()

            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.action_chains import ActionChains
            
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            
            self.wait_for_element_invisible(self.locators.ORDER_CONFIRMATION_MODAL)
        
        _close_order_modal(self)

    @allure.step('Клик по первому ингредиенту')
    def click_first_ingredient(self):
        @self.handle_exceptions("Не кликнут первый ингредиент")
        def _click_first_ingredient(self):
            self.click_element(self.locators.FIRST_INGREDIENT)
        
        _click_first_ingredient(self)

    @allure.step('Ожидание появления модального окна')
    def wait_for_modal_to_appear(self):
        @self.handle_exceptions("Модалка не появилась")
        def _wait_for_modal_to_appear(self):
            self.wait_for_element_visible(self.locators.MODAL_WINDOW)
        
        _wait_for_modal_to_appear(self)

    @allure.step('Закрытие модального окна')
    def close_modal(self):
        @self.handle_exceptions("Не удалось закрыть модальное окно")
        def _close_modal(self):
            self.wait_for_modal_to_appear()
            self.click_element(self.locators.CLOSE_MODAL_BUTTON)
        
        _close_modal(self)

    @allure.step('Ожидание исчезновения модального окна')
    def wait_for_modal_to_disappear(self):
        @self.handle_exceptions("Модалка не исчезла")
        def _wait_for_modal_to_disappear(self):
            self.wait_for_element_invisible(self.locators.MODAL_WINDOW)
        
        _wait_for_modal_to_disappear(self)

    @allure.step('Перетаскивание ингредиента в корзину')
    def drag_and_drop_ingredient(self):
        @self.handle_exceptions("Не удалось перетащить ингредиент в корзину")
        def _drag_and_drop_ingredient(self):
            try:
                if self.is_element_visible(self.locators.MODAL_WINDOW):
                    self.click_element(self.locators.CLOSE_MODAL_BUTTON)
                    self.wait_for_element_invisible(self.locators.MODAL_WINDOW)
            except Exception:
                pass

            source = self.find_element(self.locators.FIRST_INGREDIENT)
            target = self.find_element(self.locators.TARGET_AREA)
            
            actions = ActionChains(self.driver)
            actions.click_and_hold(source).move_to_element(target).release().perform()
        
        _drag_and_drop_ingredient(self)

    @allure.step('Ожидание появления ингредиента в корзине')
    def wait_for_ingredient_in_basket(self):
        @self.handle_exceptions("Ингридиент не добавлен")
        def _wait_for_ingredient_in_basket(self):
            self.wait_for_element_visible(self.locators.CONSTRUCTOR_ROW)
        
        _wait_for_ingredient_in_basket(self)

    @allure.step('Получение значения счетчика')
    def get_counter_value(self):
        @self.handle_exceptions("Не получено значение счетчика")
        def _get_counter_value(self):
            counter_text = self.get_element_text(self.locators.COUNTER)
            return int(counter_text.strip())
        
        return _get_counter_value(self)

    @allure.step('Клик по кнопке Оформить заказ')
    def click_order_button(self):
        @self.handle_exceptions("Не кликнута кнопка Оформить заказ")
        def _click_order_button(self):
            self.click_element(self.locators.ORDER_BUTTON)
        
        _click_order_button(self)

    @allure.step('Ожидание появления модального окна подтверждения заказа')
    def wait_for_order_confirmation_modal(self):
        @self.handle_exceptions("Модалка подтверждения заказа не появилась")
        def _wait_for_order_confirmation_modal(self):
            self.wait_for_element_visible(self.locators.ORDER_CONFIRMATION_MODAL)
        
        _wait_for_order_confirmation_modal(self)
            
    @allure.step('Проверка видимости модального окна ингредиента')
    def is_ingredient_modal_visible(self):

        return self.is_element_visible(self.locators.MODAL_WINDOW)
        
    @allure.step('Получение текста заголовка модального окна')
    def get_modal_title_text(self):
        @self.handle_exceptions("Не получен текст модалки")
        def _get_modal_title_text(self):
            return self.get_element_text(self.locators.MODAL_TITLE)
        
        return _get_modal_title_text(self)
            
    @allure.step('Получение номера заказа')
    def get_order_number(self):
        @self.handle_exceptions("Не получен номер заказа")
        def _get_order_number(self):
            self.wait_for_element_visible(self.locators.ORDER_NUMBER)
            
            def order_number_loaded(driver):
                order_number_element = self.find_element(self.locators.ORDER_NUMBER)
                order_number_text = order_number_element.text
                return order_number_text != "" and order_number_text != "9999"

            wait = WebDriverWait(self.driver, 15) 
            wait.until(order_number_loaded)
            
            order_number_text = self.get_element_text(self.locators.ORDER_NUMBER)
            return order_number_text
        
        return _get_order_number(self)
