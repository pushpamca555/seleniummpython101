import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from Utilities.test_data import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()

    request.cls.driver = driver
    # Load the AUT
    driver.get(TestData.base_url)
    driver.maximize_window()
    # transfer control to the test scripts
    yield
    driver.close()


# 1st Step: Declare Variables For Setting Up LambdaTest
user_name = "pranav_naik"
access_token = "TIip2A6dnYX0RVdW3jMAYtNNFr7O9ZWXljPMQbtrS0QbqqefWW"
remote_url = "http://" + user_name + ":" + access_token + "@hub.lambdatest.com/wd/hub"

# 2nd Step: Define The Desired Capabilities (3 Caps)
chrome_caps = {
    "build": "1.0",
    "name": "LambdaTest Grid On Chrome and Windows 10",
    "platform": "Windows 10",
    "browserName": "Chrome",
    "version": "88.0",
    "visual": True,
    "video": True,
    "network": True,
    "console": True
}

edge_caps = {
    "build": "2.0",
    "name": "LambdaTest Grid On Edge and macOS Sierra",
    "platform": "macOS Sierra",
    "browserName": "Edge",
    "version": "87.0",
    "visual": True,
    "video": True,
    "network": True,
    "console": True
}

firefox_caps = {
    "build": "3.0",
    "name": "LambdaTest Grid On Firefox and Windows 7",
    "platform": "Windows 7",
    "browserName": "Firefox",
    "version": "82.0",
    "visual": True,
    "video": True,
    "network": True,
    "console": True
}

ie_caps = {
    "build": "4.0",
    "name": "LambdaTest Grid On Internet Explorer and Windows 10",
    "platform": "Windows 10",
    "browserName": "Internet Explorer",
    "version": "11.0",
    "visual": True,
    "video": True,
    "network": True,
    "console": True
}


# 3rd Step: Connect To LambdaTest Using A Fixture & RemoteConnection
@pytest.fixture(params=["chrome", "firefox", "edge", "ie"])
def driver_initialization(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("LT:Options", chrome_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            options=chrome_options
        )
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_capability("LT:Options", firefox_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            options=firefox_options
        )
    elif request.param == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.set_capability("LT:Options", edge_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            options=edge_options
        )
    elif request.param == "ie":
        ie_options = webdriver.IeOptions()
        ie_options.set_capability("LT:Options", ie_caps)
        driver = webdriver.Remote(
            command_executor=RemoteConnection(remote_url),
            options=ie_options
        )
    request.cls.driver = driver
    driver.get(TestData.base_url)
    driver.maximize_window()
    yield
    driver.close()
