from trello import TrelloApi
import re
import os   
from subprocess import call 
import schedule
import time

def job():
 
	trello = TrelloApi('API-KEY-HERE')
	resp = trello.boards.get('BOARD-ID-HERE')
	list = trello.lists.get('LIST-ID-HERE')
	cards = trello.lists.get_card('ID-HERE')


# open premade card_names main file in append mode (a+) to keep track of card names

	card_names = open("./card_names.txt", "a+")


# open premade tasks file in append mode (a+) to use for printer

	tasks = open("./tasks.txt", "a+")    

#get cards from trello
#iterate over each card check that card name is NOT in the card_names file
# if name is in the card_names file do nothing
# else add name into task file AND the card_naames file

	for obj in cards:
  	  if obj["id"] in open('card_names.txt').read():
     	    print "already in the master list"
    	    pass 
  	  else:
    	    card_names.write(obj["id"]+"\n")
    	    tasks.write("\n\n\n\n\n"+ obj["name"] + "\n\n\n\n\n:)")
    	    print "yo i'm printing"	 
    # add name into task file and the card_names file



# print task file if there's content

	if os.stat("tasks.txt").st_size > 0:
          call(["lpr","-o","fit-to-page", "tasks.txt"])

  
# clear task file

	f= open('tasks.txt', 'r+')
	f.truncate()

# schedule job to run the code every 5 seconds

schedule.every(2).seconds.do(job)

while True:
  schedule.run_pending()
  time.sleep(1) 

#def print_card(filename):
#  print "Printing card!"
#  call(["lpr","-o","fit-to-page", "./" + filename + ".txt"])


#for obj in cards:
#  filename = obj["id"]
#  f = open( filename + ".txt", 'w+')
#  f.write(obj["name"]+"\n")
#  print filename
#  print_card(filename)
#  f.close()

