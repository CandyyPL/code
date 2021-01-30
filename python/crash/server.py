import sys

try:
    assert sys.version_info >= (3, 0)
except:
    print('version error: use python 3 or higher')
    exit()

import socket as s

host = s.gethostbyname(s.gethostname())
port = 13378

BUFFER = 1024

serv = s.socket(s.AF_INET, s.SOCK_STREAM)
serv.bind((host, port))

serv.listen()

while True:
    client, addr = serv.accept()

    print(f'Connection from {addr[0]}')