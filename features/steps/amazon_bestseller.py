from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BESTSELLER_TABS = (By.XPATH, "//div[@id='zg_tabs']//a")
BESTSELLER_TEXT = (By.CSS_SELECTOR, 'div#zg_banner_text_wrapper')


@given('Open amazon bestseller page')
def open_bestseller(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then('Verify {expected_count} links are there displayed in the header')
def verify_bestseller_links(context, expected_count):
    actual_count = len(context.driver.find_elements(*BESTSELLER_TABS))
    assert int(expected_count) == actual_count, f'Expected {expected_count}, but only got {actual_count}'


@then('Verify each link has opened and content is visible')
def click_and_verify_links(context):
    links = context.driver.wait.until(EC.visibility_of_all_elements_located(BESTSELLER_TABS))    #
    for link in links:
        print(link.text)
        link.click()
        sleep(2)
        result_msg = context.driver.wait.until(EC.presence_of_element_located(BESTSELLER_TEXT)).text
  





