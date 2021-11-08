import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox',
                     help="Choose brower: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser')
    browser = None

    if browser_name == "chrome":
        browser = webdriver.Chrome()
        print("[INFO] start Chrome for test")
    elif browser_name == "firefox":
        current_dir = os.path.abspath(os.path.dirname(__file__))
        geckodriver = os.path.join(current_dir, "drivers/geckodriver")
        service = Service(geckodriver)
        browser = webdriver.Firefox(service=service)
        print("[INFO] start Firefox for test")
    else:
        raise pytest.UsageError("[ERROR] --browser should be chrome or firefox")

    yield browser
    print("[INFO] quite browser")
    browser.quit()
