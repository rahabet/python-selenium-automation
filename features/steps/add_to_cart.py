from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SELECT_SIZE = (By.ID, 'dropdown_selected_size_name')
SIZE_SELECTED = (By.ID, 'size_name_0')
BUY_NOW_BUTTON = (By.ID, 'buy-now-button')

@when('Search for a {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)


@when('Click on the first product')
def first_product(context):
    context.driver.find_element(*PRODUCT_RESULT).click()


@when('Click on add to cart button')
def add_cart(context):
    context.driver.find_element(*ADD_CART_BUTTON).click()
    if len(context.driver.find_elements(*SIZE_TOOLTIP)) == 1:
        context.driver.find_element(*SELECT_SIZE).click()
        context.driver.find_element(*SIZE_SELECTED).click()
        # sleep(2)
        # context.driver.find_element(*ADD_CART_BUTTON).click()
        context.driver.wait.until(EC.element_to_be_clickable((BUY_NOW_BUTTON)))
        e = context.driver.wait.until(EC.element_to_be_clickable((ADD_CART_BUTTON)))
        e.click()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expected {expected_count} but got {cart_count}'