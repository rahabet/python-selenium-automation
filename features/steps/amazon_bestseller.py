from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLER_TABS = (By.XPATH, "//div[@id='zg_tabs']//a")

@given('Open amazon bestseller page')
def open_bestseller(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")

@then('Verify {expected_count} links are there displayed in the header')
def verify_bestseller_links(context, expected_count):
    actual_count = (len(context.driver.find_elements(*BESTSELLER_TABS)))
    assert int(expected_count) == actual_count, f'Expected {expected_count}, but only got {actual_count}'

