from selenium.webdriver.common.by import By

class FeedPageLocators:
    FIRST_ORDER = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]')
    MODAL_TITLE = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div')
    ORDER_LIST = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul')
    TOTAL_DONE_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")
    TOTAL_DONE_COUNTER = (By.CLASS_NAME, "OrderFeed_number__2MbrQ")
    TOTAL_TODAY_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")
    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, ".text_type_digits-default.mb-2")
