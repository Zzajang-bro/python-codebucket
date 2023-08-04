# 20230804
# runAsAdminWin( func )

from installPyUAC import installPyUAC

installPyUAC()

import pyuac
def runAsAdminWin( func ):
	if not pyuac.isUserAdmin():
		pyuac.runAsAdmin()
	else:
		func()