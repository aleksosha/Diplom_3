from selenium.webdriver.common.by import By

class MainPageLocators:
        FIRST_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/ancestor::a')
        MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]')
        MODAL_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
        CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS')
        TARGET_AREA = (By.CSS_SELECTOR, '.constructor-element_pos_top')
        COUNTER = (By.CSS_SELECTOR, ".counter_counter__num__3nue1")
        CONSTRUCTOR_ROW = (By.CLASS_NAME, "constructor-element__row")
        ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
        ORDER_CONFIRMATION_MODAL = (By.CSS_SELECTOR, '.Modal_modal__contentBox__sCy8X')
        ORDER_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS')
        ORDER_NUMBER = (By.CSS_SELECTOR, '.text_type_digits-large')
