# 20230805
# numberPaddingZero( 자리수, 숫자 )

def numberPaddingZero( digit, num ):
	l = [0] * digit
	for i in range(digit-1, -1, -1):
		l[i] = chr(ord('0') + num % 10 )
		num //= 10
	return ''.join(l)
