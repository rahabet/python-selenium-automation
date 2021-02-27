from selenium.webdriver.common.by import By
from behave import given, then


PRODUCTS = (By.XPATH, '//li[@class="s-result-item" and .//span[contains(@class, "prime-price")]]/div')
PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')

@given('Open wholefoods page from amazon website')
def open_url(context):
    context.driver.get("https://www.amazon.com/wholefoodsdeals")


@then('Verify that wholefoods products has a name and Regular text')
def verify_product(context):
    products = context.driver.find_elements(*PRODUCTS)
    for e in products:
        assert 'Regular' in e.text, f'Error...'
        prod_name = e.find_element(*PRODUCT_NAME).text
        assert prod_name, f'Error...'





