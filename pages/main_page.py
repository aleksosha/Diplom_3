from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, url="https://stellarburgers.nomoreparties.site")
        self.locators = MainPageLocators

    def click_first_ingredient(self):

        try:
            self.click_element(self.locators.FIRST_INGREDIENT)
        except Exception as e:
            raise

    def wait_for_modal_to_appear(self):

        try:
            self.wait_for_element_visible(self.locators.MODAL_WINDOW)
        except TimeoutException as e:
            raise TimeoutException("Модалка не появилась") from e

    def close_modal(self):

        try:
            self.wait_for_modal_to_appear()  # Ensure modal is open
            self.click_element(self.locators.CLOSE_MODAL_BUTTON)
        except Exception as e:
            raise

    def wait_for_modal_to_disappear(self):

        try:
            self.wait_for_element_invisible(self.locators.MODAL_WINDOW)
        except TimeoutException as e:
            raise TimeoutException("Модалка не появилась") from e

    def drag_and_drop_ingredient(self):

        try:
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
        except Exception as e:
            raise

    def wait_for_ingredient_in_basket(self):
   
        try:
            self.wait_for_element_visible(self.locators.CONSTRUCTOR_ROW)
        except TimeoutException as e:
            raise TimeoutException("Ингридиент не добавлен") from e

    def get_counter_value(self):

        try:
            counter_text = self.get_element_text(self.locators.COUNTER)
            return int(counter_text.strip())
        except (ValueError, Exception) as e:
            raise Exception(f"Не получено значение: {str(e)}")

    def click_order_button(self):

        try:
            self.click_element(self.locators.ORDER_BUTTON)
        except Exception as e:
            raise

    def wait_for_order_confirmation_modal(self):

        try:
            self.wait_for_element_visible(self.locators.ORDER_CONFIRMATION_MODAL)
        except TimeoutException as e:
            raise TimeoutException("Модалка подтверждения заказа не появилась") from e
            
    def is_ingredient_modal_visible(self):

        return self.is_element_visible(self.locators.MODAL_WINDOW)
        
    def get_modal_title_text(self):

        try:
            return self.get_element_text(self.locators.MODAL_TITLE)
        except Exception as e:
            raise Exception(f"Не получен текст модалки: {str(e)}")
            
    def get_order_number(self):

        try:
            self.wait_for_element_visible(self.locators.ORDER_NUMBER)
            order_number_text = self.get_element_text(self.locators.ORDER_NUMBER)
            return order_number_text
        except Exception as e:
            raise Exception(f"Не получен номер заказа: {str(e)}")
