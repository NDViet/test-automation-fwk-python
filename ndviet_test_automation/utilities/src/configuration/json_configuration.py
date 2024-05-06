import json

from ndviet_test_automation.utilities.src.configuration.abstract_configuration import AbstractConfiguration


class JsonConfiguration(AbstractConfiguration):
    def __init__(self):
        super().__init__()
        self.m_data = {}

    def read_configuration_from(self, file_path):
        with open(file_path, 'r') as json_file:
            self.m_data = json.load(json_file)

    def get_value(self, key):
        return self.m_data.get(key)

    def get_list_values(self, key):
        values = self.m_data.get(key)
        if isinstance(values, list) or values is None:
            return values
        else:
            raise Exception("Return object is not a List")

    def get_dict_values(self, key):
        values = self.m_data.get(key)
        if isinstance(values, dict) or values is None:
            return values
        else:
            raise Exception("Return object is not a HashMap")
