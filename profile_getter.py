from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random 

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

	"""Given the url of a participant in the study, return a friend of theirs"""
	def run(self, friend_url):
		friends_list = self.access_friends_of_profile()
		self.access_friend(friends_list)

	""" Enters a user's facebook profile"""
	def access_profile(self):
		ffprofile = webdriver.FirefoxProfile()
		ffprofile.set_preference("dom.webnotifications.enabled", False)
		self.browser = webdriver.Firefox(ffprofile)
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

	""" Accesses the friends of a given profile"""
	def access_friends_of_profile(self, friend_url):
		self.browser.get(friend_url + '/friends')
		friends = set()
		friends_len = 0
		while True:
			friends |= set(self.browser.find_elements_by_class_name('_698'))
			if len(friends) == friends_len:
				return list(friends)
			friends_len = len(friends)
			self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			sleep(2)

	"""Given a list of friends, access the profile of a random friend"""
	def access_friend(self, friends_list):
		num_friends = len(friends_list)



f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')
f.access_friends_of_profile('https://www.facebook.com/greg.hg.3')
