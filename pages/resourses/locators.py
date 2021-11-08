from selenium.webdriver.common.by import By


class MainPageLocators:
    SHOP_CATEGORIES = (By.CSS_SELECTOR, "div.shop-categories")
    PAYMENTS = (By.CLASS_NAME, "payments__items")
    KASPI_RED_MENU = (By.CSS_SELECTOR, ".kaspiRedMenu._clearfix")
    KASPI_GUIDE_BLOCK = (By.CSS_SELECTOR, "div.kaspiGuide-desk-videoTutorBlock")
