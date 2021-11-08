from pages.main_page import MainPage


url = "https://kaspi.kz/"


class TestMainPage:
    def test_guest_should_see_main_page(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.confirm_region()
        page.should_be_main_page()

    def test_guest_see_confirm_region_modal_window(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.should_be_confirm_region_modal_window()

    def test_guest_confirm_region(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.get_confirm_region()
        page.confirm_region()
        page.should_be_selected_region()
