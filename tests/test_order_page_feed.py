import pytest
import allure
from page_object.order_page_feed import OrderPageFeed


@allure.suite("Order Feed")
class TestOrderFeed:
    @allure.title("При клике на заказ открывается модалка с деталями")
    def test_open_order_details(self, main_page, driver):
        page = OrderPageFeed(driver)

        page.get_create_order()
        main_page.close_modal()
        main_page.close_overlay()
        main_page.go_to_order_feed()

        page.open_order_details(order_index=0)

        assert page.order_modal_visible(), "Модальное окно с деталями заказа не открылось"

    @allure.title("История заказов отображается в ленте заказов")
    def test_orders_in_order_feed(self, main_page, driver):
        page = OrderPageFeed(driver)

        page.get_create_order()
        main_page.close_modal()
        main_page.close_overlay()

        page.go_to_account()
        main_page.close_modal()
        main_page.close_overlay()
        page.go_to_order_history()

        orders = page.get_orders()
        assert len(orders) > 0, "Заказы не отображаются в Ленте заказов"

    @allure.title("Счётчик выполненных заказов увеличивается")
    def test_completed_counter_increase(self, main_page, driver):
        page = OrderPageFeed(driver)

        main_page.go_to_order_feed()
        initial_count = page.get_completed_counter()

        main_page.go_to_constructor()
        page.get_create_order()
        main_page.close_modal()
        main_page.close_overlay()

        main_page.go_to_order_feed()
        new_count = page.get_completed_counter()
        assert new_count > initial_count, f"Счётчик выполненных заказов не увеличился: {new_count} <= {initial_count}"

    @allure.title("Счётчик заказов за сегодня увеличивается")
    def test_today_counter_increase(self, main_page, driver):
        page = OrderPageFeed(driver)

        main_page.go_to_order_feed()
        initial_count = page.get_today_counter()

        main_page.go_to_constructor()
        page.get_create_order()
        main_page.close_modal()
        main_page.close_overlay()

        main_page.go_to_order_feed()
        new_count = page.get_today_counter()
        assert new_count > initial_count, f"Счётчик заказов за сегодня не увеличился: {new_count} <= {initial_count}"

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_in_progress(self, main_page, driver):
        page = OrderPageFeed(driver)

        page.get_create_order()
        main_page.close_modal()
        main_page.close_overlay()

        main_page.go_to_order_feed()

        in_progress_orders = page.get_in_progress_orders()
        assert len(in_progress_orders) > 0, "Новый заказ не появился в разделе В работе"
