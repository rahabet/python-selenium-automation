from selenium.webdriver.common.by import By
from behave import given,when, then,step
from time import sleep

HAM_MENU= (By.ID, 'nav-hamburger-menu')

@then('Verify hamburger menu icon is visible')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU)
    