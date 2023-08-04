from printTraceback import printTraceback

try:
	from runAsAdminWin import runAsAdminWin
	def script():
		from downloadUrl import downloadUrl
		from runCmd import runCmd
		downloadUrl('https://download.sublimetext.com/sublime_text_build_4152_x64_setup.exe', 'sublime.exe')
		runCmd(['./tmp/sublime.exe', '/SILENT', '/NORESTART'])
	runAsAdminWin(script)
except:
	printTraceback()
	input()