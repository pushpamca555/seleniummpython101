import pytest
import time

from Pages.BasePage import BasePage
from Pages.SimpleFormDemo import SimpleFormDemo
from Tests.common_tests import CommonTests
from Utilities.test_data import TestData


class TestScenario1(CommonTests):
    def test_simple_form_demo(self):
        base_page = BasePage(self.driver)
        simple_form_demo = SimpleFormDemo(self.driver)

        # Click “Simple Form Demo” under Input Forms.
        base_page.click_on_element(TestData.simple_form_demo_link)
        time.sleep(2)

        # Validate that the URL contains “simple-form-demo"
        simple_form_demo.verify_url_contains_text("simple-form-demo")

        # Create a variable for a string value E.g: “Welcome to LambdaTest
        text_field_value = "Welcome to LambdaTest"

        # Use this variable to enter values in the “Enter Message” text box
        base_page.enter_text_in_field(TestData.enter_message_text_field, text_field_value)

        # Click “Get Checked Value"
        base_page.click_on_element(TestData.get_checked_button)

        # Validate whether the same text message is displayed in the right-hand
        # panel under the “Your Message:” section.
        simple_form_demo.validate_your_message("Welcome to LambdaTest")


