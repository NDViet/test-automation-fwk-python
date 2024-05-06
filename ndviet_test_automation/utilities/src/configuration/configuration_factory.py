from ndviet_test_automation.utilities.src.configuration.configuration_ordering import ConfigurationOrdering
from ndviet_test_automation.utilities.src.configuration.properties_configuration import PropertiesConfiguration

from ndviet_test_automation.utilities.src.configuration.constants import Constants


class ConfigurationFactory:
    @staticmethod
    def create_instance():
        try:
            properties_configuration = PropertiesConfiguration()
            properties_configuration.read_configuration_from(None)
            configuration_ordering = ConfigurationFactory.extract_ordering_configurations(properties_configuration)
            configurations = ConfigurationOrdering(
                properties_configuration.get_value(Constants.PROP_CONFIGURATION_BASE),
                configuration_ordering)
        except Exception as e:
            raise Exception("Could not create Configuration instance", e)
        return configurations

    @staticmethod
    def extract_ordering_configurations(configuration):
        list_keys = [key for key in configuration.get_data().keys() if Constants.PROP_CONFIGURATION_ORDERING in key]
        list_keys.sort()
        list_files = [configuration.get_value(key) for key in list_keys if configuration.get_value(key)]
        return list_files
