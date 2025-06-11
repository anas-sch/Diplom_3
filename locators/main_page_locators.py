from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//a[@href='/']")
    ORDER_FEED = (By.XPATH, "//a[@href='/feed']")
    ORDER_SUCCESS = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    ORDER_AREA = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")
    INGREDIENT_ITEM = (By.CLASS_NAME, "BurgerIngredient_ingredient__text__yp3dH")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")
    MODAL_CONTAINER = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
    MODAL = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    CLOSE_BUTTON_MODAL = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]/..")
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]/..")
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]/..")
    ORDER_LOADER = (By.XPATH, "//img[@alt='loading']")
