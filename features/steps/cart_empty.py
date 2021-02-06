from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.ID,"nav-cart-count")
RESULT_MESSAGE = (By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty")

@given('Open Amazon webpage')
def open_amazon_url(context):
    context.driver.get("https://www.amazon.com")

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(1)

@then('A message your amazon cart is empty should be displayed')
def verify_result(context):
    expected_text = 'Your Amazon Cart is empty'
    actual_text = context.driver.find_element(*RESULT_MESSAGE).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'