import sys

try:
    assert sys.version_info >= (3, 0)
except:
    print('version error: use python 3 or higher')
    exit()

import random
import os

DATABASE = ['hello.txt', 'goodbye.txt']

def dbCheck(db):
    for rec in db:
        if os.path.exists(rec):
            pass
        else: return False
    return True

def randomLine(file):
    toRead = open(file)
    read = toRead.read()
    lines = read.splitlines()
    return random.choice(lines)

def makeAnswer(inp):
    if inp in fHelloLines:
        answer = randomLine(DATABASE[0])
        return print(f'Caedmil> {answer}')
    elif inp in fGoodbyeLines:
        answer = randomLine(DATABASE[1])
        return print(f'Caedmil> {answer}')
    else:
        return print('Caedmil> Sorry, but I don\'t understand what are you trying to say!')

if dbCheck(DATABASE) == False:
    print('database loading error')
    print('exiting')
    exit()
else:
    fHello = open(DATABASE[0], 'r')
    fHelloRead = fHello.read()
    fHelloLines = fHelloRead.splitlines()
    fGoodbye = open(DATABASE[1], 'r')
    fGoodbyeRead = fGoodbye.read()
    fGoodbyeLines = fGoodbyeRead.splitlines()

    print('Hello, I\'m Caedmil. I\'m kinda CleverBot,\n so you can ask me something.\n C\'mon!')
    username = input('First enter your name: ')

    while True:
        question = input(username+'> ')

        makeAnswer(question)