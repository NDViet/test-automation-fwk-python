import unittest
import os
from ndviet_test_automation.utilities.src.configuration.configuration_ordering import ConfigurationOrdering


class ConfigurationOrderingTests(unittest.TestCase):
    def setUp(self):
        self.config_ordering = ConfigurationOrdering(
            f"{os.getcwd()}/../../../tests/resources/configuration/baseConfiguration.yaml",
            [f"{os.getcwd()}/../../../tests/resources/configuration/seleniumConfiguration.yaml"])

    def test_get_value_returns_value_when_key_exists(self):
        result = self.config_ordering.get_value('selenium.hub.url')
        self.assertEqual(result, 'http://testops.ndviet.org/selenium')

    def test_list_values_returns_values_when_key_exists(self):
        result = self.config_ordering.get_list_values('selenium.browser.firefox.args')
        self.assertEqual(result, ['--ignore-certificate-errors', '--start-maximized', '--enable-logging', '-private'])

    def test_dict_values_returns_values_when_key_exists(self):
        result = self.config_ordering.get_dict_values('selenium.browser.chrome.prefs')
        self.assertEqual(result, {'se:recordVideo': True, 'se:screenResolution': '1920x1080'})


if __name__ == '__main__':
    unittest.main()
