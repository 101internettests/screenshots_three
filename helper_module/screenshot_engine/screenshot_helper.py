import allure
from helper_module.screenshot_engine.javascript_executor import *
from helper_module.screenshot_engine.image_processor import ImageProcessor
from time import sleep


class ScreenshotHelper(ImageProcessor):
    DEFAULT_WIDTH = 1920
    DEFAULT_HEIGHT = 1080

    def check_by_screenshot(self, driver, extra_driver):
        sleep(0.5)
        remove_problem_elements(driver)
        page_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(self.DEFAULT_WIDTH, page_height)
        sleep(1)
        screenshot_driver_bytes = driver.get_screenshot_as_png()

        remove_problem_elements(extra_driver)
        extra_driver.set_window_size(self.DEFAULT_WIDTH, page_height)
        sleep(1)
        screenshot_extra_driver_bytes = extra_driver.get_screenshot_as_png()

        # image_prod = self.load_image_from_bytes(screenshot_driver_bytes)
        # image_beta = self.load_image_from_bytes(screenshot_extra_driver_bytes)
        # get_result = self.check_images_difference(image_prod, image_beta)

        image_101 = self.load_image_from_bytes(screenshot_driver_bytes)
        image_mol = self.load_image_from_bytes(screenshot_extra_driver_bytes)
        image_pol = self.load_image_from_bytes(screenshot_extra_driver_bytes)
        get_result = self.check_images_difference(image_101, image_mol, image_pol)
        image_result = self.load_image_from_bytes(get_result[1])

        try:
            assert get_result[0] == 0
        except AssertionError:
            # allure.attach(self.image_to_bytes(image_prod), 'prod', allure.attachment_type.PNG)
            # allure.attach(self.image_to_bytes(image_beta), 'stage', allure.attachment_type.PNG)
            allure.attach(self.image_to_bytes(image_101), 'stage', allure.attachment_type.PNG)
            allure.attach(self.image_to_bytes(image_mol), 'stage', allure.attachment_type.PNG)
            allure.attach(self.image_to_bytes(image_pol), 'stage', allure.attachment_type.PNG)
            allure.attach(self.image_to_bytes(image_result), 'diff', allure.attachment_type.PNG)

        return get_result[0]
