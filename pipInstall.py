# 20230804
# pipInstall(pkgNm)

def pipInstall(pkgNm):
	from runCmd import runCmd
	runCmd(['pip', 'install', pkgNm])
