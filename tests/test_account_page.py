import pytest
import allure

@allure.suite("Личный кабинет")
@pytest.mark.usefixtures("driver", "create_user")
class TestAccount:
    @allure.title("Переход в Личный кабинет")
    def test_go_to_account(self, account_page):
        account_page.go_to_account()
        account_page.wait_for_url("account")
        assert "account" in account_page.get_current_url()

    @allure.title("Переход в Историю заказов")
    def test_go_to_order_history(self, account_page):
        account_page.go_to_account()

        account_page.go_to_order_history()
        assert "order-history" in account_page.get_current_url()

    @allure.title("Выход из аккаунта")
    def test_logout(self, account_page):
        account_page.go_to_account()
        account_page.logout()
        account_page.wait_for_url("login")
        assert "login" in account_page.get_current_url()