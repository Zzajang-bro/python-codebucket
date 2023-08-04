from printTraceback import printTraceback
try:
	from downloadGit import downloadGit
	from runCmd import runCmd
	downloadGit()
	runCmd(['./tmp/git.exe', '/SILENT', '/NORESTART'])
except:
	printTraceback()
	input()