from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ndviet_test_automation.utilities.src.configuration.configuration_manager import ConfigurationManager
from ndviet_test_automation.utilities.src.configuration.constants import Constants
from ndviet_test_automation.web.src.web_element_helpers import WebElementHelpers

config_default_time_out = ConfigurationManager.get_instance().get_value(Constants.SELENIUM_DEFAULT_TIMEOUT)
m_default_time_out = 10 if config_default_time_out is None else int(config_default_time_out)


def get_wait_driver(driver, is_wait, time_out=m_default_time_out):
    if is_wait:
        if time_out >= 0:
            wait = WebDriverWait(driver, time_out)
        else:
            wait = get_wait_driver(driver, True)
    else:
        wait = WebDriverWait(driver, 0)
    return wait


class Element:
    @staticmethod
    def presence_of_element_located(driver, object, is_wait, time_out):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.presence_of_element_located(WebElementHelpers.get_by(object))
        )

    @staticmethod
    def element_to_be_clickable(driver, object, is_wait, time_out):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.element_to_be_clickable(WebElementHelpers.get_by(object))
        )

    @staticmethod
    def visibility_of(driver, object, is_wait, time_out):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.visibility_of(
                EC.presence_of_element_located(WebElementHelpers.get_by(object))
            )
        )

    @staticmethod
    def visibility_of_element_located(driver, object, is_wait, time_out):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.visibility_of_element_located(WebElementHelpers.get_by(object))
        )


class Elements:
    @staticmethod
    def presence_of_all_elements_located(driver, object, is_wait, time_out):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.presence_of_all_elements_located(WebElementHelpers.get_by(object))
        )

    @staticmethod
    def visibility_of_all_elements_located_by(driver, object, is_wait, time_out):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.visibility_of_all_elements_located(WebElementHelpers.get_by(object))
        )


class Condition:
    @staticmethod
    def invisibility_of_element_located(driver, object, is_wait, time_out, expect_text):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.invisibility_of_element_located(WebElementHelpers.get_by(object))
        )

    @staticmethod
    def not_presence_of_element_located(driver, object, is_wait, time_out, expect_text):
        return get_wait_driver(driver, is_wait, time_out).until_not(
            EC.presence_of_element_located(WebElementHelpers.get_by(object))
        )

    @staticmethod
    def text_to_be_present_in_element_located(driver, object, is_wait, time_out, expect_text):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.text_to_be_present_in_element(WebElementHelpers.get_by(object), expect_text)
        )

    @staticmethod
    def text_to_be_present_in_element(driver, object, is_wait, time_out, expect_text):
        return get_wait_driver(driver, is_wait, time_out).until(
            EC.text_to_be_present_in_element(
                EC.text_to_be_present_in_element(WebElementHelpers.get_by(object), expect_text)
            )
        )
