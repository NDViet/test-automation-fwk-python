from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from typing import List
import json
import yaml

from ndviet_test_automation.utilities.src.configuration.abstract_configuration import AbstractConfiguration
from ndviet_test_automation.utilities.src.configuration.configuration_manager import ConfigurationManager
from ndviet_test_automation.utilities.src.configuration.json_configuration import JsonConfiguration
from ndviet_test_automation.utilities.src.configuration.yaml_configuration import YamlConfiguration


class ConfigurationUtils:
    @keyword
    def getValue(self, key: str) -> str:
        return ConfigurationManager.get_instance().get_value(key)

    @keyword
    def getListValues(self, key: str) -> List[str]:
        return ConfigurationManager.get_instance().getListValues(key)

    @keyword
    def readYamlConfiguration(self, filePath: str) -> AbstractConfiguration:
        configuration = YamlConfiguration()
        configuration.read_configuration_from(filePath)
        return configuration

    @keyword
    def readJsonConfiguration(self, filePath: str) -> AbstractConfiguration:
        configuration = JsonConfiguration()
        configuration.read_configuration_from(filePath)
        return configuration
