from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

CLICK_LINK = (By.XPATH, "//a[text()='Amazon applications']")
SEND_LINK_BUTTON = (By.CSS_SELECTOR, 'span#mgt-email-sms-send-button-announce')


@given('Open the webpage for amazon application T&C page')
def open_url(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when('Click on Amazon Application link')
def click_link(context):
    context.driver.find_element(*CLICK_LINK).click()


@then('Amazon app page is opened')
def verify_app_page_opened(context):
   assert context.driver.wait.until(EC.presence_of_element_located(SEND_LINK_BUTTON)), \
       f'Error...'

