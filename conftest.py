import pytest
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import who_calls
from config import bot, chat_id


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Проверка связи, скриншотные тесты! Смотри здесь https://101internettests.github.io/screenshot_tests/ ")


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        options=chrome_options,
        service=Service(ChromeDriverManager().install())
    )
    # .maximize_window()
    # auth(driver)

    yield driver
    driver.quit()
#
#
# @pytest.fixture()
# def admin_driver():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     }
#     chrome_options.add_experimental_option("prefs", prefs)
#     if who_calls():
#         driver = webdriver.Chrome(
#             options=chrome_options,
#             service=Service(ChromeDriverManager().install())
#         )
#         driver.maximize_window()
#         auth_admin(driver)
#     else:
#         current_test = "driver:" + os.getenv("PYTEST_CURRENT_TEST").replace('(setup)', '')
#         if "screenshot" in current_test:
#             chrome_options.add_argument("--headless")
#         if os.getenv('VNC_ENABLE') == "True":
#             vnc_enable = True
#         else:
#             vnc_enable = False
#         chrome_options.set_capability("selenoid:options", {
#                 "enableVNC": vnc_enable,
#         })
#         chrome_options.add_argument("--hide-scrollbars")
#         chrome_options.set_capability("browserName", "chrome")
#         chrome_options.set_capability("browserVersion", "115.0")
#
#         driver = webdriver.Remote(
#             command_executor='http://127.0.0.1:4444/wd/hub',
#             options=chrome_options
#         )
#         driver.set_window_size(1920, 1080)
#         driver.maximize_window()
#         auth_admin(driver)
#     yield driver
#
#
# @pytest.fixture()
# def extra_driver_beta():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     }
#     chrome_options.add_experimental_option("prefs", prefs)
#     if who_calls():
#         driver = webdriver.Chrome(
#             options=chrome_options,
#             service=Service(ChromeDriverManager().install())
#         )
#         driver.maximize_window()
#         auth_second_account(driver)
#     else:
#         current_test = "extra_driver:" + os.getenv("PYTEST_CURRENT_TEST").replace('(setup)', '')
#         if os.getenv('VNC_ENABLE') == "True":
#             vnc_enable = True
#         else:
#             vnc_enable = False
#         chrome_options.set_capability("selenoid:options", {
#                 "enableVNC": vnc_enable,
#         })
#         chrome_options.add_argument("--hide-scrollbars")
#         chrome_options.set_capability("browserName", "chrome")
#         chrome_options.set_capability("browserVersion", "115.0")
#         driver = webdriver.Remote(
#             command_executor='http://127.0.0.1:4444/wd/hub',
#             options=chrome_options
#         )
#         driver.set_window_size(1920, 1080)
#         driver.maximize_window()
#         auth_second_account(driver)
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture()
# def extra_driver():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     }
#     chrome_options.add_experimental_option("prefs", prefs)
#     if who_calls():
#         driver = webdriver.Chrome(
#             options=chrome_options,
#             service=Service(ChromeDriverManager().install())
#         )
#         driver.maximize_window()
#         auth_screenshot_account(driver)
#     else:
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--hide-scrollbars")
#         driver = webdriver.Remote(
#             command_executor='http://127.0.0.1:4444/wd/hub',
#             options=chrome_options
#         )
#         driver.set_window_size(1920, 1080)
#         driver.maximize_window()
#         auth_screenshot_account(driver)
#     yield driver
#     driver.quit()



