import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.driver_name = 'firefox'
    #browser.config.driver_options = webdriver.FirefoxOptions()
    #browser.config.window_height = 1920
    #browser.config.window_width = 1080
    #browser.config.driver_options.add_argument('--headless')



    yield

    browser.quit()