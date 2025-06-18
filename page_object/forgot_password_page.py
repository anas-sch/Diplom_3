import allure
import urls
from helpers import generate_unique_email
from locators.forgot_password_page_locators import ForgotPasswordLocators
from page_object.base_page import BasePage


@allure.title("Методы для Forgot Password Page")
class ForgotPasswordPage(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open_recovery_page(self):
        self.driver.get(urls.FORGOT_PASSWORD_URL)

    @allure.step("Ввести email для восстановления")
    def enter_email(self):
        email = generate_unique_email()
        email_input = self.find_element(ForgotPasswordLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    @allure.step("Переключить видимость пароля")
    def toggle_password_visibility(self):
        self.click_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверить подсветку поля пароля")
    def password_field_highlighted(self):
        return self.get_attribute(ForgotPasswordLocators.PASSWORD_FIELD, "type") == "text"

    @allure.step("Нажать кнопку восстановления пароля")
    def click_recover_password(self):
        self.click_with_scroll_to_center(ForgotPasswordLocators.RECOVER_PASSWORD_BUTTON)


