import sys

try:
    assert sys.version_info >= (3, 0)
except:
    print('version error: use python 3 or higher')
    exit()

import socket as s
import time

host = sys.argv[1]
port = int(sys.argv[2])

client = s.socket(s.AF_INET, s.SOCK_STREAM)

client.connect((host, port))

print(f'Connected to {host}')
time.sleep(2)
client.close()
exit()