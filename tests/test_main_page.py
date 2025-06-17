import pytest
import allure


@allure.suite("Main Page")
class TestMainPage:
    @allure.title("Переход по клику на «Конструктор»")
    def test_navigation_to_constructor(self,  main_page):
        main_page.go_to_order_feed()
        main_page.go_to_constructor()
        current_url = main_page.get_current_url().rstrip("/")
        expected_url = main_page.get_base_url()
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, но был: {current_url}"


    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigation_to_order_feed(self, driver, main_page):
        main_page.open_url_base()

        main_page.go_to_order_feed()
        assert "feed" in main_page.get_current_url().rstrip("/"), "Не удалось перейти на страницу ленты заказов"

    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_ingredient_modal_open_close(self, driver, main_page):
        main_page.open_url_base()

        main_page.open_ingredient_modal()
        assert main_page.is_ingredient_modal_visible(), "Модальное окно не появилось"
        main_page.close_main_modal()
        assert main_page.is_ingredient_modal_closed(), "Модальное окно не закрылось"

    @allure.title("Добавление ингредиента в заказ и проверка счётчика")
    def test_add_ingredient_to_order(self, driver, main_page):
        main_page.open_url_base()

        ingredient_name = "Краторная булка N-200i"
        initial_count = main_page.get_ingredient_counter_by_name(ingredient_name)
        main_page.add_ingredient_to_constructor(ingredient_name)
        final_count = main_page.get_ingredient_counter_by_name(ingredient_name)
        assert final_count > initial_count, f"Счётчик не увеличился: {initial_count} → {final_count}"

    @allure.title("Оформление заказа залогиненным пользователем")
    def test_place_order_logged_in(self, main_page):
        main_page.close_main_modal()
        main_page.add_ingredient_to_constructor("Краторная булка N-200i")
        main_page.add_ingredient_to_constructor("Соус Spicy-X")
        main_page.make_order()
        assert main_page.order_success_modal_visible(), "Модальное окно успешного заказа не появилось"