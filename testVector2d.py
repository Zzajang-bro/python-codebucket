# 20230806
# just test

from printTraceback import printTraceback
from vector2d import vector2d

try:
	v = vector2d().access

	print(v(1,2,3))
	print(v(1,2))

	print(v(-1,2,10))
	print(v(-1,2))

	print(v(2,3))

	input()
except:
	printTraceback()
	input()