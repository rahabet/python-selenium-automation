from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ProductSelection(Page):
    CART = (By.ID, 'nav-cart-count')
    SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
    SELECT_SIZE = (By.ID, 'dropdown_selected_size_name')
    SIZE_SELECTED = (By.ID, 'size_name_1')
    BUY_NOW_BUTTON = (By.ID, 'buy-now-button')
    ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')

    def select_product(self):
        self.click(*self.ADD_CART_BUTTON)
        if len(self.find_elements(*self.SIZE_TOOLTIP)) == 1:
            self.click(*self.SELECT_SIZE)
            self.click(*self.SIZE_SELECTED)
            self.wait_for_element_click(*self.BUY_NOW_BUTTON)
            self.wait_for_element_click(*self.ADD_CART_BUTTON)

    def verify_cart(self, cart_result):
        self.verify_text(cart_result, *self.CART)




