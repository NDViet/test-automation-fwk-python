from selenium import webdriver


class DriverManager:
    _driver = None

    @staticmethod
    def get_driver():
        return DriverManager._driver

    @staticmethod
    def set_driver(driver):
        DriverManager._driver = driver

    @staticmethod
    def quit():
        DriverManager._driver.quit()
        DriverManager._driver = None
