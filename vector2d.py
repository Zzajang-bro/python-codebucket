# 20230806
# v = vector2d().access
# v(x, y, v) 할당
# v(x, y)

class vector2d:
	def __init__(self):
		self.dat = {}
	def access( self, *args ):
		tup = (args[0], args[1])
		if len(args) > 2:
			self.dat[tup] = args[2]
		if len(args) >= 2:
			if tup in self.dat:
				return self.dat[tup]
			else:
				return None
		return None
