from selenium.webdriver.common.by import By
from behave import given, then
CS_ELEMENTS =['//div[contains(@class, "a-section a-spacing-extra")]/h1',
              '//h2[@class="a-spacing-none a-text-normal"]',
              '//h3[contains(@class,"a-spacing-none")]',
              '//input[@id = "helpsearch"]',
              '//div[contains(@class,"a-span12")]/h1',
              '//div[@class = "csg-box-inner"]',
              '//img[@class = "csg-hb-promo"]'
              ]

# CS_ELEMENTS =[(By.XPATH, 'div[contains(@class, "a-section a-spacing-extra")]/h1'),
#               (By.XPATH, '//h2[@class="a-spacing-none a-text-normal"]'),
#               (By.XPATH, '//h3[contains(@class,"a-spacing-none")]'),
#               (By.ID, 'helpsearch'),
#               (By.XPATH, '//div[contains(@class,"a-span12")]/h1'),
#               (By.CSS_SELECTOR, 'div.csg-hover-box'),
#               (By.CSS_SELECTOR, 'img.csg-hb-promo')
#               ]

@given('Open amazon cs webpage')
def open_cs_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")
@then('Verify if the web elements are displayed')
def verify_webelemnts(context):
  for element in (CS_ELEMENTS):
      actual_element = context.driver.find_element_by_xpath(element)
      print(actual_element.is_displayed())
