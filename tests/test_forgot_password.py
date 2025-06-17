import allure
import pytest

@allure.suite("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Открытие страницы восстановления пароля")
    def test_open_page_recovery_password(self, forgot_password_page):
        forgot_password_page.open_recovery_page()
        assert "forgot-password" in forgot_password_page.get_current_url()

    @allure.title("Ввод email и отправка запроса на восстановление")
    def test_email_enter_and_send_request_recovery(self, forgot_password_page):
        forgot_password_page.enter_email()

        forgot_password_page.click_recover_password()

        forgot_password_page.wait_for_url("reset-password")
        assert "reset-password" in forgot_password_page.get_current_url()

    @allure.title("Проверка переключения видимости пароля")
    def test_toggle_password_visibility(self, forgot_password_page):

        forgot_password_page.open_recovery_page()
        forgot_password_page.enter_email()

        forgot_password_page.click_recover_password()
        forgot_password_page.wait_for_url("reset-password")

        forgot_password_page.toggle_password_visibility()
        assert forgot_password_page.password_field_highlighted(), "Пароль должен отображаться после переключения"