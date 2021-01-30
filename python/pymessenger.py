import sys

try:
    assert sys.version_info >= (3, 0)
except:
    print('version error: use python 3 or higher')
    exit()

import platform
import fbchat
from fbchat import Client
import getpass
import msvcrt as ms
import time
import os

def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    if platform.system() == 'Linux':
        os.system('clear')

print('Welcome to pyMessenger by Candyy!\nYou musn\'t change code and share program under name \'pyMessenger\'\nThanks!')
print('\nHit G to start or Q to exit', end='')

if ms.getch() == b'g':
    clearScreen()
    loginUser = input('Enter your Fb username: ')
    loginPass = getpass.getpass('Enter your Fb password: ')
    attm = 0

    while attm < 3:
        try:
            session = Client(loginUser, loginPass)
            break
        except:
            print(f'Trying attempt {attm+1}')
            attm += 1
    time.sleep(2)

    while True:
        clearScreen()
        searching = session.searchForUsers(input('Search for friend: '))
        clearScreen()

        while True:
            msg = input(f'{searching[0].name} < ')
            if msg == '.quit': break
            elif msg == '.clear': clearScreen()
            else: session.send(fbchat.models.Message(msg), searching[0].uid)

elif ms.getch() == b'q': exit()