import pytest
from selene import have, command
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.window_width = 1080
    browser.config.window_height = 950
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    ads.should(have.size_less_than_or_equal(3))
    ads.perform(command.js.remove)
    yield