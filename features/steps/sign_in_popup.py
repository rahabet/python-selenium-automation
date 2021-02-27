from selenium.webdriver.common.by import By
from behave import given, then, when
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_POPUP = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-inner')
NAV_TOOLS = (By.ID, 'nav-tools')

@when('Click on sign in from popup')
def sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable((SIGN_IN_POPUP)))
    e.click()


@then('Verify that sign in page opens')
def verify_popup(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
                        f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin')


@then('Verify Sign in is clickable')
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP))


@then('Verify that Sign in disappears')
def verify_sign_in_disappear(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_POPUP))
    context.driver.wait.until(EC.presence_of_element_located(NAV_TOOLS))

@when('Wait for {sec} sec')
def wait_sec(context, sec):
    sleep(int(sec))