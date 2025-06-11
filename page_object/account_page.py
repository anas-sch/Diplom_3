from locators.account_page_locators import AccountLocators
from page_object.base_page import BasePage

class AccountPage(BasePage):
    def go_to_account(self):
        self.click_element(AccountLocators.ACCOUNT_BUTTON)

    def go_to_order_history(self):
        self.click_element(AccountLocators.ORDER_HISTORY_BUTTON)

    def logout(self):
        self.click_element(AccountLocators.LOGOUT_BUTTON)