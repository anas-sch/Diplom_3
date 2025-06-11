from locators.forgot_password_page_locators import ForgotPasswordLocators
from page_object.base_page import BasePage
from urls import FORGOT_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    def open_recovery_page(self):
        self.open_url(FORGOT_PASSWORD_URL)

    def enter_email(self, email):
        email_input = self.find_element(ForgotPasswordLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def click_recover_password(self):
        self.wait_until_modal_overlay_disappears()
        self.click_element(ForgotPasswordLocators.RECOVER_PASSWORD_BUTTON, scroll=True)

    def toggle_password_visibility(self):
        self.click_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    def password_field_highlighted(self):
        return self.get_attribute(ForgotPasswordLocators.PASSWORD_FIELD, "type") == "text"


    def test_toggle_password(self, forgot_password_page, test_email, reset_password_url):
        forgot_password_page.open_recovery_page()
        forgot_password_page.enter_email(test_email)
        forgot_password_page.click_recover_password()
        forgot_password_page.wait_for_url(reset_password_url)
        forgot_password_page.toggle_password_visibility()
        assert forgot_password_page.password_field_highlighted()