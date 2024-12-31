import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities.test_data import TestData


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def load_url(self):
        self.driver.get(TestData.base_url)

    def find_element_on_page(self, *locator):
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element_on_page(*locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def enter_text_in_field(self, locator, value):
        self.click_on_element(locator)
        self.find_element_on_page(*locator).clear()
        self.find_element_on_page(*locator).send_keys(value)
        time.sleep(1)

    def get_text_in_element(self, locator):
        return self.find_element_on_page(*locator).text
