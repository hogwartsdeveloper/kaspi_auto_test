from pages.base_page import BasePage
from pages.resourses.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_main_page(self):
        self.should_be_kaspi_shop()
        self.should_be_kaspi_payments()
        self.should_be_kaspi_red_menu()
        self.should_be_kaspi_guide_block()

    def should_be_kaspi_shop(self):
        assert self.is_element_present(*MainPageLocators.SHOP_CATEGORIES), \
            "Kaspi Shop is not present"

    def should_be_kaspi_payments(self):
        assert self.is_element_present(*MainPageLocators.PAYMENTS), \
            "Kaspi Payments is not present"

    def should_be_kaspi_red_menu(self):
        assert self.is_element_present(*MainPageLocators.KASPI_RED_MENU), \
            "Kaspi red menu is not present"

    def should_be_kaspi_guide_block(self):
        assert self.is_element_present(*MainPageLocators.KASPI_GUIDE_BLOCK), \
            "Kaspi guide block is not present"
