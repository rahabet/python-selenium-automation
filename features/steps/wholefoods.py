from selenium.webdriver.common.by import By
from behave import given, then

PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')
REGULAR_TEXT = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__regular-price')

@given('Open wholefoods page from amazon website')
def open_url(context):
    context.driver.get("https://www.amazon.com/wholefoodsdeals")


@then('Verify {expec_count}wholefoods products has a name and Regular text')
def verify_product(context, expec_count):
    pro_count = len(context.driver.find_elements(*PRODUCT_NAME))
    reg_count = len(context.driver.find_elements(*REGULAR_TEXT))

    assert int(expec_count) == pro_count and int(expec_count) == reg_count, \
        f'expected {expec_count} but got {pro_count} for products with product name' \
        f' and {reg_count} for text with Regular' \


