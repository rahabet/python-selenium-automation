from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "h1.a-spacing-small")

    def verify_sign_in_page_opened(self, result_word):
        self.verify_text(result_word, *self.SIGN_IN_TEXT)


