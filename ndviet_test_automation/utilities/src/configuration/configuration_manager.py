from ndviet_test_automation.utilities.src.configuration.configuration_factory import ConfigurationFactory


class ConfigurationManager:
    configurations = None

    @staticmethod
    def get_instance():
        if ConfigurationManager.configurations is None:
            ConfigurationManager.set_instance(ConfigurationFactory.create_instance())
        return ConfigurationManager.configurations

    @staticmethod
    def set_instance(configuration_ordering):
        ConfigurationManager.configurations = configuration_ordering

    @staticmethod
    def release():
        ConfigurationManager.configurations = None
