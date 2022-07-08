from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

CWAIT = 6
class User_Test(LiveServerTestCase):


#class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def checking_if_in_table_list(self,row_test):
		timing =time.time()
		while time.time()-timing<CWAIT:
			time.sleep(0.5)
			try:
				table = self.browser.find_element_by_id('SignUp')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_test,[row.text for row in rows])
				return
			except (AssertionError,sakin) as e:
				if time.time()-timing>CWAIT:
					raise e
				time.sleep(1)
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get(self.live_server_url)
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
		self.assertEqual(inpDets1.get_attribute('placeholder'),'Enter your email here.')
		self.assertEqual(inpDets2.get_attribute('placeholder'),'Enter your phone number.')
		self.assertEqual(inpDets3.get_attribute('placeholder'),'Enter your gender.')
		self.assertEqual(inpDets4.get_attribute('placeholder'),'Enter your age.')
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
		inpDets = self.browser.find_element_by_id('FullName')
		inpDets1 = self.browser.find_element_by_id('Email')
		inpDets2 = self.browser.find_element_by_id('PhoneNumber')
		inpDets3 = self.browser.find_element_by_id('Gender')
		inpDets4 = self.browser.find_element_by_id('Age')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(inpDets.get_attribute('placeholder'),'Enter your name here.')
		self.assertEqual(inpDets1.get_attribute('placeholder'),'Enter your email here.')
		self.assertEqual(inpDets2.get_attribute('placeholder'),'Enter your phone number.')
		self.assertEqual(inpDets3.get_attribute('placeholder'),'Enter your gender.')
		self.assertEqual(inpDets4.get_attribute('placeholder'),'Enter your age.')
		inpDets.click()
		inpDets.send_keys('JohnCarlo')
		time.sleep(1)
		inpDets1.send_keys('johncarlo@rocketmail.com')
		time.sleep(1)
		inpDets2.send_keys('14356782804')
		time.sleep(1)
		inpDets3.send_keys('Male')
		time.sleep(1)
		inpDets4.send_keys('23')
		time.sleep(1)

		btn_button.click()
		time.sleep(1)
		self.checking_if_in_table_list('1: Jhonny Smith jhonnymail@hotmail.com 12334567891 Male 35')
		self.checking_if_in_table_list('2: JohnCarlo johncarlo@rocketmail.com 14356782804 Male 23')


	def test_another_input(self):
		self.browser.get(self.live_server_url)
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
		self.assertEqual(inpDets1.get_attribute('placeholder'),'Enter your email here.')
		self.assertEqual(inpDets2.get_attribute('placeholder'),'Enter your phone number.')
		self.assertEqual(inpDets3.get_attribute('placeholder'),'Enter your gender.')
		self.assertEqual(inpDets4.get_attribute('placeholder'),'Enter your age.')
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
		