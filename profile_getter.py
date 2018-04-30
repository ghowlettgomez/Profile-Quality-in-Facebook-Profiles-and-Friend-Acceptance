from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

""" Accesses a user's facebook profile
	Note that selenium requires geckodriver 
	to be added to PATH. Geckdriver can be 
	downloaded here: 
	https://github.com/mozilla/geckodriver/releases
"""
class FB_Profile_Driver():
	""" Note that to access a user's friends list,
		we need to enter a facebook account
	"""
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.access_profile()

	""" Enters a user's facebook profile"""
	def access_profile(self):
		self.browser = webdriver.Firefox()
		self.browser.get('https://www.facebook.com/')
		sleep(1)
		username_input = self.browser.find_element_by_id('email')
		username_input.send_keys(self.username)
		sleep(1)
		password_input = self.browser.find_element_by_id('pass')
		password_input.send_keys(self.password)
		login_input = self.browser.find_element_by_id('loginbutton')
		login_input.click()
		sleep(1)

	""" Accesses friends, assumes access_profile already called"""
	def access_friend(self):
		profile_link = self.browser.find_element_by_id('findFriendsNav')


f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')
