from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon webpage')
def open_amazon_url(context):
    context.app.main_page.open_main_page()


@when('Click on cart icon')
def click_cart(context):
    context.app.main_page.click_cart_icon()


@then('A message {search_word} should be displayed')
def verify_result(context, search_word):
    context.app.cart_empty_page.verify_cart_empty(search_word)
