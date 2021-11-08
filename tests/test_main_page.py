import pytest
from pages.main_page import MainPage


url = "https://kaspi.kz/"


class TestMainPage:
    def test_guest_should_see_main_page(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.should_be_main_page()
