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
	def run(self, profile_url):
		friends_list = self.access_friends_of_profile(profile_url)
		friend_body_html = self.access_friend(friends_list)
		self.load_body_html(friend_body_html)

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
	def access_friends_of_profile(self, profile_url):
		self.browser.get(profile_url + '/friends')
		friends = set()
		friends_len = 0
		while True:
			friends |= set(self.browser.find_elements_by_xpath("//div[@class='fsl fwb fcb']"))
			if len(friends) == friends_len:
				return list(friends)
			friends_len = len(friends)
			self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			sleep(2)

	"""Given a list of friends, access the profile of a random friend
		and get the inner html of the body.
	"""
	def access_friend(self, friends_list):
		num_friends = len(friends_list)
		random_int = random.randint(0, num_friends)
		random_friend = friends_list[random_int]
		random_friend.find_element_by_tag_name("a").click()
		return self.browser.execute_script("return document.body.innerHTML")


	"""Given the inner html of the body, load that html"""
	def load_body_html(self, body_html):
		self.browser.execute_script("document.body.innerHTML = '" + body_html.replace("'", r"\'") + "'")

f = FB_Profile_Driver('cs232facebook@gmail.com', 'Facebook1!')
f.run('https://www.facebook.com/greg.hg.3')
