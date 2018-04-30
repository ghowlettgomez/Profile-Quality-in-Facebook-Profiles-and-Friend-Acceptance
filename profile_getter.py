from selenium import webdriver
from selenium.webdriver.common.keys import Keys

""" Accesses a user's facebook profile
	Note that selenium requires geckodriver 
	to be added to PATH. Geckdriver can be 
	downloaded here: 
	https://github.com/mozilla/geckodriver/releases
"""
class FB_Profile_Driver():
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.browser = webdriver.Firefox()

	def enter_Facebook(self):
		self.browser.get('https://www.facebook.com/')
		email = self.browser.find_element_by_id('email')
		email.send_keys(self.username)
		elem = self.browser.find_element_by_id('pass')
		elem.send_keys(self.password)
		elem.send_keys(Keys.RETURN)
		self.browser.close()

f = FB_Profile_Driver('email', 'password')
f.enter_Facebook()
