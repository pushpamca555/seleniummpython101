from selenium.webdriver.common.by import By


class TestData:
    """
    This class stores all the test data and locators required for the test scenario automation
    """

    base_url = "https://www.lambdatest.com/selenium-playground"

    # Scenario 1:
    simple_form_demo_link = (By.XPATH, "//a[normalize-space()='Simple Form Demo']")

    enter_message_text_field = (By.CSS_SELECTOR, "input#user-message")
    get_checked_button = (By.XPATH, "//button[text() = 'Get Checked Value']")
    your_message = (By.CSS_SELECTOR, "p#message")

    # Scenario 2:
    drag_and_drop_slider_link = (By.XPATH, "//a[normalize-space()='Drag & Drop Sliders']")
    default_value_15_slider = "//input[@value='15']"
    slider_value_output = (By.XPATH, "//input[@value='15']/following-sibling::output")

    # Scenario 3:
    input_form_submit_link = (By.XPATH, "//a[normalize-space()='Input Form Submit']")
    form_submit_button = (By.XPATH, "//button[normalize-space()='Submit']")

    # warning message for empty field submission
    # the below locator does not locate the warning message as it seems to be detached from the DOM
    warning_message = (By.XPATH, "//*[contains(text(),'Please fill in this field')]")

    name_field = (By.XPATH, "//input[@name='name']")
    email_field = (By.CSS_SELECTOR, "input#inputEmail4")
    password_field = (By.XPATH, "//input[@name='password']")
    company_field = (By.XPATH, "//input[@name='company']")
    website_field = (By.XPATH, "//input[@name='website']")

    country_dropdown_menu = "//div/select[@name='country']"
    city_field = (By.XPATH, "//input[@name='city']")
    address_1_field = (By.XPATH, "//input[@name='address_line1']")
    address_2_field = (By.XPATH, "//input[@name='address_line2']")
    state_field = (By.XPATH, "//input[@id='inputState']")
    zip_code_field = (By.XPATH, "//input[@name='zip']")




