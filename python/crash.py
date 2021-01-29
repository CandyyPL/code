import sys

try:
    sys.version_info >= (3, 0)
except:
    print('version error: use python 3 or higher')
    exit()

from colored import fg, attr
import random
import time
import os

def game(rng):
    os.system('cls')

    if rng == 1:
        crash_rng = random.uniform(crashRange.cat1[0], crashRange.cat1[1])
    elif rng == 2:
        crash_rng = random.uniform(crashRange.cat2[0], crashRange.cat2[1])
    elif rng == 3:
        crash_rng = random.uniform(crashRange.cat3[0], crashRange.cat3[1])
    elif rng == 4:
        crash_rng = random.uniform(crashRange.cat4[0], crashRange.cat4[1])
    elif rng == 5:
        crash_rng = random.uniform(crashRange.cat5[0], crashRange.cat5[1])
    elif rng == 6:
        crash_rng = random.uniform(crashRange.cat6[0], crashRange.cat6[1])

    crsh = 1.00
    while crsh < crash_rng:
            crsh += 0.01
            os.system('cls')
            # sys.stdout.write(f'\rCurrent crash: {colors.green}x{round(crsh, 2)}{colors.res}')
            # sys.stdout.write(f'\n\rCurrent balance to withdraw: {colors.green}{bet * round(crsh, 2)}{colors.res}')
            # print('Press SPACE to withdraw')
            time.sleep(0.02)
            sys.stdout.flush()
    os.system('cls')
    print(f'Current crash: {colors.red}x{round(crsh, 2)} !CRASHED!{colors.res}')
    time.sleep(4)


nickname = input('Enter your nickname: ')
balance = 500
bet = 0

playModes = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]

class colors:
    green = fg('green')
    red = fg('red')
    res = attr('reset')

class crashRange:
    cat1 = [1.01, 3.49]
    cat2 = [3.50, 7.49]
    cat3 = [7.50, 22.49]
    cat4 = [22.50, 48.49]
    cat5 = [48.50, 75.49]
    cat6 = [75.50, 125.49]

while True:
    os.system('cls')
    bet = int(input(f'Place your bet [{balance}]: '))
    if bet > balance:
        print('Not enough coins!')
        time.sleep(2)
    else:
        crs = random.choice(playModes)
        game(crs)