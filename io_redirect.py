''' demo showing subprocess and stdout '''
import shlex
import subprocess

print(shlex.quote('foo bar'))

LOG_FILE = 'logs.txt'
try:
    FILE = open(LOG_FILE, mode='w+b')
except IOError as err:
    print('Failed to open LOG_FILE: %s' % LOG_FILE)
    raise err

try:
    subprocess.run('ls -al ~', check=True, shell=True, stdout=FILE, stderr=FILE)
except subprocess.CalledProcessError as err:
    print('Failed to run subprocess, err: %s' % err)
    raise err
finally:
    print('Closing file: %s' % LOG_FILE)
    FILE.close()
