import allure

from locators.login_page_locators import LoginPageLocators
from page_object.base_page import BasePage

@allure.title("Методы для Login Page")
class LoginPage(BasePage):

    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        self.clear_and_send_keys(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.clear_and_send_keys(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Нажать кнопку входа")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Выполнить авторизацию (email: {email})")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Дождаться успешной авторизации")
    def wait_to_auth(self):
        self.wait_for_element_to_be_visible(LoginPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Перейти на страницу входа")
    def go_to_login_page(self):
        self.click_element(LoginPageLocators.GO_TO_ACCOUNT_BUTTON)