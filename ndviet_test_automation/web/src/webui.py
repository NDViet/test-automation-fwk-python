from ndviet_test_automation.web.src.driver.driver_manager import DriverManager
from ndviet_test_automation.web.src.driver.target_factory import TargetFactory
from ndviet_test_automation.web.src.web_element_helpers import WebElementHelpers
from ndviet_test_automation.web.src.webui_abstract import WebUIAbstract
from ndviet_test_automation.utilities.src.test_object.object_repository import ObjectRepository

from robot.api.deco import keyword


class WebUI:
    @staticmethod
    @keyword
    def openBrowser(url=None, browser=None, implicit_wait_time=30):
        if not browser:
            DriverManager.set_driver(TargetFactory.create_instance())
        else:
            DriverManager.set_driver(TargetFactory.create_instance(browser))
        if url:
            WebUI.navigateToUrl(url)
        if implicit_wait_time and implicit_wait_time > 0:
            DriverManager.get_driver().implicitly_wait(implicit_wait_time)
        return DriverManager.get_driver()

    @staticmethod
    @keyword
    def navigateToUrl(url):
        DriverManager.get_driver().get(url)

    @staticmethod
    def closeBrowser():
        DriverManager.quit()

    @staticmethod
    def findWebElement(test_object):
        driver = DriverManager.get_driver()
        return WebElementHelpers.find_web_element(driver, test_object)

    @staticmethod
    def findWebElements(test_object):
        driver = DriverManager.get_driver()
        return WebElementHelpers.find_web_elements(driver, test_object)

    @staticmethod
    def click(object_id, timeout=-1, variables=None):
        driver = DriverManager.get_driver()
        WebUIAbstract.click(driver, ObjectRepository.find_test_object(object_id, variables), timeout)

    @staticmethod
    def setText(object_id, text, timeout=-1, variables=None):
        driver = DriverManager.get_driver()
        WebUIAbstract.set_text(driver, ObjectRepository.find_test_object(object_id, variables), text, timeout)

    @staticmethod
    def sendKey(object_id, key_name, timeout=-1, variables=None):
        driver = DriverManager.get_driver()
        WebUIAbstract.send_key(driver, ObjectRepository.find_test_object(object_id, variables), key_name)

    @staticmethod
    def getText(object_id, timeout=-1, variables=None):
        driver = DriverManager.get_driver()
        return WebUIAbstract.get_text(driver, ObjectRepository.find_test_object(object_id, variables), timeout)

    @staticmethod
    def getAttributeValue(object_id, attribute_name, timeout=-1, variables=None):
        driver = DriverManager.get_driver()
        return WebUIAbstract.get_attribute_value(driver, ObjectRepository.find_test_object(object_id, variables), attribute_name, timeout)

    @staticmethod
    def getTexts(test_object):
        driver = DriverManager.get_driver()
        return WebUIAbstract.getTexts(driver, test_object)

    @staticmethod
    def moveToElement(test_object):
        driver = DriverManager.get_driver()
        WebUIAbstract.moveToElement(driver, test_object)

    @staticmethod
    def scrollToElement(test_object):
        driver = DriverManager.get_driver()
        WebUIAbstract.scrollToElement(driver, test_object)

    @staticmethod
    def uploadFile(test_object, absolute_path):
        driver = DriverManager.get_driver()
        WebUIAbstract.uploadFile(driver, test_object, absolute_path)

    @staticmethod
    def verifyElementPresent(test_object):
        driver = DriverManager.get_driver()
        WebUIAbstract.verifyElementPresent(driver, test_object)

    @staticmethod
    def verifyElementNotPresent(test_object):
        driver = DriverManager.get_driver()
        WebUIAbstract.verifyElementNotPresent(driver, test_object)

    @staticmethod
    def verifyElementVisible(test_object):
        driver = DriverManager.get_driver()
        WebUIAbstract.verifyElementVisible(driver, test_object)

    @staticmethod
    def verifyElementNotVisible(test_object):
        driver = DriverManager.get_driver()
        WebUIAbstract.verifyElementNotVisible(driver, test_object)

    @staticmethod
    def verifyElementTextEquals(test_object, expect_text):
        driver = DriverManager.get_driver()
        WebUIAbstract.verifyElementTextEquals(driver, test_object, expect_text)

    @staticmethod
    def verifyElementTextContains(test_object, expect_text):
        driver = DriverManager.get_driver()
        WebUIAbstract.verifyElementTextContains(driver, test_object, expect_text)
