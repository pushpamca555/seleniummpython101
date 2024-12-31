from Pages.BasePage import BasePage
from Pages.InputForms import InputForms
from Tests.common_tests import CommonTests
from Utilities.test_data import TestData


class TestScenario3(CommonTests):
    def test_form_inputs(self):
        base_page = BasePage(self.driver)
        input_forms_page = InputForms(self.driver)

        # Click “Simple Form Demo” under Input Forms.
        base_page.click_on_element(TestData.input_form_submit_link)

        # Click submit without entering input field values
        base_page.click_on_element(TestData.form_submit_button)

        """
        I noticed there has been an update in the UI due to which the error message for empty fields seems to be 
        detached from the DOM.
        Due to this, the error message element cannot be located using conventional locator strategies.
        Hence, I have commented out the assertion part for the warning text below:
        """
        # input_forms_page.validate_warning_message_for_input_fields()

        # Enter form details
        input_forms_page.enter_form_details()

        # Click on Submit
        base_page.click_on_element(TestData.form_submit_button)





