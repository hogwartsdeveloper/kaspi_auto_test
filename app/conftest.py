import time

import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="function")
def browser():
    time.sleep(5)
    browser = webdriver.Remote('http://selenium:4444/wd/hub', options=webdriver.ChromeOptions())
    # service = Service("app/drivers/geckodriver")
    # browser = webdriver.Firefox(service=service)
    print("[INFO] start Chrome for test")

    yield browser
    print("[INFO] quite browser")
    browser.quit()
