from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('TraBAGhanap Seekers', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Register Form', headerText)
		inpDets = self.browser.find_element_by_id('FullName')
		inpDets1 = self.browser.find_element_by_id('Email')
		inpDets2 = self.browser.find_element_by_id('PhoneNumber')
		inpDets3 = self.browser.find_element_by_id('Gender')
		inpDets4 = self.browser.find_element_by_id('Age')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(inpDets.get_attribute('placeholder'),'Enter your name here.')
		inpDets.click()
		inpDets.send_keys('Jhonny Smith')
		time.sleep(1)
		inpDets1.send_keys('jhonnymail@hotmail.com')
		time.sleep(1)
		inpDets2.send_keys('12334567891')
		time.sleep(1)
		inpDets3.send_keys('Male')
		time.sleep(1)
		inpDets4.send_keys('35')
		time.sleep(1)

		btn_button.click()
		time.sleep(1)
		self.checking_if_in_table_list('1: Jhonny Smith jhonnymail@hotmail.com 12334567891 Male 35')

	def test_another_input(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('TraBAGhanap Seekers', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Register Form', headerText)
		inpDets = self.browser.find_element_by_id('FullName')
		inpDets1 = self.browser.find_element_by_id('Email')
		inpDets2 = self.browser.find_element_by_id('PhoneNumber')
		inpDets3 = self.browser.find_element_by_id('Gender')
		inpDets4 = self.browser.find_element_by_id('Age')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(inpDets.get_attribute('placeholder'),'Enter your name here.')
		inpDets.click()
		inpDets.send_keys('LucasMarcus')
		time.sleep(1)
		inpDets1.send_keys('marcusl@hotmail.com')
		time.sleep(1)
		inpDets2.send_keys('19860452390')
		time.sleep(1)
		inpDets3.send_keys('Male')
		time.sleep(1)
		inpDets4.send_keys('28')
		time.sleep(1)

		btn_button.click()
		time.sleep(1)
		self.checking_if_in_table_list('1: LucasMarcus marcusl@hotmail.com 19860452390 Male 28')

	def checking_if_in_table_list(self,row_text):
		'''def checking_if_in_table_list(self,row_test):
								save_time =time.time()
								while time.time()-save_time<CWAIT:
									time.sleep(0.5)
									try:'''
		table = self.browser.find_element_by_id('SignUp')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])
				'''return
															except (AssertionError,aywala) as e:
																if time.time()-save_time>CWAIT:
																	raise e'''
				time.sleep(1)
if __name__ == '__main__':
	unittest.main(warnings='ignore')
