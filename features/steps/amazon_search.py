# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
# SUBMIT_BUTTON = (By.ID, 'nav-search-submit-button')
# RESULTS_FOUND_MESSAGE = (By.XPATH, "//div [@id = 'nav-subnav' ] //a[contains(@href, '/books-used-books-textbooks/b')]")
#
#
# @given('Open Amazon website')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
#
# @when('Enter {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)
#
#
# @when('Click on search')
# def click_search_icon(context):
#     context.driver.find_element(*SUBMIT_BUTTON).click()
#     sleep(1)
#
#
# @then('Results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
#     assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)
#
#
#
