from abc import ABC, abstractmethod


class AbstractConfiguration(ABC):
    def __init__(self):
        self.m_data = {}

    def get_data(self):
        return self.m_data

    @abstractmethod
    def read_configuration_from(self, file_path):
        pass

    @abstractmethod
    def get_value(self, key):
        pass

    @abstractmethod
    def get_list_values(self, key):
        pass

    @abstractmethod
    def get_dict_values(self, key):
        pass
