import Data

class Player:
	def __init__(self, x, y, board):
		self.setX(x)
		self.setY(y)

		self.setUnder(board.getTile(self.getX(), self.getY()))
		board.setTile(self.getX(), self.getY(), Data.PLAYER)