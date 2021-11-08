import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    print("[INFO] start Chrome for test")

    yield browser
    print("[INFO] quite browser")
    browser.quit()
