import os
import tempfile

from ndviet_test_automation.utilities.src.configuration.configuration_manager import ConfigurationManager
from ndviet_test_automation.utilities.src.configuration.constants import Constants
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

from ndviet_test_automation.utilities.src.file.file_helpers import FileHelpers
from ndviet_test_automation.web.src.driver.driver_manager import DriverManager


class TakeScreenshot:
    m_directory = get_screenshot_directory()
    m_fileType = get_screenshot_file_type()
    m_count = Constants.DEFAULT_SCREENSHOT_COUNT

    @staticmethod
    def reset_screenshot_count():
        m_count = Constants.DEFAULT_SCREENSHOT_COUNT

    @staticmethod
    def get_screenshot_file_type():
        file_type = ConfigurationManager.get_instance().get_value(Constants.SELENIUM_SCREENSHOT_FILE_TYPE)
        if file_type is not None and file_type != "":
            return file_type
        else:
            return "png"

    @staticmethod
    def get_screenshot_directory():
        file_type = ConfigurationManager.get_instance().get_value(Constants.SELENIUM_SCREENSHOT_DIRECTORY)
        if file_type is not None and file_type != "":
            return file_type
        else:
            return os.path.join(os.getcwd(), Constants.TARGET_DIR, Constants.SCREENSHOT_DIR)

    @staticmethod
    def capture_full_page_screenshot(file_name):
        driver = DriverManager.get_driver()
        screenshot = driver.get_screenshot_as_png()
        target_file = get_target_file(file_name)
        with open(target_file, 'wb') as f:
            f.write(screenshot)
        print(f"Screenshot is available in location: {target_file}")
        return target_file

    @staticmethod
    def capture_page_screenshot(file_name):
        driver = DriverManager.get_driver()
        screenshot = driver.get_screenshot_as_png()
        target_file = get_target_file(file_name)
        with open(target_file, 'wb') as f:
            f.write(screenshot)
        print(f"Screenshot is available in location: {target_file}")
        return target_file

    @staticmethod
    def get_target_file(file_name):
        FileHelpers.is_directory(m_directory, True)
        if file_name is None:
            target_file = tempfile.NamedTemporaryFile(suffix=f"_SS.{m_fileType}", dir=m_directory, delete=False).name
        else:
            target_file = os.path.join(m_directory, f"{file_name}_SS_{m_count}.{m_fileType}")
            m_count += 1
        return target_file
