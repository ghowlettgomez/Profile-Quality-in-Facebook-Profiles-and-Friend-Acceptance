from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from fb_module.alter_profile import HTML_Editor
from time import sleep
import io
import random
import json


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
		self.editor = HTML_Editor()

	def run_full(self, body_html, path, type):
		profile_type_list = [self.editor.returnToDefault, self.editor.returnUnchanged, self.editor.onlySidebar, self.editor.onlyPosts, self.editor.removeAllHistory]
		edited_body_html = profile_type_list[type](body_html, 'User')
		self.load_body_html(edited_body_html)
		self.take_screenshot_full(path)

	def run_small(self, body_html, path, type):
		small_html = self.editor.replaceRequests(body_html, type)
		self.load_body_html(small_html)
		self.take_screenshot_small(path)


	"""Given the url of a participant in the study, return a friend of theirs"""
	def run(self, profile_url, path, sleeptime, type):
		friends_list = self.access_friends_of_profile(profile_url)
		small_html = self.access_friend_small(friends_list,sleeptime)
		self.run_small(small_html, path, type)
		full_html = self.editor.deleteRequestDropdown(small_html)
		self.run_full(full_html, path, type)

	"""Function such that if run fails, we try again"""
	def runner(self, profile_url, path, sleeptime, type):
		self.access_profile()
		while True:
			try:
				self.run(profile_url, path, sleeptime, type)
				break
			except IndexError as err:
				if sleeptime < 5:
					print("IndexError iter " . sleeptime)
					runner(sleeptime + 1,openreqs)
				else:
					print("IndexError: {0}".format(err))
			except ValueError as err:
				if sleeptime < 5:
					print("ValueError iter " . sleeptime)
					self.runner(sleeptime + 1,openreqs)
					break
				else:
					print("ValueError: {0}".format(err))
		self.browser.close()

	""" Enters a user's facebook profile"""
	def access_profile(self):
		options = Options()
		options.add_argument('-headless')
		ffprofile = webdriver.FirefoxProfile()
		ffprofile.set_preference("dom.webnotifications.enabled", False)
		self.browser = webdriver.Firefox(ffprofile, firefox_options=options, log_path=None)
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
		#self.browser.get(profile_url.split('?')[0] + '/friends')
		self.browser.get(profile_url)
		friends_url = self.browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div[3]/div/div[2]/div[2]/ul/li[3]/a')
		friends_url.click()
		sleep(5)
		friends = set()
		friends_len = 0
		while True:
			friends |= set(self.browser.find_elements_by_xpath("//div[@class='fsl fwb fcb']"))
			if len(friends) == friends_len or friends_len > 200:
				return list(friends)
			friends_len = len(friends)
			self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			sleep(2)

	"""Given a list of friends, access the profile of a random friend
		and get the inner html of the body.
	"""
	def access_friend_small(self, friends_list, sleeptime):
		num_friends = len(friends_list)
		random_int = random.randint(0, num_friends)
		random_friend = friends_list[random_int]
		random_friend.find_element_by_tag_name("a").click()
		sleep(5*sleeptime)
		self.browser.find_element_by_name("requests").click()
		sleep(5*sleeptime)
		return self.browser.execute_script("return document.body.innerHTML")

	"""Given the inner html of the body, load that html"""
	def load_body_html(self, body_html):
		self.browser.execute_script("document.body.innerHTML = %s" % json.dumps(body_html))
		sleep(5)

	"""Takes a screenshot and saves it to given path, give 5 seconds for screen to load"""
	def take_screenshot_full(self, path):
		sleep(5)
		image = self.browser.find_element_by_xpath('/html/body').screenshot_as_png
		open(path + 'screenshot_full.png', 'wb').write(image)

	def take_screenshot_small(self, path):
		sleep (5)
		image = self.browser.find_element_by_id('01392847102938471209587012398471029384701_1_req').screenshot_as_png
		open(path + 'screenshot_small.png', 'wb').write(image)
