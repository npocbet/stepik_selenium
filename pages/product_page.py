from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_correct_value_in_the_allert(self):
        self.should_be_buscet_button()
        self.click_to_add_to_buscet_button()

    def should_be_buscet_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BUSCET_BUTTON), "Add button is not presented"

    def click_to_add_to_buscet_button(self):
        addButton = self.get_element(*ProductPageLocators.ADD_TO_BUSCET_BUTTON)
        if addButton:
            addButton.click()

    def check_product_name_in_the_buscet(self):
        item_name_added_to_buscet = self.get_element(*ProductPageLocators.ITEM_NAME_MESSAGE).text
        item_name_added_to_buscet = item_name_added_to_buscet[
                                    :item_name_added_to_buscet.find(' has been added to your basket.')]
        item_name = self.get_element(*ProductPageLocators.ITEM_NAME).text
        assert item_name_added_to_buscet == item_name, "There is a difference between item name and " \
                                                       "item name added to buscet"

    def check_product_price_in_the_buscet(self):
        item_price_added_to_buscet = self.get_element(*ProductPageLocators.ITEM_PRICE_MESSAGE).text
        item_price = self.get_element(*ProductPageLocators.ITEM_PRICE).text
        assert item_price_added_to_buscet == item_price, "There is a difference between item price and " \
                                                         "price of added to buscet"
