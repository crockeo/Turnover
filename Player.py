import Data

class Player:
	def __init__(self, x, y, board):
		self.setX(x)
		self.setY(y)

		self.setUnder(board.getTile(self.getX(), self.getY()))
		board.setTile(self.getX(), self.getY(), Data.PLAYER)

	# Updating the player
	def update(self, read, board):
		if read == 'w':
			newPos = self.wouldMoveTo(0, -1)
		elif read == 's':
			newPos = self.wouldMoveTo(0,  1)
		elif read == 'a':
			newPos = self.wouldMoveTo(-1, 0)
		elif read == 'd':
			newPos = self.wouldMoveTo( 1, 0)

		# Collision
		if (newPos[0] < 0) or (newPos[0] > board.getWidth() - 1):
			return
		elif (newPos[1] < 0) or (newPos[1] > board.getHeight() - 1):
			return
		elif board.getTile(newPos[0], newPos[1]) == Data.WALL:
			return

		
		# Board operations
		board.setTile(self.getX(), self.getY(), self.getUnder())
		board.flipTile(self.getX(), self.getY())

		# Moving the player
		self.moveTo(newPos[0], newPos[1])
		self.setUnder(board.getTile(self.getX(), self.getY()))

		# More board operations! :D
		board.setTile(self.getX(), self.getY(), Data.PLAYER)
		

	# Moving
	def move(self, dX, dY):
		self.setX(self.getX() + dX)
		self.setY(self.getY() + dY)

	def wouldMoveTo(self, dX, dY): return (self.getX() + dX, self.getY() + dY)

	# Accessors
	def getPosition(self): return (self.getX(), self.getY())
	def getX(self): return self._x
	def getY(self): return self._y
	def getUnder(self): return self._under

	# Mutators
	def setPosition(self, x, y):
		self.setX(x)
		self.setY(y)

	def moveTo(self, x, y):
		self.setX(x)
		self.setY(y)

	def setX(self, x): self._x = x
	def setY(self, y): self._y = y
	def setUnder(self, under): self._under = under