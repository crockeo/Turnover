import IOUtils
import Player
import Board

_running = False

# Initializing the game
def init(width, height):
	pass

# Starting the game
def start():
	global _running
	_running = True
	return _loop()

# Stopping the game
def stop():
	global _running
	_running = False


def _loop():
	while _running:
		pass


# Loop functions