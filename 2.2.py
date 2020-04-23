import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/selects2.html')

num1 = driver.find_element_by_id('num1')
first = num1.text
num2 = driver.find_element_by_id('num2')
second = num2.text
sum1 = int(first) + int(second)

result = Select(driver.find_element_by_xpath("//select[@id='dropdown']"))
result.select_by_visible_text(str(sum1))
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.quit()
