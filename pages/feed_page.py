from pages.base_page import BasePage
from locators.feed_locators import FeedPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import URLs
import re
import time
import allure

class FeedPage(BasePage):
  
    def __init__(self, driver):
        super().__init__(driver, url=URLs.FEED_URL)
        
    @allure.step('Открытие страницы ленты заказов')
    def open_feed_page(self):
        self.open()
        
    @allure.step('Ожидание загрузки списка заказов')
    def wait_for_orders_to_load(self):
        self.wait_for_element_visible(FeedPageLocators.ORDER_LIST)
        
    @allure.step('Ожидание загрузки счетчика выполненных заказов')
    def wait_for_total_done_counter(self):
        self.wait_for_element_visible(FeedPageLocators.TOTAL_DONE_COUNTER)
        
    @allure.step('Ожидание загрузки счетчика заказов за сегодня')
    def wait_for_total_today_counter(self):
        self.wait_for_element_visible(FeedPageLocators.TOTAL_TODAY_COUNTER)
        
    @allure.step('Ожидание увеличения счетчика выполненных заказов')
    def wait_for_total_done_increase(self, initial_value, timeout=10):
        self.wait_for_total_done_counter()
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_value = self.get_total_done_counter()
            if current_value > initial_value:
                return current_value
            
        
        return self.get_total_done_counter()
        
    @allure.step('Ожидание увеличения счетчика заказов за сегодня')
    def wait_for_total_today_increase(self, initial_value, timeout=10):
        self.wait_for_total_today_counter()
    
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_value = self.get_total_today_counter()
            if current_value > initial_value:
                return current_value
        
        return self.get_total_today_counter()
        
    @allure.step('Ожидание появления заказа {order_number} в списке "В работе"')
    def wait_for_order_in_progress(self, order_number, timeout=10):

        self.wait_for_orders_to_load()
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_order_in_progress(order_number):
                return True
   
        return False

    @allure.step('Клик по первому заказу')
    def click_first_order(self):
        @self.handle_exceptions("Не кликнут первый заказ")
        def _click_first_order(self):
            self.click_element(FeedPageLocators.FIRST_ORDER)
        
        _click_first_order(self)

    @allure.step('Проверка открытия модального окна')
    def is_modal_opened(self):
        try:
            self.wait_for_element_visible(FeedPageLocators.MODAL_TITLE)
            return True
        except TimeoutException:
            return False

    @allure.step('Проверка отображения списка заказов')
    def is_order_list_displayed(self):
        try:
            self.wait_for_element_visible(FeedPageLocators.ORDER_LIST)
            return True
        except TimeoutException:
            return False
            
    @allure.step('Получение общего количества выполненных заказов')
    def get_total_done_count(self):
        try:
            total_done_element = self.wait_for_element_visible(FeedPageLocators.TOTAL_DONE_COUNT)
            total_done_text = self.get_element_text(FeedPageLocators.TOTAL_DONE_COUNT)
        
            match = re.search(r'\d+', total_done_text)
            if match:
                count = int(match.group())
                return count
            else:
                return 0
        except (TimeoutException, NoSuchElementException, ValueError) as e:
            return 0
            
    @allure.step('Получение значения счетчика выполненных заказов')
    def get_total_done_counter(self):
        try:
            total_done_element = self.wait_for_element_visible(FeedPageLocators.TOTAL_DONE_COUNTER)
            total_done_text = self.get_element_text(FeedPageLocators.TOTAL_DONE_COUNTER)
            
            count = int(total_done_text.strip())
            return count
        except (TimeoutException, NoSuchElementException, ValueError) as e:
            return 0
            
    @allure.step('Получение значения счетчика заказов за сегодня')
    def get_total_today_counter(self):
        try:
            total_today_element = self.wait_for_element_visible(FeedPageLocators.TOTAL_TODAY_COUNTER)
            total_today_text = self.get_element_text(FeedPageLocators.TOTAL_TODAY_COUNTER)
            
            count = int(total_today_text.strip())
            return count
        except (TimeoutException, NoSuchElementException, ValueError) as e:
            return 0
            
    @allure.step('Получение списка заказов в работе')
    def get_in_progress_orders(self):
        try:
            self.wait_for_element_visible(FeedPageLocators.IN_PROGRESS_ORDERS)
            
            in_progress_elements = self.find_elements(FeedPageLocators.IN_PROGRESS_ORDERS)
            
            in_progress_orders = [element.text for element in in_progress_elements]
            
            return in_progress_orders
        except (TimeoutException, NoSuchElementException) as e:
            return []
            
    @allure.step('Проверка наличия заказа {order_number} в списке заказов в работе')
    def is_order_in_progress(self, order_number):
        try:
            in_progress_orders = self.get_in_progress_orders()
            
            is_in_progress = order_number in in_progress_orders or f"0{order_number}" in in_progress_orders
            
            return is_in_progress
        except Exception as e:
            return False
