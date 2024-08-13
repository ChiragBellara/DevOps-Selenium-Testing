import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AmazonSearchTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path="")	# Path to the chrome driver executable
		self.base_url = "https://amazon.in"

	def test_amazon_loading_page(self):
		driver = self.driver
		driver.maximize_window()
		driver.get(self.base_url)
		driver.save_screenshot('Outputs/test_amazon_loading_page.png')

	def test_amazon_todays_deals(self):
		driver = self.driver
		driver.get(self.base_url)
		driver.maximize_window()
		todays_deals_box = driver.find_element_by_link_text("Today's Deals")
		todays_deals_box.send_keys(Keys.RETURN)
		timeout=10
		element_present = EC.presence_of_element_located((By.ID, '101 5ad664d8-announce'))
		WebDriverWait(driver, timeout).until(element_present)
		driver.save_screenshot('Outputs/test_amazon_todays_deals.png')

	def tearDown(self):
		self.driver.close()