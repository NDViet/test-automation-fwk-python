from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from ndviet_test_automation.utilities.src.test_object.test_object import TestObject


class WebElementHelpers:
    @staticmethod
    def get_by(object):
        if isinstance(object, TestObject):
            text_object = object.get_value()
        else:
            text_object = str(object)

        if text_object.startswith("xpath="):
            return By.XPATH, text_object.replace("xpath=", "")
        elif text_object.startswith("cssSelector="):
            return By.CSS_SELECTOR, text_object.replace("cssSelector=", "")
        else:
            return By.XPATH, text_object

    @staticmethod
    def find_web_element(driver, test_object):
        return driver.find_element(*WebElementHelpers.get_by(test_object))

    @staticmethod
    def find_web_elements(driver, test_object):
        return driver.find_elements(*WebElementHelpers.get_by(test_object))

    @staticmethod
    def scroll_into_view(driver, element):
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @staticmethod
    def get_web_element(driver, object):
        if isinstance(object, TestObject):
            element = WebElementHelpers.find_web_element(driver, object)
        elif isinstance(object, webdriver.remote.webelement.WebElement):
            element = WebElementHelpers.is_refreshed(driver, object)
        else:
            element = object[0]

        WebElementHelpers.scroll_into_view(driver, element)
        return element

    @staticmethod
    def is_refreshed(driver, element):
        try:
            element.is_enabled()
            return element
        except StaleElementReferenceException:
            return WebElementHelpers.refresh_web_element(driver, element)

    @staticmethod
    def refresh_web_element(driver, element):
        element_info = str(element)
        element_info = element_info[element_info.index("->"):]
        element_locator = element_info[element_info.index(": "):]
        element_locator = element_locator[2:-1]

        if "-> link text:" in element_info:
            return driver.find_element(By.LINK_TEXT, element_locator)
        elif "-> name:" in element_info:
            return driver.find_element(By.NAME, element_locator)
        elif "-> id:" in element_info:
            return driver.find_element(By.ID, element_locator)
        elif "-> xpath:" in element_info:
            return driver.find_element(By.XPATH, element_locator)
        elif "-> class name:" in element_info:
            return driver.find_element(By.CLASS_NAME, element_locator)
        elif "-> css selector:" in element_info:
            return driver.find_element(By.CSS_SELECTOR, element_locator)
        elif "-> partial link text:" in element_info:
            return driver.find_element(By.PARTIAL_LINK_TEXT, element_locator)
        elif "-> tag name:" in element_info:
            return driver.find_element(By.TAG_NAME, element_locator)
        else:
            raise Exception("Could not refresh the WebElement.")
