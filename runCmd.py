# 20230804
# runCmd( cmdList )

import subprocess
import sys
import traceback
def runCmd( cmdList ):
	try:
		subprocess.Popen(cmdList, stdout=sys.stdout, stderr=sys.stdout)
	except:
		print(traceback.format_exc())