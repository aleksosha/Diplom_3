from selenium.webdriver.common.by import By

class FeedPageLocators:
    FIRST_ORDER = (By.CSS_SELECTOR, 'li.OrderHistory_listItem__2x95r.mb-6:first-child')
    MODAL_TITLE = (By.CSS_SELECTOR, 'div.Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X.p-10')
    ORDER_LIST = (By.CSS_SELECTOR, 'ul.OrderFeed_list__OLh59')
    TOTAL_DONE_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")
    TOTAL_DONE_COUNTER = (By.CLASS_NAME, "OrderFeed_number__2MbrQ")
    TOTAL_TODAY_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")
    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, ".text_type_digits-default.mb-2")
