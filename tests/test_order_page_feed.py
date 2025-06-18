import pytest
import allure


@allure.suite("Order Feed")
class TestOrderFeed:
    @allure.title("При клике на заказ открывается модалка с деталями")
    def test_open_order_details(self, order_page_feed):

        order_page_feed.get_create_order()
        order_page_feed.close_order_modal()
        order_page_feed.go_to_order_feed()

        order_page_feed.open_order_details(order_index=0)

        assert order_page_feed.order_modal_visible(), "Модальное окно с деталями заказа не открылось"

    @allure.title("История заказов отображается в ленте заказов")
    def test_orders_in_order_feed(self, order_page_feed):

        order_page_feed.get_create_order()
        order_page_feed.close_order_modal()
        order_page_feed.go_to_account()

        order_page_feed.go_to_order_history()

        orders = order_page_feed.get_orders()
        assert len(orders) > 0, "Заказы не отображаются в Ленте заказов"

    @allure.title("Счётчик выполненных заказов увеличивается")
    def test_completed_counter_increase(self, order_page_feed):

        order_page_feed.go_to_order_feed()
        initial_count = order_page_feed.get_completed_counter()

        order_page_feed.go_to_constructor()
        order_page_feed.get_create_order()
        order_page_feed.close_order_modal()


        order_page_feed.go_to_order_feed()
        new_count = order_page_feed.get_completed_counter()
        assert new_count > initial_count, f"Счётчик выполненных заказов не увеличился: {new_count} <= {initial_count}"

    @allure.title("Счётчик заказов за сегодня увеличивается")
    def test_today_counter_increase(self, order_page_feed):

        order_page_feed.go_to_order_feed()
        initial_count = order_page_feed.get_today_counter()

        order_page_feed.go_to_constructor()
        order_page_feed.get_create_order()
        order_page_feed.close_order_modal()


        order_page_feed.go_to_order_feed()
        new_count = order_page_feed.get_today_counter()
        assert new_count > initial_count, f"Счётчик заказов за сегодня не увеличился: {new_count} <= {initial_count}"

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_in_progress(self, order_page_feed):

        order_page_feed.get_create_order()
        order_page_feed.close_order_modal()

        order_page_feed.go_to_order_feed()

        in_progress_orders = order_page_feed.get_in_progress_orders()
        assert len(in_progress_orders) > 0, "Новый заказ не появился в разделе В работе"