from selenium.webdriver.common.by import By
from behave import given, then, when


COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

# @given('Open amazon {product_id} page')
# def open_url(context, product_id):
#     context.driver.get(f'https://www.amazon.com/gp/product/{product_id}')


@then('verify user can click through the jeans color')
def verify_jeans_color(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash',
                       'Light Vintage', 'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse',
                       'Rinsed Vintage', 'Vintage Light Wash', 'Washed Black']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in range(len(colors)):
        colors[color].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[color] == selected_color, f'for {expected_colors[color]}, I got the wrong color'

