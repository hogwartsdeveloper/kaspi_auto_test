from selenium.webdriver.common.by import By


class MainPageLocators:
    SHOP_CATEGORIES = (By.CSS_SELECTOR, "div.shop-categories")
    PAYMENTS = (By.CLASS_NAME, "payments__items")
    KASPI_RED_MENU = (By.CSS_SELECTOR, ".kaspiRedMenu._clearfix")
    KASPI_GUIDE_BLOCK = (By.CSS_SELECTOR, "div.kaspiGuide-desk-videoTutorBlock")

    TITLE_REGION_CONFIRM = (By.CLASS_NAME, "headerRegionConfirm__title")
    BUTTON_REGION_CONFIRM = (By.ID, "headerRegionConfirm__ConfirmButton")
    BUTTON_REGION_NOT_CONFIRM = (By.ID, "headerRegionConfirm__CancelButton")

    REGION = (By.ID, "headerRegionId")
