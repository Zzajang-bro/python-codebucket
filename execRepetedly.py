# 20230806
# execRepetedly( module name, args as list, time as second )

import importlib
import time

def execRepetedly( moduleNm, args, t):
	while True:
		mod = importlib.import_module(moduleNm)
		fn = getattr(mod, moduleNm)(*args)
		time.sleep(t)