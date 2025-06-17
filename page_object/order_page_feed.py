from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_feed_locators import OrderPageFeedLocators
from page_object.base_page import BasePage

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
        account_button = self.wait.until(
            EC.element_to_be_clickable(OrderPageFeedLocators.ACCOUNT_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", account_button)
        try:
            account_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", account_button)

    def go_to_order_history(self):
        history_button = self.wait.until(
            EC.element_to_be_clickable(OrderPageFeedLocators.ORDER_HISTORY_TAB))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", history_button)
        try:
            history_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", history_button)

    def get_completed_counter(self):
        element_text = self.find_element(OrderPageFeedLocators.COMPLETED_COUNTER).text
        return int(element_text.strip())

    def get_today_counter(self):
        element_text = self.find_element(OrderPageFeedLocators.TODAY_COUNTER).text
        return int(element_text.strip())

    def get_in_progress_orders(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.IN_PROGRESS_ORDERS)
        return self.driver.find_elements(*OrderPageFeedLocators.IN_PROGRESS_ORDERS)


    def get_orders(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_HISTORY_ITEM)
        return self.driver.find_elements(*OrderPageFeedLocators.ORDER_HISTORY_ITEM)

    def get_orders_from_feed(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_ITEM)
        return self.driver.find_elements(*OrderPageFeedLocators.ORDER_ITEM)


    def close_order_modal(self):
        self.wait_for_order_ready()
        return self.close_modal(
            container_locator=OrderPageFeedLocators.MODAL_CONTAINER,
            close_button_locator=OrderPageFeedLocators.CLOSE_BUTTON_MODAL
        )

    def wait_for_order_ready(self):
        try:
            self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_LOADER)
            print("[DEBUG] Лоадер появился — ждём его исчезновения")
        except TimeoutException:
            print("[DEBUG] Лоадер не появился — возможно, заказ уже отрендерен")

        try:
            self.wait_for_element_to_be_invisible(OrderPageFeedLocators.ORDER_LOADER)
            print("[DEBUG] Лоадер исчез — заказ готов")
        except TimeoutException:
            print("[WARN] Лоадер не исчез вовремя — заказ может быть не готов")



    def go_to_order_feed(self):
        feed_button = self.wait.until(
            EC.element_to_be_clickable(OrderPageFeedLocators.ORDER_FEED))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", feed_button)
        try:
            feed_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", feed_button)

    def go_to_constructor(self):
        self.click_element(OrderPageFeedLocators.CONSTRUCTOR_TAB)


    def get_create_order(self):
        self.add_ingredient_to_constructor("Краторная булка N-200i")
        self.add_ingredient_to_constructor("Соус Spicy-X")
        self.make_order()

    def add_ingredient_to_constructor(self, ingredient_name):
        self.wait_all_ingredients_load()

        ingredient = (
            By.XPATH,
            f'//p[text()="{ingredient_name}"]/ancestor::a[@draggable="true"]'
        )

        self.drag_and_drop_js(ingredient, OrderPageFeedLocators.ORDER_AREA)


    def make_order(self):
        try:
            order_button = self.wait.until(
                EC.element_to_be_clickable(OrderPageFeedLocators.PLACE_ORDER_BUTTON))

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});",
                order_button)

            try:
                order_button.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", order_button)

        except Exception as e:
            print(f"Ошибка при оформлении заказа: {e}")
            raise

    def wait_all_ingredients_load(self):
        self.find_elements(OrderPageFeedLocators.INGREDIENT_ITEM)
