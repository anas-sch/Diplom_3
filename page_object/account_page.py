from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from locators.account_page_locators import AccountLocators
from page_object.base_page import BasePage

class AccountPage(BasePage):

    def go_to_account(self):
        account_button = self.wait.until(
            EC.element_to_be_clickable(AccountLocators.ACCOUNT_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", account_button)
        try:
            account_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", account_button)


    def go_to_order_history(self):
        order_button = self.wait.until(
            EC.element_to_be_clickable(AccountLocators.ORDER_HISTORY_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        try:
            order_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", order_button)


    def logout(self):
        logout_button = self.wait.until(
            EC.element_to_be_clickable(AccountLocators.LOGOUT_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logout_button)
        try:
            logout_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", logout_button)