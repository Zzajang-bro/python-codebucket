# 20230805
# ymd(): YYYYMMDD

import datetime
from numberPaddingZero import numberPaddingZero

def ymd():
	t = datetime.date.today()
	y = t.year
	m = t.month
	d = t.day
	return numberPaddingZero(4, y) + numberPaddingZero(2, m) + numberPaddingZero(2, d)