from pages.base_page import BasePage
from pages.resourses.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_main_page(self):
        self.should_be_kaspi_shop()

    def should_be_kaspi_shop(self):
        assert self.is_element_present(*MainPageLocators.SHOP_CATEGORIES), \
            "Kaspi Shop is nor present"
