import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_binding():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.driver.maximize_window()

    yield browser

    browser.quit()
