# 20230804
# downloadResFrmWeb(url, nm)

from urllib import request
def downloadResFrmWeb(url, nm):
	request.urlretrieve(url, nm)
