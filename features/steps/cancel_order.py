from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.ID,'helpsearch')
RESULTS_FOUND_MESSAGE = (By.XPATH,"//div[@id='totalSearchResults']/preceding::p/b")

@given('Open what can i help you with page from amazon website')
def open_amazon_cancel_order(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Enter {search_query} into search field')
def input_search(context, search_query):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_query)
    search.send_keys(Keys.ENTER)
    sleep(1)
# @when('Press Enter Key')
# def press_enter(context):
#     context.driver.find_element(*SEARCH_INPUT, Keys.ENTER)
#     sleep(1)
@then('result for {search_query} should be displayed')
def verify_result_found(context, search_query):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_query in results_msg, "Expected word '{}' in message, but got '{}'".format(search_query, results_msg)



