import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_binding():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.driver.maximize_window()
    # browser.config.window_width = 1920
    # browser.config.window_height = 1080

    yield browser

    browser.quit()
