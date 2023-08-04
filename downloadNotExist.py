# 20230804
# downloadNotExist( path, url )

from downloadResFrmWeb import downloadResFrmWeb
from checkFileExist import checkFileExist

def downloadNotExist( path, url ):
	if not checkFileExist( path ):
		downloadResFrmWeb( url, path)