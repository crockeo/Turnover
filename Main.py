#!/usr/bin/python
# (For running on Unix)

import Data
import Game

# Loading a level from a file
def loadLevel(location):
	try:
		with open(location, 'r') as reader:
			line = reader.readline().split(' ')
			Game.init(int(line[0]), int(line[1]))

			for y in range(Game.board.getHeight()):
				line = reader.readline().rstrip('\n').split(' ')
				if line == '#':
					y -= 1
					continue
				for x in range(Game.board.getWidth()):
					print line
					Game.board.setTile(x, y, line[x])
					if Game.board.getTile(x, y) == Data.SPAWN:
						Game.player.setPosition(x, y)

		Game.board.setTile(Game.player.getX(), Game.player.getY(), Data.PLAYER)
	except IOError:
		print "File not found."
		return -1

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
		if loadLevel(fileLocation) == -1:
			continue

	Game.player.setUnder(Data.SPAWN)
	shouldRun = Game.start()

print "Thanks for playing!" # Saying good bye
raw_input() # Pausing at the end