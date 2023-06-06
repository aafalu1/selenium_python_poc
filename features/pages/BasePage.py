from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from features.utilities.LoadConfig import LoadConfig


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        element = self._wait_until_element_is_clickable(locator)
        element.click()

    def get_text(self, locator):
        element = self._wait_until_element_is_visible(locator)
        return element.text

    def enter_value(self, locator, value):
        element = self._wait_until_element_is_visible(locator)
        element.clear()
        element.send_keys(value)

    def _wait_until_element_is_visible(self, locator):
        element = self._wait_for_element(locator, EC.visibility_of_element_located)
        return element

    def _wait_until_element_is_clickable(self, locator):
        element = self._wait_for_element(locator, EC.element_to_be_clickable)
        return element

    def _wait_for_element(self, locator, condition):
        config = LoadConfig()
        explicit_wait = config.int_property_config('app', 'explicit_wait_time')
        try:
            element = WebDriverWait(self.driver, explicit_wait).until(condition(locator))
            return element
        except TimeoutException:
            raise Exception(f"Element {locator} not found or not matching the condition within the timeout period.")

    def get_application_url(self):
        config = LoadConfig()
        url=config.string_property_config('app', 'base_url')
        self.driver.get(url)