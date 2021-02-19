from selenium.webdriver.common.by import By
from behave import given, then, when
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_POPUP = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')

@when('Click on sign in from popup')
def sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable((SIGN_IN_POPUP)))
    e.click()

@then('Verify that sign in page opens')
def verify_popup(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
                        f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin')
