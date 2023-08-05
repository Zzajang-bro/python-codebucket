# 20230805
# 0000000123 나오면 성공

from printTraceback import printTraceback
try:
	from numberPaddingZero import numberPaddingZero

	print(numberPaddingZero(10, 123))
	input()
except:
	printTraceback()
	input()