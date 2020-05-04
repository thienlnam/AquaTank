#!/usr/bin/python


#- DB imports
import peewee
from peewee import *

import MySQLdb

import time
from selenium import webdriver
from random import randint #For random int values

driver = webdriver.Chrome('/home/jack/Desktop/Trainy/chromedriver')  # Optional argument, if not specified will search path.
username = ""
password = ""
url = "https://www.chegg.com/homework-help/questions-and-answers/10-augmented-matrix-denotes-arbitrary-number-denotes-nonzero-number-determine-whether-give-q28297415"

def login_one():
	driver.get('https://www.chegg.com');
	time.sleep(3) # Let the user actually see something!
	driver.find_element_by_css_selector(".signin-item.nav-item.track-signin").click()
	time.sleep(4) # Let the user actually see something!
	driver.find_element_by_id("emailForSignIn").send_keys(username)
	time.sleep(5) # Let the user actually see something!
	driver.find_element_by_id("passwordForSignIn").send_keys(password)
	time.sleep(3)
	driver.find_element_by_css_selector(".login-button.button.flat").click()
	time.sleep(5)
	driver.quit()

def login_from_answer():
	driver.find_element_by_css_selector(".btn-primary-lg.cta-btn").click()
	time.sleep(randint(1, 5))
	driver.find_element_by_xpath('//span[@aria-label="Go to sign in panel."]').click()
	time.sleep(randint(2, 5))
	driver.find_element_by_id("emailForSignIn").send_keys(username)
	time.sleep(randint(1, 5))
	driver.find_element_by_id("passwordForSignIn").send_keys(password)
	time.sleep(randint(2, 5))
	driver.find_element_by_css_selector(".login-button.button.flat").click()
	time.sleep(randint(1, 5))


def grab_data():
	driver.get(link);
	time.sleep(randint(1, 4))

	question_title_element = driver.find_element_by_css_selector(".question-text.chg-ellipsis")
	question_title = question_title_element.text

	question_image_links = []
	answer_image_links = []
	question_element = driver.find_element_by_css_selector(".ugc-base.question-body-text")
	question_body = question_element.text
	if (question_element.find_elements_by_tag_name('img')):
		images = question_element.find_elements_by_tag_name('img')
		for image in images:
			question_image_links.append(image.get_attribute('src'))

	category_element = driver.find_element_by_css_selector(".txt-2-small.global-breadcrumb")
	category = category_element.text

	print(question_image_links)
	driver.quit()

	#if (driver.find_element_by_css_selector(".dialog.inline-obfus")):
		#login_from_answer()
	#	time.sleep(randint(4, 8))

	#answer_element = driver.find_element_by_css_selector(".answer-given-body.ugc-base")
	#answer_text = answer_element.text
	#if (answer.find_elements_by_tag_name('img')):
	#	images = question_element.find_elements_by_tag_name('img')
	#	for image in images:
	#		answer_image_links.append(image.get_attribute('src'))







def input_database():
	db = MySQLdb.connect(host="",    # your host, usually localhost
                     user="",         # your username
                     passwd="",  # your password
                     db="")        # name of the data base

	print(db)

	question_title = "question_title"
	question_text = "question_text"
	question_links = "questionlinks"
	answer_text = "answer_text"
	answer_links = "answerlinks"
	category = "category"

	cur = db.cursor()
	"""
	class CheggEntry(Model):
		link = url
		question_title = TextField()
		question_text = TextField()
		question_links = TextField()
		answer_text = TextField()
		answer_links = TextField()
		category = TextField()

		class Meta:
			database = db


	entry = CheggEntry.create(question_title=question_title, question_text=question_text, question_links=question_links, answer_text=answer_text, answer_links=answer_links, category=category)
	"""

	mycursor = mydb.cursor()

	sql = "INSERT INTO chegg (title, question, answer, link, category, has_image) VALUES (%s, %s, %s, %s, %s, %s, %d)"
	val = ("title", "question", "answer", "link", "category", 1)
	mycursor.execute(sql, val)

	mydb.commit()

	#print(mycursor.rowcount, "record inserted.")

input_database()
