import yaml

from ndviet_test_automation.utilities.src.configuration.abstract_configuration import AbstractConfiguration
from ndviet_test_automation.utilities.src.dictionary.dict_utils import DictUtils


class YamlConfiguration(AbstractConfiguration):
    def __init__(self):
        super().__init__()
        self.m_data = {}

    def read_configuration_from(self, file_path):
        with open(file_path, 'r') as stream:
            try:
                self.m_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        print(self.m_data)

    def get_value(self, key):
        return DictUtils.get_value_as_string(self.m_data, key)

    def get_list_values(self, key):
        values = DictUtils.get_value_as_object(self.m_data, key)
        print(values)
        if isinstance(values, list) or values is None:
            return values
        else:
            raise Exception("Return object is not a List")

    def get_dict_values(self, key):
        values = DictUtils.get_value_as_object(self.m_data, key)
        if isinstance(values, dict) or values is None:
            return values
        else:
            raise Exception("Return object is not a Dictionary")
