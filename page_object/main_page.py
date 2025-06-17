from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from page_object.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    def go_to_constructor(self):
        constructor_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_TAB))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", constructor_button)
        try:
            constructor_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", constructor_button)



    def go_to_order_feed(self):
        feed_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_FEED))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", feed_button)
        try:
            feed_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", feed_button)

    def open_ingredient_modal(self, index=0):
        self.close_main_modal()
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
        try:
            self.close_main_modal()

            order_button = self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.PLACE_ORDER_BUTTON))

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



    def close_main_modal(self):
        self.wait_for_order_ready()
        return self.close_modal_if_visible(
            modal_locator=MainPageLocators.MODAL_CONTAINER,
            close_button_locator=MainPageLocators.CLOSE_BUTTON_MODAL
        )
