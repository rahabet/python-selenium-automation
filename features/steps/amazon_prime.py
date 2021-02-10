from selenium.webdriver.common.by import By
from behave import Given, Then
from time import sleep

BENEFIT_BOX= (By.CSS_SELECTOR,'.benefit-box')

@Given('Open amazon prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')

@Then('Verify {box_count} benefit boxes are displayed')
def verify_benefit_box(context, box_count):
    actual_boxes = (context.driver.find_elements(*BENEFIT_BOX))
    assert len(actual_boxes) == int(box_count), f'expected {box_count} but get {len(actual_boxes)}'
