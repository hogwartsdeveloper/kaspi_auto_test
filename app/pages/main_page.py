from pages.base_page import BasePage
from pages.resourses.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.confirm_region_title = None

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

    def should_be_confirm_region_modal_window(self):
        assert self.is_element_present(*MainPageLocators.TITLE_REGION_CONFIRM), \
            "Region confirm modal window is not present"

    def confirm_region(self):
        button = self.browser.find_element(*MainPageLocators.BUTTON_REGION_CONFIRM)
        button.click()

    def not_confirm_region(self):
        button = self.browser.find_element(*MainPageLocators.BUTTON_REGION_NOT_CONFIRM)
        button.click()

    def get_confirm_region(self):
        title_region = self.browser.find_element(*MainPageLocators.TITLE_REGION_CONFIRM)
        region = title_region.text[10:-1]
        self.confirm_region_title = region

    def should_be_selected_region(self):
        selected_region = self.browser.find_element(*MainPageLocators.REGION)

        assert self.confirm_region_title == selected_region.text, \
            f"Wrong region, got {selected_region.text} instead of {self.confirm_region_title}"

    def should_not_be_selected_region(self):
        assert self.is_not_element_present(*MainPageLocators.REGION), \
            "Selected region is present"
