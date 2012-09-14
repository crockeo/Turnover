import Data

class Board:
	def __init__(self, width, height):
		self._width = width
		self._height = height

		self.setAll(Data.UNACTIVATED)

	def __str__(self):
		return '\n'.join(
			' '.join(self.getTile(x, y) for x in range(self.getWidth()))
			for y in range(self.getHeight())
		)

	def draw(self): print str(self) # Drawing
	def convert(self, x, y): return (y * self.getWidth()) + x # Converting 2D array coords to 1D array coords

	# Flipping a tile
	def flipTile(self, x, y):
		if self.getTile(x, y) == Data.UNACTIVATED:
			self.setTile(x, y, Data.ACTIVATED)
		elif self.getTile(x, y) == Data.ACTIVATED:
			self.setTile(x, y, Data.UNACTIVATED)

	# Accessors
	def getWidth(self): return self._width
	def getHeight(self): return self._height
	def getTiles(self): return self._tiles
	def getTile(self, x, y): return self._tiles[self.convert(x, y)]

	# Mutators
	def setAll(self, value): self._tiles = [value]*(self.getWidth() * self.getHeight())
	def setSize(self, width, height):
		self._width = width
		self._height = height

		old = self.getTiles()
		self.setAll(Data.UNACTIVATED)

		for x in range(len(old)):
			self.setTileByIndex(x, old[x])


	def setWidth(self, width): self.setSize(width, self.getHeight())
	def setHeight(self, height): self.setSize(self.getWidth(), height)

	def setTile(self, x, y, value): self._tiles[self.convert(x, y)] = value
	def setTileByIndex(self, index, value): self._tiles[index] = value