import logging

from ndviet_test_automation.utilities.src.configuration.configuration_manager import ConfigurationManager

from ndviet_test_automation.utilities.src.configuration.constants import Constants

logger = logging.getLogger('ConfigurationHelpers')


def get_system_locale():
    locale_language_tag = ConfigurationManager.get_instance().get_value(Constants.LOCALE_LANGUAGE_TAG)
    locale_language_tag = "en-US" if locale_language_tag is None else locale_language_tag
    components = locale_language_tag.split("-")
    try:
        locale = (components[0], components[1])
    except Exception as e:
        logger.error("Could not create Locale instance. Kindly check the Language Tag")
        raise e
    return locale
