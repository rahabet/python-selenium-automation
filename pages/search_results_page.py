from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):

    RESULTS_FOUND_MESSAGE = (By.XPATH, "//span[@class = 'a-color-state a-text-bold']")

    def verify_search_result(self, result_word):
        self.verify_text(result_word, *self.RESULTS_FOUND_MESSAGE)
        # results_msg = self.driver.find_element(*self.RESULTS_FOUND_MESSAGE).text
        # assert result_word in results_msg, "Expected word '{}' in message, but got '{}'".format(result_word, results_msg)
