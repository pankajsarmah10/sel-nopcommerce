from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.............")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.............")
    else:
        driver = webdriver.Safari()
    return driver


def pytest_addoption(parser): #This will get the value from the CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the Browser value to the setup method
    return request.config.getoption("--browser")

################## Pytest Html Report ##################
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'nopCommerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['QA'] = 'Pankaj'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
