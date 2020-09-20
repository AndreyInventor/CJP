from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import email, password
import time
import random
import math
import csv
from selenium.common.exceptions import NoSuchElementException

class CJBot():

	def __init__(self, email, passowrd):
		
		self.email = email
		self.password = password
		self.browser = webdriver.Chrome('chromedriver\chromedriver')

	def close_browser(self):
		
		self.browser.close()
		self.browser.quit()

	def login(self):

		browser = self.browser
		
		browser.get('https://candyjar.io/en/auth')
		time.sleep(random.randrange(3, 5))

		email_input = browser.find_element_by_xpath('/html/body/div/div/div[3]/form/div[1]/input')
		email_input.clear()
		email_input.send_keys(email)

		time.sleep(2)

		password_input = browser.find_element_by_xpath('/html/body/div/div/div[3]/form/div[2]/div[1]/input')
		password_input.clear()
		password_input.send_keys(password)

		password_input.send_keys(Keys.ENTER)
		time.sleep(3)

	def parsing(self, url, file_name):

		PEOPLE_PER_PAGE = 25

		browser = self.browser
		
		browser.get(url)
		time.sleep(random.randrange(3, 5))

		people_count = int(browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[1]').text.split(" ")[-1])
		pages_count = int(math.ceil(people_count / PEOPLE_PER_PAGE))

		split_url = url.split("/")
		
		user_emails = {}
		# Outer cycle through the pages of the search result
		for i in range(pages_count):
			#print(f'Cur page = {i+1}')
			cur_page_url = split_url[0]+'/'+split_url[1]+'/'+split_url[2]+'/'+split_url[3]+'/'+split_url[4]+'/'+split_url[5]+'/'+str(i+1)+'/'+split_url[7]
			browser.get(cur_page_url)
			people_cards = len(browser.find_elements_by_class_name('card'))
			
			# Inner cycle through the resulst of current page
			for j in range(people_cards):
				#/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[ (j+1) ] - current people card
				#/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[ (j+1) ]/div[1]/div/div[2] - current user name
				#/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[ (j+1) ]/div[2]/div/div[1]/div[2]/div - current user email
				user_name_xpath = '/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[' + str(j+1) + ']/div[1]/div/div[2]'
				if(len(browser.find_elements_by_xpath(user_name_xpath)) != 0):
					user_name = browser.find_elements_by_xpath(user_name_xpath)[0].text
				
				user_name = 'NONAME' + str(i*PEOPLE_PER_PAGE+j+1) if user_name == '' else user_name
				
				user_email_xpath = '/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[' + str(j+1) + ']/div[2]/div/div[1]/div[2]/div'
				if(len(browser.find_elements_by_xpath(user_email_xpath)) != 0):
					user_email = browser.find_elements_by_xpath(user_email_xpath)[0].get_attribute('data-template')
				else:
					user_email = 'NOEMAIL' + str(i*PEOPLE_PER_PAGE+j+1)
				
				user_emails[user_email] = user_name
				#print(f'{user_email};{user_name}')
		
		# Write parsing data to file
		with open(file_name + '.csv', 'w', encoding='utf-8') as file:
			for key, val in user_emails.items():
				file.write(key + ';' + val + '\n')

my_bot = CJBot(email, password)
my_bot.login()
time.sleep(3)
my_bot.parsing('https://candyjar.io/search/vacancy/5420/1/W1sicG9zdGdyZXNxbCJdLFtdLCIiLFtdXQ==', 'Belarus-Ruby-Postgresql-262')
my_bot.close_browser()
