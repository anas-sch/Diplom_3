from locators.order_page_feed_locators import OrderPageFeedLocators
from page_object.base_page import BasePage
from page_object.main_page import MainPage

class OrderPageFeed(BasePage):
    def open_order_details(self, order_index=0):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_ITEM)
        orders = self.driver.find_elements(*OrderPageFeedLocators.ORDER_ITEM)
        if not orders:
            raise ValueError("Заказы не найдены")
        orders[order_index].click()

    def order_modal_visible(self):
        return self.is_element_visible(OrderPageFeedLocators.ORDER_MODAL)

    def go_to_account(self):
        self.click_element(OrderPageFeedLocators.ACCOUNT_TAB)

    def go_to_order_history(self):
        self.click_element(OrderPageFeedLocators.ORDER_HISTORY_TAB)

    def get_completed_counter(self):
        element_text = self.find_element(OrderPageFeedLocators.COMPLETED_COUNTER).text
        return int(element_text.strip())

    def get_today_counter(self):
        element_text = self.find_element(OrderPageFeedLocators.TODAY_COUNTER).text
        return int(element_text.strip())

    def get_in_progress_orders(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.IN_PROGRESS_ORDERS)
        return self.driver.find_elements(*OrderPageFeedLocators.IN_PROGRESS_ORDERS)

    def get_create_order(self):
        main_page = MainPage(self.driver)
        main_page.add_ingredient_to_constructor("Краторная булка N-200i")
        main_page.add_ingredient_to_constructor("Соус Spicy-X")
        main_page.make_order()

    def get_orders(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_HISTORY_ITEM)
        return self.driver.find_elements(*OrderPageFeedLocators.ORDER_HISTORY_ITEM)

    def get_orders_from_feed(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_ITEM)
        return self.driver.find_elements(*OrderPageFeedLocators.ORDER_ITEM)
