import pytest
from selenium import webdriver


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
        browser = webdriver.Firefox()
        print("[INFO] start Firefox for test")
    else:
        raise pytest.UsageError("[ERROR] --browser should be chrome or firefox")

    yield browser
    print("[INFO] quite browser")
    browser.quit()
