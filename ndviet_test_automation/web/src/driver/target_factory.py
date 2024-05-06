from ndviet_test_automation.utilities.src.configuration.configuration_manager import ConfigurationManager
from ndviet_test_automation.web.src.driver.browser_factory import BrowserFactory
from ndviet_test_automation.web.src.driver.remote_driver_factory import RemoteDriverFactory

from ndviet_test_automation.utilities.src.configuration.constants import Constants

import logging


class TargetFactory:
    LOGGER = logging.getLogger('TargetFactory')

    @staticmethod
    def create_instance(browser=None, target=None):
        if browser is None:
            browser = ConfigurationManager.get_instance().get_value(Constants.SELENIUM_BROWSER_TYPE)
        if target is None:
            target = ConfigurationManager.get_instance().get_value(Constants.SELENIUM_WEB_DRIVER_TARGET)

        instance = target.upper()
        if instance == 'LOCAL':
            return BrowserFactory.create_local_driver(browser.upper())
        elif instance == 'REMOTE':
            return RemoteDriverFactory.create_remote_instance(browser)
        else:
            raise Exception("Target is still not support!")

    @staticmethod
    def is_remote_target():
        target = ConfigurationManager.get_instance().get_value(Constants.SELENIUM_WEB_DRIVER_TARGET)
        return target.upper() == 'REMOTE'
