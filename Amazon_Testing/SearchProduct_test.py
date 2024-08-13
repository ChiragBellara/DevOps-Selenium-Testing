import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AmazonSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="")  # Path to the Chrome driver executable
        self.base_url = "https://amazon.in"

    def test_amazon_search_without_criteria(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        search_box = driver.find_element_by_id("twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys(Keys.RETURN)
        driver.save_screenshot('Outputs/test_amazon_search_without_criteria.png')

    def test_amazon_search_for_selenium(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        search_box = driver.find_element_by_id("twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys("Camera Tripod")
        search_box.send_keys(Keys.RETURN)
        driver.save_screenshot('Outputs/test_amazon_search_for_selenium.png')

    def test_amazon_search_with_invalid_string(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        search_box = driver.find_element_by_id("twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys("?*#^*^%")
        search_box.send_keys(Keys.RETURN)
        driver.save_screenshot('Outputs/test_amazon_search_with_invalid_string.png')
  
    def tearDown(self):
        self.driver.close()
