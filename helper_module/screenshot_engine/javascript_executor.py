from selenium.common import JavascriptException


def remove_marker(driver):
    try:
        driver.execute_script(
            'return document.getElementsByClassName("header_auth-cell js-header-notifications")[0].remove();')
        driver.execute_script('return document.getElementsByClassName("create-marker-from")[0].remove();')
        driver.execute_script('return document.getElementsByClassName("create-marker-from-shadow")[0].remove();')
    except JavascriptException:
        pass


def remove_car(driver):
    try:
        driver.execute_script('return document.getElementsByClassName("create-car-decor")[0].remove();')
    except JavascriptException:
        pass


def remove_road(driver):
    try:
        driver.execute_script('return document.getElementsByClassName("road")[0].remove();')
    except JavascriptException:
        pass


def remove_line(driver):
    try:
        driver.execute_script(
            'return document.getElementsByClassName("create_variation-decorate create_variation-decorate_vertical")[0].remove();')
    except JavascriptException:
        pass


def remove_problem_elements(driver):
    remove_marker(driver)
    remove_car(driver)
    remove_road(driver)
    remove_line(driver)


def remove_notification_bell(driver):
    try:
        driver.execute_script(
            'return document.getElementsByClassName("header_auth-cell js-header-notifications")[0].remove();')
    except JavascriptException:
        pass


def remove_margin_xl(driver):
    try:
        driver.execute_script('return document.getElementsByClassName("margin-xl")[0].remove();')
    except JavascriptException:
        pass


def remove_history_calendar(driver):
    try:
        driver.execute_script('return document.getElementsByClassName("js-search-history-container")[0].remove();')
    except JavascriptException:
        pass


def remove_problem_elements_main_page(driver):
    try:
        driver.execute_script(
            'return document.getElementsByClassName("header_auth-cell js-header-notifications")[0].remove();')
        driver.execute_script('return document.getElementsByClassName("event-wrapper")[0].remove();')
        driver.execute_script('return document.getElementsByClassName("popular")[0].remove();')
    except JavascriptException:
        pass


def remove_problem_elements_stations(driver):
    try:
        driver.execute_script('return document.getElementsByClassName("main-popular-stations")[0].remove();')
        driver.execute_script('return document.getElementsByClassName("main-popular-schedule")[0].remove();')
    except JavascriptException:
        pass


def remove_event_wrapper(driver):
    try:
        driver.execute_script('return document.getElementsByClassName("event-wrapper")[0].remove();')
    except JavascriptException:
        pass


def remove_subscription_info(driver):
    try:
        driver.execute_script('return document.getElementsByClassName("margin-lg")[0].remove();')
    except JavascriptException:
        pass


def remove_problem_screenshot_elements(driver):
    remove_notification_bell(driver)
    remove_margin_xl(driver)