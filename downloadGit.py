# 20230804
# downloadGit()
# tmp 폴더에 git.exe 다운
def downloadGit():
	from makeDirNotExist import makeDirNotExist
	from downloadNotExist import downloadNotExist
	makeDirNotExist('./tmp')

	giturl = 'https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.3/Git-2.41.0.3-64-bit.exe'
	path= './tmp/git.exe'
	downloadNotExist(path, giturl)
