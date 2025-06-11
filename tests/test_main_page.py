import pytest
import allure
from page_object.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL, FORGOT_PASSWORD_URL


@allure.suite("Main Page")
class TestMainPage:
    @allure.title("Переход по клику на «Конструктор»")
    def test_navigation_to_constructor(self, driver):
        driver.get(FORGOT_PASSWORD_URL)
        page = MainPage(driver)

        page.go_to_constructor()
        current_url = driver.current_url.rstrip("/")
        expected_url = BASE_URL.rstrip("/")
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, но был: {current_url}"

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigation_to_order_feed(self, driver):
        driver.get(BASE_URL)
        page = MainPage(driver)

        page.go_to_order_feed()
        assert "feed" in driver.current_url, "Не удалось перейти на страницу ленты заказов"

    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_ingredient_modal_open_close(self, driver):
        driver.get(BASE_URL)
        page = MainPage(driver)

        page.open_ingredient_modal()
        assert page.is_element_visible(MainPageLocators.MODAL_CONTAINER), "Модальное окно не появилось"
        page.close_overlay()
        assert not page.is_element_visible(MainPageLocators.MODAL_CONTAINER), "Модальное окно не закрылось"

    @allure.title("Добавление ингредиента в заказ и проверка счётчика")
    def test_add_ingredient_to_order(self, driver):
        driver.get(BASE_URL)
        page = MainPage(driver)
        page.close_overlay()

        ingredient_name = "Краторная булка N-200i"
        initial_count = page.get_ingredient_counter_by_name(ingredient_name)
        page.add_ingredient_to_constructor(ingredient_name)
        final_count = page.get_ingredient_counter_by_name(ingredient_name)
        assert final_count > initial_count, f"Счётчик не увеличился: {initial_count} → {final_count}"

    @allure.title("Оформление заказа залогиненным пользователем")
    def test_place_order_logged_in(self, main_page):
        main_page.close_overlay()
        main_page.add_ingredient_to_constructor("Краторная булка N-200i")
        main_page.add_ingredient_to_constructor("Соус Spicy-X")
        main_page.make_order()
        assert main_page.order_success_modal_visible(), "Модальное окно успешного заказа не появилось"