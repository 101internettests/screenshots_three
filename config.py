import os
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))
host_stage = (os.getenv("HOST_STAGE"))
host_prod = (os.getenv("HOST_PROD"))

host_101 = (os.getenv("HOST_101"))
host_mol = (os.getenv("HOST_MOL"))
host_pol = (os.getenv("HOST_POL"))
# __prod_url = os.getenv('BASE_URL_PROD')
# __beta_url = os.getenv('BASE_URL_BETA')
# __beta_login = os.getenv('AUTH_LOGIN_BETA')
# __beta_password = os.getenv('AUTH_LOGIN_PASSWORD')


def who_calls():
    if os.getenv('CALL') == 'PC':
        return True
    if os.getenv('CALL') == 'GITLAB':
        return False


def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # if who_calls():
    #     driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    #     driver.maximize_window()
    #     auth_second_account(driver)
    # else:
    #     chrome_options.add_argument("--headless")
    #     chrome_options.add_argument("--hide-scrollbars")
    #     driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=chrome_options)
    #     driver.set_window_size(1920, 1080)
    #     driver.maximize_window()
    #     auth_second_account(driver)
    # return driver


def create_screenshot_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {"credentials_enable_service": False,
             "profile.password_manager_enabled": False}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    # driver.maximize_window()
    return driver

