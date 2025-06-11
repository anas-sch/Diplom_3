from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator, scroll=False):
        self.wait_until_modal_overlay_disappears()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if scroll:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))


    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except Exception:
            return False


    def wait_for_element_to_be_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_url(self, partial_url):
        self.wait.until(EC.url_contains(partial_url))


    def wait_until_modal_overlay_disappears(self):
        overlay_locator = (By.XPATH,
                    '//*[contains(@class, "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]')
        try:
            self.wait.until(EC.invisibility_of_element_located(overlay_locator))
        except TimeoutException:
            print("⚠️ Модальное перекрытие не исчезло вовремя")

    def clear_and_send_keys(self, locator, text):
        element = self.wait_for_element_to_be_visible(locator)
        element.clear()
        element.send_keys(text)


    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        js_script = """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {dataTransfer, bubbles: true}));
            target.dispatchEvent(new DragEvent('drop', {dataTransfer, bubbles: true}));
            source.dispatchEvent(new DragEvent('dragend', {dataTransfer, bubbles: true}));
        """
        self.driver.execute_script(js_script, source, target)



    def is_element_clickable_wait(self, locator, timeout=10):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            f"Элемент {locator} не стал кликабельным за {timeout} секунд ожидания"
        )

    def try_close_modal_if_present(self, close_button_locator, modal_locator=None):
        try:
            self.wait_until_modal_overlay_disappears()
            close_button = self.is_element_clickable_wait(close_button_locator)
            close_button.click()
            if modal_locator:
                self.wait_for_element_to_be_invisible(modal_locator)
        except Exception as e:
            print(f"Не удалось закрыть модалку: {e}")