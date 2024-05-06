from ndviet_test_automation.web.src.driver.driver_manager import DriverManager
from ndviet_test_automation.web.src.driver.target_factory import TargetFactory
from ndviet_test_automation.web.src.web_element_helpers import WebElementHelpers
from ndviet_test_automation.web.src.webui_abstract import WebUIAbstract
from ndviet_test_automation.utilities.src.test_object.object_repository import ObjectRepository

from robot.api.deco import keyword


class WebUI:
    @staticmethod
    @keyword
    def openBrowser(url=None, browser=None):
        if not browser:
            DriverManager.set_driver(TargetFactory.create_instance())
        else:
            DriverManager.set_driver(TargetFactory.create_instance(browser))
        if url:
            WebUI.navigateToUrl(url)
        return DriverManager.get_driver()

    @staticmethod
    @keyword
    def navigateToUrl(url):
        DriverManager.get_driver().get(url)

    @staticmethod
    def closeBrowser():
        DriverManager.quit()

    @staticmethod
    def findWebElement(driver_manager, test_object):
        driver = driver_manager.get_driver()
        return WebElementHelpers.find_web_element(driver, test_object)

    @staticmethod
    def findWebElements(driver_manager, test_object):
        driver = driver_manager.get_driver()
        return WebElementHelpers.find_web_elements(driver, test_object)

    @staticmethod
    def click(object_id, timeout=-1, variables=None):
        driver = DriverManager.get_driver()
        WebUIAbstract.click(driver, ObjectRepository.find_test_object(object_id, variables), timeout)

    @staticmethod
    def setText(driver_manager, test_object, text):
        driver = driver_manager.get_driver()
        WebUIAbstract.setText(driver, test_object, text)

    @staticmethod
    def getText(driver_manager, test_object):
        driver = driver_manager.get_driver()
        return WebUIAbstract.getText(driver, test_object)

    @staticmethod
    def getTexts(driver_manager, test_object):
        driver = driver_manager.get_driver()
        return WebUIAbstract.getTexts(driver, test_object)

    @staticmethod
    def moveToElement(driver_manager, test_object):
        driver = driver_manager.get_driver()
        WebUIAbstract.moveToElement(driver, test_object)

    @staticmethod
    def scrollToElement(driver_manager, test_object):
        driver = driver_manager.get_driver()
        WebUIAbstract.scrollToElement(driver, test_object)

    @staticmethod
    def uploadFile(driver_manager, test_object, absolute_path):
        driver = driver_manager.get_driver()
        WebUIAbstract.uploadFile(driver, test_object, absolute_path)

    @staticmethod
    def verifyElementPresent(driver_manager, test_object):
        driver = driver_manager.get_driver()
        WebUIAbstract.verifyElementPresent(driver, test_object)

    @staticmethod
    def verifyElementNotPresent(driver_manager, test_object):
        driver = driver_manager.get_driver()
        WebUIAbstract.verifyElementNotPresent(driver, test_object)

    @staticmethod
    def verifyElementVisible(driver_manager, test_object):
        driver = driver_manager.get_driver()
        WebUIAbstract.verifyElementVisible(driver, test_object)

    @staticmethod
    def verifyElementNotVisible(driver_manager, test_object):
        driver = driver_manager.get_driver()
        WebUIAbstract.verifyElementNotVisible(driver, test_object)

    @staticmethod
    def verifyElementTextEquals(driver_manager, test_object, expect_text):
        driver = driver_manager.get_driver()
        WebUIAbstract.verifyElementTextEquals(driver, test_object, expect_text)

    @staticmethod
    def verifyElementTextContains(driver_manager, test_object, expect_text):
        driver = driver_manager.get_driver()
        WebUIAbstract.verifyElementTextContains(driver, test_object, expect_text)
