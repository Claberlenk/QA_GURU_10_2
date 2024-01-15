from selene import browser, be, have
import pytest

@pytest.fixture
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
    browser.quit()

def test_google_request(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_not_info(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('-info').press_enter()
    browser.element('[id=botstuff] [role=heading]').should(have.text('По запросу -info ничего не найдено.'))
