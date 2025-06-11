from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from page_object.base_page import BasePage

class MainPage(BasePage):

    def go_to_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_TAB)

    def go_to_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED)

    def open_ingredient_modal(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        ingredients[index].click()


    def wait_all_ingredients_load(self):
        self.find_elements(MainPageLocators.INGREDIENT_ITEM)



    def add_ingredient_to_constructor(self, ingredient_name):
        self.wait_all_ingredients_load()

        ingredient = (
            By.XPATH,
            f'//p[text()="{ingredient_name}"]/ancestor::a[@draggable="true"]'
        )

        self.drag_and_drop_js(ingredient, MainPageLocators.ORDER_AREA)


    def get_ingredient_counter(self):
        try:
            return int(self.find_element(MainPageLocators.INGREDIENT_COUNTER).text)
        except:
            return 0


    def get_ingredient_counter_by_name(self, ingredient_name):
        try:
            locator = (
                By.XPATH,
                f'//p[text()="{ingredient_name}"]/ancestor::a//p[contains(@class, "counter_counter__num")]'
            )
            return int(self.find_element(locator).text)
        except:
            return 0

    def order_success_modal_visible(self):
        try:
            self.wait_for_element_to_be_visible(MainPageLocators.ORDER_SUCCESS)
            return True
        except TimeoutException:
            return False

    def make_order(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)


    def close_overlay(self):
        try:
            if self.is_element_visible(MainPageLocators.MODAL_CONTAINER):
                self.click_element(MainPageLocators.CLOSE_BUTTON_MODAL)
                self.wait_for_element_to_be_invisible(MainPageLocators.MODAL_CONTAINER)
        except TimeoutException:
            print("Модалка не появилась — ничего не закрываем")

    def close_modal(self):
        try:
            self.wait_for_order_ready()

            if self.is_element_visible(MainPageLocators.MODAL_CONTAINER):
                self.click_element(MainPageLocators.CLOSE_BUTTON_MODAL)
                self.wait_for_element_to_be_invisible(MainPageLocators.MODAL_CONTAINER)
                print("[DEBUG] Модалка успешно закрыта")
        except Exception as e:
            print(f"[WARN] Ошибка при закрытии модалки: {e}")


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