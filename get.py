# ---- PACKAGES ----
# before the trello package works, make sure to install it: https://pypi.python.org/pypi/trello
from trello import TrelloApi

# in our case, this package helps us interact with files. More info here https://docs.python.org/3/tutorial/stdlib.html#operating-system-interface
import os

# this package is necessary to trigger the printing command from our application. More info here https://pythonspot.com/en/python-subprocess/
from subprocess import call

# import scheduling packages
import schedule
import time

def job():
	trello = TrelloApi('API-KEY-HERE')

  #get cards from trello
	cards = trello.lists.get_card('LIST-ID-HERE')


  # open premade card_names main file in append mode (a+) to keep track of card names
	card_names = open('./card_names.txt', 'a+')


  # open premade tasks file in append mode (a+) to use for printer
	tasks = open('./tasks.txt', 'a+')

  # iterate over each card check that card name is NOT in the card_names file
	for obj in cards:
		# if name is in the card_names file do nothing
		if obj['id'] in open('card_names.txt').read():
			print 'already in the master list'
			pass
		else: # add name into task file and the card_names file
			card_names.write(obj['id']+'\n')
			tasks.write('\n\n\n\n\n'+ obj['name'] + '\n\n\n\n\n:)')
			print "yo i'm printing"


  # print task file if there's content
	if os.stat('tasks.txt').st_size > 0:
		call(['lpr','-o','fit-to-page', 'tasks.txt'])


  # clear task file
	f= open('tasks.txt', 'r+')
	f.truncate()

# schedule job to run the code every 2 seconds
schedule.every(2).seconds.do(job)

# run task when app is ran via the python shell
while True:
	schedule.run_pending()
	time.sleep(1)
