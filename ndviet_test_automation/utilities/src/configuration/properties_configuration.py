import os
import configparser
from robot.libraries.BuiltIn import BuiltIn

from ndviet_test_automation.utilities.src.configuration.abstract_configuration import AbstractConfiguration


class PropertiesConfiguration(AbstractConfiguration):
    def __init__(self):
        super().__init__()
        self.m_data = {}

    def read_configuration_from(self, file_path):
        self.m_data = {}
        config = configparser.ConfigParser()
        if file_path is None:
            self.m_data = dict(os.environ)
        else:
            with open(file_path, 'r') as f:
                config.read_file(f)
            for section in config.sections():
                for key, val in config.items(section):
                    self.m_data[key] = val
        print(self.m_data)

    def get_value(self, key):
        print("Get value from properties configuration " + '${' + str(key) + '}')
        print(BuiltIn().get_variable_value('${' + str(key) + '}'))
        if BuiltIn().get_variable_value('${' + str(key) + '}') is not None:
            return BuiltIn().get_variable_value('${' + str(key) + '}')
        else:
            return self.m_data.get(key)

    def get_list_values(self, key):
        return None

    def get_dict_values(self, key):
        return None
