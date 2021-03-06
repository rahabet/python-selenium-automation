from selenium.webdriver.common.by import By
from behave import given, when, then


@when("Click Amazon Orders link")
def click_order_link(context):
    context.app.main_page.click_link()


@then("Verify {result_word} page is opened")
def verify_sign_in_page_opened(context, result_word):
    context.app.sign_in_page.verify_sign_in_page_opened(result_word)


# session deleted because of page crash
# from unknown error: cannot determine loading status
# from tab crashed