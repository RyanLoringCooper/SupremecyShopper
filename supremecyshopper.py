from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import *

import sys, __future__, os, time

def getConfig():
	url = ""
	size = ""
	name = ""
	email = ""
	tel = ""
	address = ""
	zipCode = ""
	city = ""
	state = ""
	country = ""
	cardType = ""
	number = ""
	expMonth = ""
	expYear = ""
	CVV = ""
	
	conf = open('config.txt')
	line = conf.readline()
	while line != "":
		words = line.split()
		if len(words) > 0:
			if words[0] == 'url':
				url = words[2]
			elif words[0] == 'size':
				if(len(words) == 3):
					size = words[2]
			elif words[0] == 'name':
				name = words[2] + " " + words[3]
			elif words[0] == 'email':
				email = words[2]
			elif words[0] == 'tel':
				tel = words[2]
			elif words[0] == 'address':
				for i in range(2, len(words)):
					address = address + words[i] + " "
			elif words[0] == 'zip':
				zipCode = words[2]
			elif words[0] == 'city':
				for i in range(2, len(words)):
					city = city + words[i] + " "
			elif words[0] == 'state':
				state = words[2].upper()
			elif words[0] == 'country':
				country = words[2].upper()
			elif words[0] == 'type':
				cardType = words[2].lower()
			elif words[0] == 'number':
				number = words[2]
			elif words[0] == 'expMonth':
				expMonth = words[2]
			elif words[0] == 'expYear':
				expYear = words[2]
			elif words[0] == 'CVV':
				CVV = words[2]
		line = conf.readline()
	conf.close()
	return (url, size, name, email, tel, address, zipCode, city, state, country, cardType, number, expMonth, expYear, CVV)

if __name__ == '__main__':
	(url, size, name, email, tel, address, zipCode, city, state, country, cardType, number, expMonth, expYear, CVV) = getConfig()

	#driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
	driver = webdriver.Firefox() # this will show what the program is doing through firefox
	#driver = webdriver.Chrome(str(os.getcwd())+'/chromedriver') # same as the firefox thing, but for chrome
	driver.set_window_size(800, 800)
	driver.get(url)
	addToCartButton = None
	good = False
	while not good:
		try:
			if size != "":
				select = Select(driver.find_element_by_name('size'))
				select.select_by_visible_text(size)
			addToCartButton = driver.find_element_by_name('commit').click() # the add to cart button
			good = True
		except NoSuchElementException as e:
			driver.get(url)
	time.sleep(1)
	driver.get('https://www.supremenewyork.com/checkout') # begin checkout
	# fill out pay form
	try:
		driver.find_element_by_id('order_billing_name').send_keys(name)
		driver.find_element_by_id('order_email').send_keys(email)
		driver.find_element_by_id('order_tel').send_keys(tel)
		driver.find_element_by_id('bo').send_keys(address)
		driver.find_element_by_id('order_billing_zip').send_keys(zipCode)
		driver.find_element_by_id('order_billing_city').send_keys(city)
		Select(driver.find_element_by_id('order_billing_state')).select_by_value(state)
		Select(driver.find_element_by_id('order_billing_country')).select_by_value(country)
		Select(driver.find_element_by_id('credit_card_type')).select_by_value(cardType)
		driver.find_element_by_id('cnb').send_keys(number)
		Select(driver.find_element_by_id('credit_card_month')).select_by_value(expMonth)
		Select(driver.find_element_by_id('credit_card_year')).select_by_value(expYear)
		driver.find_element_by_id('vval').send_keys(CVV)
		driver.find_element_by_id('order_terms').click()
		driver.find_element_by_name('commit').click()
	except NoSuchElementException as e:
		print("The config file has invalid data in it for this purchase. Check the details there.")