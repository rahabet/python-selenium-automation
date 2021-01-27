from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
driver.get('https://www.amazon.com')
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Watches')
driver.find_element(By.ID, 'nav-search-submit-button').click()

actual_text = driver.find_element_by_xpath("//span[@class= 'a-color-state a-text-bold']").text
expected_text = '"Watches"'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()
