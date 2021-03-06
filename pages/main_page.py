from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SUBMIT_BUTTON = (By.ID, 'nav-search-submit-button')
    ORDER_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    CART_ICON = (By.ID, "nav-cart-count")
    PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def open_main_page(self):
        self.open_page('https://www.amazon.com')

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)

    def click_search_icon(self):
        self.click(*self.SUBMIT_BUTTON)

    def click_link(self):
        self.click(*self.ORDER_LINK)

    # def click_cart_icon(self):
    #     self.click(*self.CART_ICON)

    def product_click(self):
        self.click(*self.PRODUCT_RESULT)




