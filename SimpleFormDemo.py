from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities.test_data import TestData


class SimpleFormDemo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_url_contains_text(self, expected_text):
        actual_url = BasePage.get_current_url(self)
        assert expected_text.lower() in actual_url, \
            "'{}' is not present in the url of the page!".format(expected_text)

    def validate_your_message(self, expected_message):
        actual_message = BasePage.get_text_in_element(self, TestData.your_message)
        assert actual_message == expected_message, \
            "Expected and Actual Messages do not match! Expected: {}, Actual: {}".format(
                expected_message, actual_message
            )
