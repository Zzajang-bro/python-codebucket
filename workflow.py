import os
os.mkdir('tmp')

from urllib import request
giturl = 'https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.3/Git-2.41.0.3-64-bit.exe'
savenm= './tmp/git.exe'
request.urlretrieve(giturl, savenm)

import subprocess
subprocess.call(['./tmp/git.exe', '/VERVSILENT', '/NORESTART'])

os.environ['PATH'] += r'C:\Program Files\Git\bin;'

subprocess.run(['git','clone','"https://github.com/Zzajang-bro/python-codebucket"'], capture_output=True)
os.chdir('python-codebucket')
subprocess.run(['git','remote','add','origin','"https://github.com/Zzajang-bro/python-codebucket"'], capture_output=True)
subprocess.run(['git','push','-u','origin','main'], capture_output=True)
subprocess.run(['git','add','.'], capture_output=True)
subprocess.run(['git','commit','-m','"update"'], capture_output=True)
subprocess.run(['git','push'], capture_output=True)
