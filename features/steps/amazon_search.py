from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SUBMIT_BUTTON = (By.ID, 'nav-search-submit-button')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//span[@class = 'a-color-state a-text-bold']")


@when('Enter {search_word} into search field')
def input_search(context, search_word):
    context.app.main_page.input_search(search_word)



@when('Click on search')
def click_search_icon(context):
    context.app.main_page.click_search_icon()


@then('Results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.search_results_page.verify_search_result(search_word)



