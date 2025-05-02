from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self, driver, url=None, timeout=10):

        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout)
    
    def open(self):

        if not self.url:
            raise Exception(f"URL не настроен {self.__class__.__name__}")
        
        self.driver.get(self.url)
        return self
    
    def find_element(self, locator, timeout=None):

        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f"Элемент не найден: {locator}")
    
    def find_elements(self, locator, timeout=None):

        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []
    
    def click_element(self, locator, timeout=None):
     
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except (TimeoutException, ElementClickInterceptedException) as e:
            raise ElementClickInterceptedException(f"Не кликнут элемент: {locator}. Ошибка: {str(e)}")
    
    def enter_text(self, locator, text, clear=True, timeout=None):
       
        element = self.find_element(locator, timeout)
        try:
            if clear:
                element.clear()
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"Не введен текст в поле: {locator}. Ошибка: {str(e)}")
    
    def is_element_visible(self, locator, timeout=None):
       
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=None):
        
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_visible(self, locator, timeout=None):
       
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Элемент недоступен: {locator}")
    
    def wait_for_element_invisible(self, locator, timeout=None):
       
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Элемент доступен: {locator}")
    
    def wait_for_url_to_be(self, url, timeout=None):
       
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.url_to_be(url))
        except TimeoutException:
            current_url = self.driver.current_url
            raise TimeoutException(f"URL не соответствует ОР. ОР: {url}, ФР: {current_url}")
    
    def wait_for_url_contains(self, partial_url, timeout=None):
        
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.url_contains(partial_url))
        except TimeoutException:
            current_url = self.driver.current_url
            raise TimeoutException(f"URL не соответствует ОР. ОР: {partial_url}, ФР: {current_url}")
    
    def get_current_url(self):
       
        return self.driver.current_url
    
    def drag_and_drop(self, source_locator, target_locator):
       
        try:
            source = self.find_element(source_locator)
            target = self.find_element(target_locator)
            
            actions = ActionChains(self.driver)
            actions.click_and_hold(source).move_to_element(target).release().perform()
        except Exception as e:
            raise Exception(f"Нет получилось дрэг'н'дропнуть. Ошибка: {str(e)}")
    
    def get_element_text(self, locator, timeout=None):
        
        element = self.find_element(locator, timeout)
        try:
            return element.text
        except Exception as e:
            raise Exception(f"Не получен текст: {locator}. Ошибка: {str(e)}")
    
    def get_element_attribute(self, locator, attribute, timeout=None):
        
        element = self.find_element(locator, timeout)
        try:
            return element.get_attribute(attribute)
        except Exception as e:
            raise Exception(f"Не получен аттрибут '{attribute}' элемента: {locator}. Ошибка: {str(e)}")
