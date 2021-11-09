import allure
from pages.main_page import MainPage


url = "https://kaspi.kz/"


@allure.feature("Проверка главной страницы")
class TestMainPage:
    @allure.story("Проверка гость видить главную страницу")
    def test_guest_should_see_main_page(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.confirm_region()
        page.should_be_main_page()

    @allure.story("Проверка гость видить модальное окно для подверждения местоположения")
    def test_guest_see_confirm_region_modal_window(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.should_be_confirm_region_modal_window()

    @allure.story("Проверка гость подверждает местоположения")
    def test_guest_confirm_region(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.get_confirm_region()
        page.confirm_region()
        page.should_be_selected_region()

    @allure.story("Проверка гость не подверждает местоположения")
    def test_guest_not_confirm_region(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.not_confirm_region()
        page.should_not_be_selected_region()
