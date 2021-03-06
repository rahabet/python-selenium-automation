from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartEmpty(Page):
    RESULT_MESSAGE = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")

    def verify_cart_empty(self, search_word):
        self.verify_text(search_word, *self.RESULT_MESSAGE)
