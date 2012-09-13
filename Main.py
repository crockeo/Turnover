#!/usr/bin/python
# (For running on Unix)

import Game

shouldRun = True
while shouldRun:
	Game.init(9, 9)
	shouldRun = Game.start()

print "Thanks for playing!"