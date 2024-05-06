import os
import yaml

from ndviet_test_automation.utilities.src.configuration.configuration_manager import ConfigurationManager

from ndviet_test_automation.utilities.src.configuration.constants import Constants
from ndviet_test_automation.utilities.src.dictionary.dict_utils import DictUtils


class WebElementIdentifier:
    m_data = {}
    m_instance = None

    def __init__(self):
        self.set_element_files()

    @staticmethod
    def get_instance():
        if WebElementIdentifier.m_instance is None:
            WebElementIdentifier.m_instance = WebElementIdentifier()
        return WebElementIdentifier.m_instance

    def set_element_files(self):
        directory = ConfigurationManager.get_instance().get_value(Constants.WEB_ELEMENT_IDENTIFIERS_DIRECTORY)
        self.load_element_files(directory)

    def load_element_files(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith(".yaml") or filename.endswith(".yml"):
                with open(os.path.join(directory, filename), 'r') as stream:
                    try:
                        DictUtils.recursive_merge(WebElementIdentifier.m_data, yaml.safe_load(stream))
                        print(f"Loaded file: {filename}")
                    except yaml.YAMLError as exc:
                        print(exc)

    def get_identifier(self, key):
        return DictUtils.get_value_as_string(WebElementIdentifier.m_data, key)
