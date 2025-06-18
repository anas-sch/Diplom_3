import allure
from selenium.common import TimeoutException

from locators.order_page_feed_locators import OrderPageFeedLocators
from page_object.base_page import BasePage

@allure.title("Методы для Order Feed Page")
class OrderPageFeed(BasePage):

    @allure.step("Открыть детали заказа по индексу {order_index}")
    def open_order_details(self, order_index=0):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_ITEM)
        orders = self.driver.find_elements(*OrderPageFeedLocators.ORDER_ITEM)
        if not orders:
            raise ValueError("Заказы не найдены")
        orders[order_index].click()

    @allure.step("Проверить видимость модального окна заказа")
    def order_modal_visible(self):
        return self.is_element_visible(OrderPageFeedLocators.ORDER_MODAL)

    @allure.step("Перейти в аккаунт")
    def go_to_account(self):
        self.click_with_scroll_to_center(OrderPageFeedLocators.ACCOUNT_BUTTON)

    @allure.step("Перейти в историю заказов")
    def go_to_order_history(self):
        self.click_with_scroll_to_center(OrderPageFeedLocators.ORDER_HISTORY_TAB)

    @allure.step("Получить счетчик выполненных заказов")
    def get_completed_counter(self):
        element_text = self.find_element(OrderPageFeedLocators.COMPLETED_COUNTER).text
        return int(element_text.strip())

    @allure.step("Получить счетчик заказов за сегодня")
    def get_today_counter(self):
        element_text = self.find_element(OrderPageFeedLocators.TODAY_COUNTER).text
        return int(element_text.strip())

    @allure.step("Получить список заказов в процессе выполнения")
    def get_in_progress_orders(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.IN_PROGRESS_ORDERS)
        return self.driver.find_elements(*OrderPageFeedLocators.IN_PROGRESS_ORDERS)

    @allure.step("Получить список заказов из истории")
    def get_orders(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_HISTORY_ITEM)
        return self.driver.find_elements(*OrderPageFeedLocators.ORDER_HISTORY_ITEM)

    @allure.step("Получить список заказов из ленты")
    def get_orders_from_feed(self):
        self.wait_for_element_to_be_visible(OrderPageFeedLocators.ORDER_ITEM)
        return self.driver.find_elements(*OrderPageFeedLocators.ORDER_ITEM)


    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.wait_for_order_ready()
        self.close_modal_if_visible(
            modal_locator=OrderPageFeedLocators.MODAL_CONTAINER,
            close_button_locator=OrderPageFeedLocators.CLOSE_BUTTON_MODAL)


    @allure.step("Ожидание готовности заказа")
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


    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click_with_scroll_to_center(OrderPageFeedLocators.ORDER_FEED)

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click_element(OrderPageFeedLocators.CONSTRUCTOR_TAB)

    @allure.step("Создать заказ")
    def get_create_order(self):
        self.add_ingredient_to_constructor("Краторная булка N-200i")
        self.add_ingredient_to_constructor("Соус Spicy-X")
        self.make_order()

    @allure.step("Добавить ингредиент '{ingredient_name}' в конструктор")
    def add_ingredient_to_constructor(self, ingredient_name):
        self.wait_all_ingredients_load()
        ingredient_xpath = OrderPageFeedLocators.INGREDIENT_ITEM_BY_NAME[1].format(ingredient_name)
        ingredient_locator = (OrderPageFeedLocators.INGREDIENT_ITEM_BY_NAME[0], ingredient_xpath)
        self.drag_and_drop_js(ingredient_locator, OrderPageFeedLocators.ORDER_AREA)

    @allure.step("Оформить заказ")
    def make_order(self):
        self.click_with_scroll_to_center(OrderPageFeedLocators.PLACE_ORDER_BUTTON)

    @allure.step("Ожидание загрузки всех ингредиентов")
    def wait_all_ingredients_load(self):
        self.find_elements(OrderPageFeedLocators.INGREDIENT_ITEM)
