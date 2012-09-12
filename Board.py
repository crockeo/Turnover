class Board:
	def __init__(self, width, height):
		self._width = width
		self._height = height

		self.setAll(Data.UNACTIVATED)

	def __str__(self):
		return '\n'.join(
			' '.join(self.getTile(x, y) for y in range(getHeight()))
			for x in range(getWidth())
		)

	def draw(self): print str(self)
	def convert(self, x, y): return (y * self.getWidth()) + x

	def getWidth(self): return self._width
	def getHeight(self): return self._height
	def getTiles(self): return self._tiles
	def getTile(self, x, y): return self._tiles[self.convert(x y)]

	def setAll(self, value): self._tiles = [value]*(self.getWidth() * self.getHeight())
	def setTile(self, x, y, value): self._tiles[self.convert(x, y)] = value