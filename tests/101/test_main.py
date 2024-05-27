import allure
from selenium import webdriver
from helper_module.screenshot_engine.image_processor import ImageProcessor
from config import create_screenshot_driver
from config import host_prod, host_stage
from config import host_101, host_mol, host_pol


class TestSomePage(ImageProcessor):

    WINDOW_H = 1280
    WINDOW_W = 4500

    @allure.title("Сравнение первой страницы")
    def test_mainpage(self, driver: webdriver.Chrome):
        path = '/'
        driver.get(host_101 + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        second_driver = create_screenshot_driver()
        second_driver.get(host_pol + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        third_driver = create_screenshot_driver()
        third_driver.get(host_mol + path)
        third_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        screenshot_101_bytes = driver.get_screenshot_as_png()
        screenshot_pol_bytes = second_driver.get_screenshot_as_png()
        screenshot_mol_bytes = third_driver.get_screenshot_as_png()

        image_101 = self.load_image_from_bytes(screenshot_101_bytes)
        image_pol = self.load_image_from_bytes(screenshot_pol_bytes)
        image_mol = self.load_image_from_bytes(screenshot_mol_bytes)

        get_result = self.check_images_difference(image_101, image_mol, image_pol)
        image_result = self.load_image_from_bytes(get_result[1])
        image_mol.show()
        image_101.show()
        image_pol.show()
        image_result.show()

    @allure.title("Сравнение страницы 'поиск по адресу'")
    def test_orders_tohome(self, driver: webdriver.Chrome):
            path = '/orders/tohome'
            driver.get(host_101 + path)
            driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

            second_driver = create_screenshot_driver()
            second_driver.get(host_pol + path)
            second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

            third_driver = create_screenshot_driver()
            third_driver.get(host_mol + path)
            third_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

            screenshot_101_bytes = driver.get_screenshot_as_png()
            screenshot_pol_bytes = second_driver.get_screenshot_as_png()
            screenshot_mol_bytes = third_driver.get_screenshot_as_png()

            image_101 = self.load_image_from_bytes(screenshot_101_bytes)
            image_pol = self.load_image_from_bytes(screenshot_pol_bytes)
            image_mol = self.load_image_from_bytes(screenshot_mol_bytes)

            get_result = self.check_images_difference(image_101, image_mol, image_pol)
            image_result = self.load_image_from_bytes(get_result[1])
            image_mol.show()
            image_101.show()
            image_pol.show()
            image_result.show()

    @allure.title("Сравнение страницы 'провайдеры'")
    def test_providers(self, driver: webdriver.Chrome):
        path = '/providers'
        driver.get(host_101 + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        second_driver = create_screenshot_driver()
        second_driver.get(host_pol + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        third_driver = create_screenshot_driver()
        third_driver.get(host_mol + path)
        third_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        screenshot_101_bytes = driver.get_screenshot_as_png()
        screenshot_pol_bytes = second_driver.get_screenshot_as_png()
        screenshot_mol_bytes = third_driver.get_screenshot_as_png()

        image_101 = self.load_image_from_bytes(screenshot_101_bytes)
        image_pol = self.load_image_from_bytes(screenshot_pol_bytes)
        image_mol = self.load_image_from_bytes(screenshot_mol_bytes)

        get_result = self.check_images_difference(image_101, image_mol, image_pol)
        image_result = self.load_image_from_bytes(get_result[1])
        image_mol.show()
        image_101.show()
        image_pol.show()
        image_result.show()

    @allure.title("Сравнение страницы 'рейтинг'")
    def test_rating(self, driver: webdriver.Chrome):
        path = '/rating'
        driver.get(host_101 + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        second_driver = create_screenshot_driver()
        second_driver.get(host_pol + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        third_driver = create_screenshot_driver()
        third_driver.get(host_mol + path)
        third_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        screenshot_101_bytes = driver.get_screenshot_as_png()
        screenshot_pol_bytes = second_driver.get_screenshot_as_png()
        screenshot_mol_bytes = third_driver.get_screenshot_as_png()

        image_101 = self.load_image_from_bytes(screenshot_101_bytes)
        image_pol = self.load_image_from_bytes(screenshot_pol_bytes)
        image_mol = self.load_image_from_bytes(screenshot_mol_bytes)

        get_result = self.check_images_difference(image_101, image_mol, image_pol)
        image_result = self.load_image_from_bytes(get_result[1])
        image_mol.show()
        image_101.show()
        image_pol.show()
        image_result.show()

    @allure.title("Сравнение страницы 'тарифы'")
    def test_rates(self, driver: webdriver.Chrome):
        path = '/rates'
        driver.get(host_101 + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        second_driver = create_screenshot_driver()
        second_driver.get(host_pol + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        third_driver = create_screenshot_driver()
        third_driver.get(host_mol + path)
        third_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        screenshot_101_bytes = driver.get_screenshot_as_png()
        screenshot_pol_bytes = second_driver.get_screenshot_as_png()
        screenshot_mol_bytes = third_driver.get_screenshot_as_png()

        image_101 = self.load_image_from_bytes(screenshot_101_bytes)
        image_pol = self.load_image_from_bytes(screenshot_pol_bytes)
        image_mol = self.load_image_from_bytes(screenshot_mol_bytes)

        get_result = self.check_images_difference(image_101, image_mol, image_pol)
        image_result = self.load_image_from_bytes(get_result[1])
        image_mol.show()
        image_101.show()
        image_pol.show()
        image_result.show()

    @allure.title("Сравнение страницы 'интернет в офис'")
    def test_orders_office(self, driver: webdriver.Chrome):
        path = '/orders/office'
        driver.get(host_101 + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        second_driver = create_screenshot_driver()
        second_driver.get(host_pol + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        third_driver = create_screenshot_driver()
        third_driver.get(host_mol + path)
        third_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)

        screenshot_101_bytes = driver.get_screenshot_as_png()
        screenshot_pol_bytes = second_driver.get_screenshot_as_png()
        screenshot_mol_bytes = third_driver.get_screenshot_as_png()

        image_101 = self.load_image_from_bytes(screenshot_101_bytes)
        image_pol = self.load_image_from_bytes(screenshot_pol_bytes)
        image_mol = self.load_image_from_bytes(screenshot_mol_bytes)

        get_result = self.check_images_difference(image_101, image_mol, image_pol)
        image_result = self.load_image_from_bytes(get_result[1])
        image_mol.show()
        image_101.show()
        image_pol.show()
        image_result.show()