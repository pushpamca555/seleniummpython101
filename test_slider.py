from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Tests.common_tests import CommonTests
from Utilities.test_data import TestData
import time


class TestScenario2(CommonTests):
    def test_slider(self):
        # We can use ActionChains to automate the drag and drop scenario
        base_page = BasePage(self.driver)

        base_page.click_on_element(TestData.drag_and_drop_slider_link)

        time.sleep(5)

        # Locate the slider
        slider = base_page.driver.find_element(By.XPATH, TestData.default_value_15_slider)

        current_position = int(base_page.get_text_in_element(TestData.slider_value_output))  ##15
        target_position = 95

        # x-axis offset value to move the slider to 95
        offset = 215

        actions = ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()

        actual_slider_value = base_page.get_text_in_element(TestData.slider_value_output)

        assert int(actual_slider_value) == target_position, \
            "Actual Slider Value {} does not match Expected Value {}!".format(
                actual_slider_value, target_position
            )
