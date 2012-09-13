import IOUtils
import Player
import Board

player = None
board = None

# Initializing the game
def init(width, height):
	global _running, player, board

	board = Board.Board(width, height)
	player = Player.Player(width / 2, height / 2)
	_running = False

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
		# Drawing
		IOUtils.clear()
		board.draw()

		# Updating
		updateVal = _update(IOUtils.getch())
		if updateVal != None:
			return updateVal


# Loop functions
def _update(char):
	# Checking if the user wants to quit
	if char == 'q':
		return _finish()

	player.update(char, board) # Updating the player

def _finish():
	IOUtils.clear()

	answer = ''
	while (answer.lower() != 'y') and (answer.lower() != 'n')
		answer = raw_input("Would you like to play again? y/N: ")
		if answer.lower() == 'y':
			return True
		elif (answer == '') or (answer.lower() == 'n'):
			return False