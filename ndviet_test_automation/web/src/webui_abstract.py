from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from ndviet_test_automation.web.src.waiting import Element as WaitElement
from ndviet_test_automation.web.src.web_element_helpers import WebElementHelpers


class WebUIAbstract:
    @staticmethod
    def click(driver, test_object, timeout=-1):
        try:
            element = WaitElement.element_to_be_clickable(driver, test_object, True, timeout)
            WebElementHelpers.scroll_into_view(driver, element)
            element.click()
        except Exception as e:
            print(f"{test_object} could not be clicked successfully.")
            raise e

    def set_text(driver, test_object, text, timeout=-1):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((test_object.get_identifier_type(), test_object.get)))
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.send_keys(text)
        except Exception as e:
            print(f"{test_object} could not set text successfully.")
            raise e

    @staticmethod
    def getText(driver, test_object):
        text = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((test_object.get_identifier_type(), test_object.get_identifier_value()))).text
        print(f"Text in element: {text}")
        return text

    @staticmethod
    def getTexts(driver, test_object):
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (test_object.get_identifier_type(), test_object.get_identifier_value())))
        texts = [element.text.strip() for element in elements]
        print(f"List texts: {texts}")
        return texts

    @staticmethod
    def moveToElement(driver, test_object):
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((test_object.get_identifier_type(), test_object.get_identifier_value())))
        ActionChains(driver).move_to_element(element).perform()

    @staticmethod
    def scrollToElement(driver, test_object):
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((test_object.get_identifier_type(), test_object.get_identifier_value())))
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def uploadFile(driver, test_object, absolute_path):
        if isinstance(driver, RemoteWebDriver):
            driver.file_detector = LocalFileDetector()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((test_object.get_identifier_type(), test_object.get_identifier_value())))
        element.send_keys(absolute_path)

    @staticmethod
    def verifyElementPresent(driver, test_object):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((test_object.get_identifier_type(), test_object.get_identifier_value())))
        except NoSuchElementException:
            print(f"Element {test_object} is not present.")
            raise

    @staticmethod
    def verifyElementNotPresent(driver, test_object):
        try:
            WebDriverWait(driver, 10).until_not(
                EC.presence_of_element_located((test_object.get_identifier_type(), test_object.get_identifier_value())))
        except NoSuchElementException:
            print(f"Element {test_object} is present.")
            raise

    @staticmethod
    def verifyElementVisible(driver, test_object):
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (test_object.get_identifier_type(), test_object.get_identifier_value())))
        except NoSuchElementException:
            print(f"Element {test_object} is not visible.")
            raise

    @staticmethod
    def verifyElementNotVisible(driver, test_object):
        try:
            WebDriverWait(driver, 10).until_not(
                EC.visibility_of_element_located(
                    (test_object.get_identifier_type(), test_object.get_identifier_value())))
        except NoSuchElementException:
            print(f"Element {test_object} is visible.")
            raise

    @staticmethod
    def verifyElementTextEquals(driver, test_object, expect_text):
        try:
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element(
                    (test_object.get_identifier_type(), test_object.get_identifier_value()), expect_text))
            actual_text = driver.find_element(test_object.get_identifier_type(),
                                              test_object.get_identifier_value()).text
            if actual_text == expect_text:
                print(f"Value: {actual_text} is present in element and equal to: {expect_text}")
            else:
                raise Exception(f"Actual value: {actual_text} does not equal the expect value: {expect_text}")
        except Exception as e:
            print(f"Expect value: {expect_text} is not present in element")
            raise e

    @staticmethod
    def verifyElementTextContains(driver, test_object, expect_text):
        try:
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element(
                    (test_object.get_identifier_type(), test_object.get_identifier_value()), expect_text))
            actual_text = driver.find_element(test_object.get_identifier_type(),
                                              test_object.get_identifier_value()).text
            if expect_text in actual_text:
                print(f"Value: {actual_text} is present in element and contain: {expect_text}")
            else:
                raise Exception(f"Actual value: {actual_text} does not contain the expect value: {expect_text}")
        except Exception as e:
            print(f"Expect value: {expect_text} is not present in element")
            raise e
