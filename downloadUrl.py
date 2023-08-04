# 20230804
# downloadUrl( url, nm )

from makeDirNotExist import makeDirNotExist
from downloadNotExist import downloadNotExist

def downloadUrl( url, nm ):
	makeDirNotExist('./tmp')
	downloadNotExist(f'./tmp/{nm}', url)
