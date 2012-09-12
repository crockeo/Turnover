#!/usr/bin/python
# (For running on Unix)

import Game

shouldRun = True
while shouldRun:
	try:
		width = int(raw_input("Enter width: "))
		height = int(raw_input("Enter height: "))
	except ValueError:
		continue

	Game.init()
	shouldRun = Game.start()

print "Thanks for playing!"