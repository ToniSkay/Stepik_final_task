from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages':'en'})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
