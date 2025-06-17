from locators.login_page_locators import LoginPageLocators
from page_object.base_page import BasePage

class LoginPage(BasePage):

    def enter_email(self, email):
        self.clear_and_send_keys(LoginPageLocators.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.clear_and_send_keys(LoginPageLocators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def wait_to_auth(self):
        self.wait_for_element_to_be_visible(LoginPageLocators.PLACE_ORDER_BUTTON)

    def go_to_login_page(self):
        self.click_element(LoginPageLocators.GO_TO_ACCOUNT_BUTTON)