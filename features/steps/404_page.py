from selenium.webdriver.common.by import By
from behave import given, then, when
from selenium.webdriver.support import expected_conditions as EC

DOG_IMG = (By.CSS_SELECTOR, 'a[href="/dogsofamazon"] img')


@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle

@when('Click to open blog')
def open_blog(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to the newly opened window')
def open_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    # print(context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then('User can close new window and switch back to original window')
def switch_to_original_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)


