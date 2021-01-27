from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get('https://www.amazon.com/gp/help/customer/display.html ')
search_word = driver.find_element(By.ID, 'helpsearch')
search_word.send_keys("Cancel order")
search_word.send_keys(Keys.ENTER)

actual_text = driver.find_element_by_xpath("//div[@id = 'totalSearchResults']/preceding::p/b").text
expected_text = "Cancel order"

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} '

driver.quit()