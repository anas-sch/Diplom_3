import allure
from locators.account_page_locators import AccountLocators
from page_object.base_page import BasePage

@allure.title("Методы для Account Page")
class AccountPage(BasePage):

    @allure.step("Перейти в личный кабинет")
    def go_to_account(self):
        self.click_with_scroll_to_center(AccountLocators.ACCOUNT_BUTTON)

    @allure.step("Перейти в историю заказов")
    def go_to_order_history(self):
        self.click_with_scroll_to_center(AccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click_with_scroll_to_center(AccountLocators.LOGOUT_BUTTON)