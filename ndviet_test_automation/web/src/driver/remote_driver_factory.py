from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from ndviet_test_automation.web.src.driver.browser_factory import BrowserFactory
import urllib.parse
import logging

from ndviet_test_automation.utilities.src.configuration.configuration_manager import ConfigurationManager
from ndviet_test_automation.utilities.src.configuration.constants import Constants


class RemoteDriverFactory:
    LOGGER = logging.getLogger('RemoteDriverFactory')

    @staticmethod
    def create_remote_instance(browser):
        capability = BrowserFactory.get_options(browser.upper())
        try:
            hub_url = ConfigurationManager.get_instance().get_value(Constants.SELENIUM_HUB_URL)
            return webdriver.Remote(command_executor=hub_url, desired_capabilities=capability,
                                    options=RemoteDriverFactory.get_enable_tracing())
        except Exception as e:
            RemoteDriverFactory.LOGGER.error("Could not open the browser.\n" + str(e))
            raise Exception(e)

    @staticmethod
    def get_enable_tracing():
        return bool(ConfigurationManager.get_instance().get_value(Constants.SELENIUM_ENABLE_TRACING))
