# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.options import Options

# options = Options()
# options.headless = True
# options=options

driver = webdriver.Firefox()
driver.get("https://github.com")
search_field  = driver.find_element_by_name("q")
search_field.click()
search_field.send_keys("selenium")
search_field.send_keys(Keys.RETURN)
#assert "We’ve found" in driver.page_source
driver.close()