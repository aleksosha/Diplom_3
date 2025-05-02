from pages.base_page import BasePage
from locators.feed_locators import FeedPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re

class FeedPage(BasePage):
  
    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site/feed")

    def click_first_order(self):
     
        try:
            self.click_element(FeedPageLocators.FIRST_ORDER)
        except Exception as e:
            raise Exception(f"Не кликнут первый заказ: {str(e)}") from e

    def is_modal_opened(self):
       
        try:
            self.wait_for_element_visible(FeedPageLocators.MODAL_TITLE)
            return True
        except TimeoutException:
            return False

    def is_order_list_displayed(self):
       
        try:
            self.wait_for_element_visible(FeedPageLocators.ORDER_LIST)
            return True
        except TimeoutException:
            return False
            
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
            
    def get_total_done_counter(self):
        try:
            total_done_element = self.wait_for_element_visible(FeedPageLocators.TOTAL_DONE_COUNTER)
            total_done_text = self.get_element_text(FeedPageLocators.TOTAL_DONE_COUNTER)
            
            count = int(total_done_text.strip())
            return count
        except (TimeoutException, NoSuchElementException, ValueError) as e:
            return 0
            
    def get_total_today_counter(self):
        try:
            total_today_element = self.wait_for_element_visible(FeedPageLocators.TOTAL_TODAY_COUNTER)
            total_today_text = self.get_element_text(FeedPageLocators.TOTAL_TODAY_COUNTER)
            
            count = int(total_today_text.strip())
            return count
        except (TimeoutException, NoSuchElementException, ValueError) as e:
            return 0
            
    def get_in_progress_orders(self):
        try:
            self.wait_for_element_visible(FeedPageLocators.IN_PROGRESS_ORDERS)
            
            in_progress_elements = self.find_elements(FeedPageLocators.IN_PROGRESS_ORDERS)
            
            in_progress_orders = [element.text for element in in_progress_elements]
            
            return in_progress_orders
        except (TimeoutException, NoSuchElementException) as e:
            return []
            
    def is_order_in_progress(self, order_number):
        try:
            in_progress_orders = self.get_in_progress_orders()
            
            is_in_progress = order_number in in_progress_orders or f"0{order_number}" in in_progress_orders
            
            return is_in_progress
        except Exception as e:
            return False
