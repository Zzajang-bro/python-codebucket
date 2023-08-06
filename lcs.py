# 20230806
# lcs( list1, list2 ) => 사용 여부 리스트 2개 반환

from vector2d import vector2d
from addNoneAsZero import addNoneAsZero as add

def lcs( list1, list2 ):
	len1 = len(list1)
	len2 = len(list2)
	v = vector2d().access
	def comp(*args):
	for i in range(len1):
		for j in range(len2):
			comp( i, j, list1[i] == list2[j])

	for i in range(len1):
		for j in range(len2):
			tmpSum = add( comp(i-1, j-1), comp(i, j) )
			tmpMax = max(comp[i-1][j], comp[i][j-1])
			comp[i][j] = max( tmpSum, tmpMax )

	x = len1 - 1
	y = len2 - 1

	while x > 1 and y > 1:
		if 
