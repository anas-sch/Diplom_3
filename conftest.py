import pytest
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from page_object.main_page import MainPage
from page_object.login_page import LoginPage
from page_object.account_page import AccountPage
from page_object.forgot_password_page import ForgotPasswordPage
from page_object.order_page_feed import OrderPageFeed
from urls import BASE_URL, API_BASE_URL



@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Неизвестный браузер: {request.param}")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def test_email():
    timestamp = int(time.time())
    return f"test_{timestamp}@example.com"

@pytest.fixture
def forgot_password_page(driver):
    forgot_password_page = ForgotPasswordPage(driver)
    driver.get(BASE_URL)
    forgot_password_page.open_recovery_page()
    return forgot_password_page

@pytest.fixture
def login_user(driver, create_user):
    user_data, _ = create_user
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(user_data["email"], user_data["password"])
    return driver

@pytest.fixture
def account_page(login_user):
    return AccountPage(login_user)

@pytest.fixture
def main_page(login_user):
    return MainPage(login_user)

@pytest.fixture
def order_page_feed(login_user):
    return OrderPageFeed(login_user)


@pytest.fixture
def reset_password_url():
    return "reset-password"

TEST_USER_DATA = {
    "email": f"usertest_{int(time.time())}@examlpe.com",
    "password": "pass12345",
    "name": "Test_user"
}

@pytest.fixture
def create_user():
    user_data = TEST_USER_DATA.copy()
    try:
        response = requests.post(f"{API_BASE_URL}/auth/register", json=user_data)
        if response.status_code == 403:
            print("Такой пользователь уже существует")
            login_response = requests.post(f"{API_BASE_URL}/auth/login",
                                           json={
                                               "email": user_data["email"],
                                               "password": user_data["password"]
                                           })

            login_response.raise_for_status()
            access_token = login_response.json().get("accessToken")

        else:
            response.raise_for_status()
            access_token = response.json().get("accessToken")

        if not access_token:
            raise ValueError("Не удалось получить токен")

        yield user_data, access_token

    finally:
        if 'access_token' in locals() and access_token:
            headers = {"Authorization": f"Bearer {access_token}"}
            delete_response = requests.delete(f"{API_BASE_URL}/auth/user", headers=headers)
            if delete_response.status_code != 202:
                print("Не удалось удалить пользователя")


