from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities.test_data import TestData


class InputForms(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # values for the form inputs
    name = "Pranav Naik"
    email = "testadmin@lambdatest.com"
    password = "@1234$lamdatest"
    company = "Lambdatest"
    website = "https://www.lambdatest.com/"
    country = "United States"
    city = "New York City"
    address_line_1 = "7953 Vernon Ave"
    address_line_2 = "Brooklyn"
    state = "NY"
    zip_code = "11208"

    """
    I noticed there has been an update in the UI due to which the error message for empty fields seems to be 
    detached from the DOM.
    Due to this, the error message element cannot be located using conventional locator strategies.
    Hence, I have commented out the assertion part for the warning text below:
    """

    def validate_warning_message_for_input_fields(self):
        base_page = BasePage(self)
        expected_error_message = "Please fill in this field"
        actual_error_message = base_page.get_text_in_element(TestData.warning_message)
        assert actual_error_message == expected_error_message, \
            "Actual Error message : '{}' does not match the Expected: '{}'".format(
                actual_error_message, expected_error_message
            )

    def select_from_dropdown(self, value):
        base_page = BasePage(self.driver)

        countries = base_page.driver.find_element(By.XPATH, TestData.country_dropdown_menu)

        select = Select(countries)
        select.select_by_visible_text(value)

    def enter_form_details(self):
        base_page = BasePage(self.driver)
        input_forms_page = InputForms(self.driver)

        base_page.enter_text_in_field(TestData.name_field, input_forms_page.name)
        base_page.enter_text_in_field(TestData.email_field, input_forms_page.email)
        base_page.enter_text_in_field(TestData.password_field, input_forms_page.password)
        base_page.enter_text_in_field(TestData.company_field, input_forms_page.company)
        base_page.enter_text_in_field(TestData.website_field, input_forms_page.website)

        input_forms_page.select_from_dropdown(input_forms_page.country)

        base_page.enter_text_in_field(TestData.city_field, input_forms_page.city)
        base_page.enter_text_in_field(TestData.address_1_field, input_forms_page.address_line_1)
        base_page.enter_text_in_field(TestData.address_2_field, input_forms_page.address_line_2)
        base_page.enter_text_in_field(TestData.state_field, input_forms_page.state)
        base_page.enter_text_in_field(TestData.zip_code_field, input_forms_page.zip_code)
