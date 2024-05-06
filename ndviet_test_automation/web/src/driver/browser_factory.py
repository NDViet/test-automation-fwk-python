from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from ndviet_test_automation.utilities.src.configuration.configuration_manager import ConfigurationManager
from ndviet_test_automation.utilities.src.configuration.constants import Constants


class BrowserFactory:
    @staticmethod
    def create_local_driver(browser_type):
        if browser_type == 'CHROME':
            return webdriver.Chrome(BrowserFactory.get_options('CHROME'))
        elif browser_type == 'FIREFOX':
            return webdriver.Firefox(BrowserFactory.get_options('FIREFOX'))
        elif browser_type == 'EDGE':
            return webdriver.Edge()
        elif browser_type == 'SAFARI':
            return None
        else:
            raise Exception("Browser type not supported")

    @staticmethod
    def get_options(browser_type):
        if browser_type == 'CHROME':
            options = ChromeOptions()
            list_args = ConfigurationManager.get_instance().get_list_values(Constants.SELENIUM_CHROME_ARGS)
            if list_args is not None:
                for arg in list_args:
                    options.add_argument(arg)
            list_prefs = ConfigurationManager.get_instance().get_dict_values(Constants.SELENIUM_CHROME_PREFS)
            if list_prefs is not None:
                for key, value in list_prefs.items():
                    options.add_experimental_option(key, value)
            return options
        elif browser_type == 'FIREFOX':
            options = FirefoxOptions()
            list_args = ConfigurationManager.get_instance().get_list_values(Constants.SELENIUM_FIREFOX_ARGS)
            if list_args is not None:
                for arg in list_args:
                    options.add_argument(arg)
            list_prefs = ConfigurationManager.get_instance().get_dict_values(Constants.SELENIUM_FIREFOX_PREFS)
            if list_prefs is not None:
                for key, value in list_prefs.items():
                    options.set_preference(key, value)
            return options
        else:
            return None
