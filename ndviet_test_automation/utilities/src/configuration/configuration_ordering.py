from ndviet_test_automation.utilities.src.configuration.json_configuration import JsonConfiguration
from ndviet_test_automation.utilities.src.configuration.properties_configuration import PropertiesConfiguration
from ndviet_test_automation.utilities.src.configuration.yaml_configuration import YamlConfiguration


class ConfigurationOrdering:
    def __init__(self, base_config_file, ordering_config_files):
        self.m_configurations = []
        self.set_config(self.initialize_configuration(None))
        for i in reversed(ordering_config_files):
            self.set_config(self.initialize_configuration(i))
        self.set_config(self.initialize_configuration(base_config_file))

    def set_config(self, configuration):
        if configuration is not None:
            self.m_configurations.append(configuration)

    def initialize_configuration(self, config_file_path):
        if config_file_path is None:
            configuration = PropertiesConfiguration()
            configuration.read_configuration_from(config_file_path)
        else:
            file_extension = config_file_path.split('.')[-1]
            if file_extension in ['yml', 'yaml']:
                configuration = YamlConfiguration()
            elif file_extension == 'json':
                configuration = JsonConfiguration()
            elif file_extension == 'properties':
                configuration = PropertiesConfiguration()
            else:
                raise Exception("Configuration file type is not support!")
            configuration.read_configuration_from(config_file_path)
        return configuration

    def get_value(self, key):
        value = None
        for configuration in self.m_configurations:
            print(f"Checking config layer: {configuration}")
            value = configuration.get_value(key)
            if value is not None:
                break
        return value

    def get_list_values(self, key):
        values = None
        for configuration in self.m_configurations:
            values = configuration.get_list_values(key)
            if values is not None:
                break
        return values

    def get_dict_values(self, key):
        values = None
        for configuration in self.m_configurations:
            values = configuration.get_dict_values(key)
            if values is not None:
                break
        return values
