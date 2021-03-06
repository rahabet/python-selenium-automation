from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.cart_empty_page import CartEmpty
from pages.product_selection_page import ProductSelection

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_empty_page = CartEmpty(self.driver)
        self.product_selection_page = ProductSelection(self.driver)

