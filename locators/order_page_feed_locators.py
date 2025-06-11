from selenium.webdriver.common.by import By

class OrderPageFeedLocators:
    ORDER_MODAL = (By.CLASS_NAME, "Modal_orderBox__1xWdi")
    ORDER_ITEM = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
    ORDER_HISTORY_TAB = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    ORDER_HISTORY_ITEM = (By.CLASS_NAME, "OrderHistory_orderHistory__qy1VB")
    ACCOUNT_TAB = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    COMPLETED_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_ORDERS = (By.CLASS_NAME, "OrderFeed_orderListReady__1YFem")
