from selenium.webdriver.common.by import By

class OrderPageFeedLocators:
    ORDER_MODAL = (By.CLASS_NAME, "Modal_orderBox__1xWdi")
    ORDER_ITEM = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
    ORDER_HISTORY_TAB = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    ORDER_HISTORY_ITEM = (By.CLASS_NAME, "OrderHistory_orderHistory__qy1VB")
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
    COMPLETED_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_ORDERS = (By.CLASS_NAME, "OrderFeed_orderListReady__1YFem")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_AREA = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")
    CONSTRUCTOR_TAB = (By.XPATH, "//a[@href='/']")
    ORDER_FEED = (By.XPATH, "//a[@href='/feed']")
    ORDER_LOADER = (By.XPATH, "//img[@alt='loading']")
    INGREDIENT_ITEM = (By.CLASS_NAME, "BurgerIngredient_ingredient__text__yp3dH")

    MODAL_CONTAINER = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    CLOSE_BUTTON_MODAL = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")

    INGREDIENT_ITEM_BY_NAME = (By.XPATH, '//p[text()="{}"]/ancestor::a[@draggable="true"]')
    INGREDIENT_COUNTER_BY_NAME = (
        By.XPATH,
        '//p[text()="{}"]/ancestor::a//p[contains(@class, "counter_counter__num")]')