from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

from locators.forgot_password_page_locators import ForgotPasswordLocators
from page_object.base_page import BasePage
from urls import FORGOT_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    def open_recovery_page(self):
        self.open_url(FORGOT_PASSWORD_URL)

    def enter_email(self, email):
        email_input = self.find_element(ForgotPasswordLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def toggle_password_visibility(self):
        self.click_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    def password_field_highlighted(self):
        return self.get_attribute(ForgotPasswordLocators.PASSWORD_FIELD, "type") == "text"

    def click_recover_password(self):
        recover_password_button = self.wait.until(
            EC.element_to_be_clickable(ForgotPasswordLocators.RECOVER_PASSWORD_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", recover_password_button)
        try:
            recover_password_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", recover_password_button)