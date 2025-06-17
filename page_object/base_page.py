from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator, scroll=False, wait_overlay=False, overlay_locator=False):
        if overlay_locator and wait_overlay:
            self.wait_until_modal_overlay_disappears(overlay_locator)
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


    def wait_until_modal_overlay_disappears(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
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


    def close_modal_if_visible(self, modal_locator=None, close_button_locator=None):
        try:
            # Проверяем, видно ли модальное окно
            if self.is_element_visible(modal_locator):

                close_button = self.wait_for_element_to_be_visible(close_button_locator)
                self.driver.execute_script("arguments[0].click();", close_button)

                # Ждем исчезновения модального окна
                self.wait_for_element_to_be_invisible(modal_locator)
        except Exception as e:
            print(f"⚠️ Ошибка при закрытии модального окна: {e}")



    def get_current_url(self):
        return self.driver.current_url

    def close_modal(self, container_locator, close_button_locator=None,
                    overlay_locator=None, timeout=5):
        try:
            if not self.is_element_visible(container_locator):
                return True

            if close_button_locator:
                self.click_element(close_button_locator)
            elif overlay_locator:
                self.click_element(overlay_locator)
            else:
                raise ValueError("Должен быть указан close_button_locator или overlay_locator")

            return self.wait_for_element_to_be_invisible(container_locator, timeout)

        except Exception as e:
            print(f"[WARN] Ошибка закрытия модалки: {str(e)}")
            return False
            self.wait_for_element_to_be_invisible(container_locator)
            return True

        except TimeoutException:
            print(f"[WARN] Таймаут при закрытии модалки (локатор: {container_locator})")
            return False
        except Exception as e:
            print(f"[WARN] Не удалось закрыть модалку: {str(e)}")
            return False