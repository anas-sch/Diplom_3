import allure
from selenium.common import TimeoutException
import urls
from locators.main_page_locators import MainPageLocators
from page_object.base_page import BasePage

@allure.title("Методы для Main Page")
class MainPage(BasePage):

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click_with_scroll_to_center(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click_with_scroll_to_center(MainPageLocators.ORDER_FEED)

    @allure.step("Открыть модальное окно ингредиента (индекс: {index})")
    def open_ingredient_modal(self, index=0):
        self.close_main_modal()
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        ingredients[index].click()

    @allure.step("Ожидание загрузки ингредиентов")
    def wait_all_ingredients_load(self):
        self.find_elements(MainPageLocators.INGREDIENT_ITEM)

    @allure.step("Добавить ингредиент в конструктор: {ingredient_name}")
    def add_ingredient_to_constructor(self, ingredient_name):
        self.wait_all_ingredients_load()
        ingredient_xpath = MainPageLocators.INGREDIENT_ITEM_BY_NAME[1].format(ingredient_name)
        ingredient_locator = (MainPageLocators.INGREDIENT_ITEM_BY_NAME[0], ingredient_xpath)
        self.drag_and_drop_js(ingredient_locator, MainPageLocators.ORDER_AREA)

    @allure.step("Получить счетчик для ингредиента: {ingredient_name}")
    def get_ingredient_counter_by_name(self, ingredient_name):
        try:
            xpath = MainPageLocators.INGREDIENT_COUNTER_BY_NAME[1].format(ingredient_name)
            locator = (MainPageLocators.INGREDIENT_COUNTER_BY_NAME[0], xpath)
            return int(self.find_element(locator).text)
        except:
            return 0

    @allure.step("Проверить видимость модального окна успешного заказа")
    def order_success_modal_visible(self):
        try:
            self.wait_for_element_to_be_visible(MainPageLocators.ORDER_SUCCESS)
            return True
        except TimeoutException:
            return False

    @allure.step("Оформить заказ")
    def make_order(self):
        self.click_with_scroll_to_center(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Дождаться готовности заказа")
    def wait_for_order_ready(self):
        try:
            self.wait_for_element_to_be_visible(MainPageLocators.ORDER_LOADER)
            print("[DEBUG] Лоадер появился — ждём его исчезновения")
        except TimeoutException:
            print("[DEBUG] Лоадер не появился — возможно, заказ уже отрендерен")

        try:
            self.wait_for_element_to_be_invisible(MainPageLocators.ORDER_LOADER)
            print("[DEBUG] Лоадер исчез — заказ готов")
        except TimeoutException:
            print("[WARN] Лоадер не исчез вовремя — заказ может быть не готов")

    @allure.step("Закрыть модальное окно")
    def close_main_modal(self):
        self.wait_for_order_ready()
        self.close_modal_if_visible(
            modal_locator=MainPageLocators.MODAL_CONTAINER,
            close_button_locator=MainPageLocators.CLOSE_BUTTON_MODAL
        )

    @allure.step("Проверка, что модальное окно ингредиента открыто")
    def is_ingredient_modal_visible(self) -> bool:
        return self.is_element_visible(MainPageLocators.MODAL_CONTAINER)

    @allure.step("Проверка, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_closed(self) -> bool:
        return not self.is_element_visible(MainPageLocators.MODAL_CONTAINER)

    @allure.step("Открытие страницы")
    def open_url_base(self):
        self.driver.get(urls.BASE_URL)

    @allure.step("Получение базовой страницы")
    def get_base_url(self):
        return urls.BASE_URL.rstrip("/")