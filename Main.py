#!/usr/bin/python
# (For running on Unix)

import Game

shouldRun = True
while shouldRun:
	fileLocation = raw_input("Enter file location: ")

	if fileLocation.lower() == "debug":
		Game.init(9, 9)
	elif fileLocation == '':
		continue
	elif fileLocation == "quit":
		break
	else:
		try:
			with open(fileLocation, 'r') as reader:
				pass
		except IOError:
			print "File not found!\n"
			continue

	shouldRun = Game.start()

print "Thanks for playing!" # Saying good bye
raw_input() # Pausing at the end