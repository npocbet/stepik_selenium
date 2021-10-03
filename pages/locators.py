from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators:
    pass


class ProductPageLocators:
    ADD_TO_BUSCET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ITEM_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alert-info > .alertinner > p > strong')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
