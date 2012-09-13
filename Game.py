import IOUtils
import Player
import Board
import Data

player = None
board = None

# Initializing the game
def init(width, height):
	global _running, player, board

	board = Board.Board(width, height)
	player = Player.Player(width / 2, height / 2, board)
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

		if _hasWon():
			return _finish(True)


# Loop functions
def _update(char):
	# Checking if the user wants to quit
	if char == 'q':
		return _finish()

	player.update(char, board) # Updating the player

def _hasWon():
	for x in board.getTiles():
		if x == Data.UNACTIVATED:
			return False
	return True

def _finish(won = False):
	IOUtils.clear()

	if (won):
		print "You won!"

	answer = ''
	while (answer.lower() != 'y') and (answer.lower() != 'n'):
		answer = raw_input("Would you like to play again? y/N: ")
		if answer.lower() == 'y':
			return True
		elif (answer == '') or (answer.lower() == 'n'):
			return False