# 20230804
# makeDirNotExist('폴더이름')

import os

def makeDirNotExist(nm):
	if not os.path.isdir(nm):
		os.mkdir(nm)