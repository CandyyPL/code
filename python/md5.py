from colored import fg, attr
import hashlib
import sys

green = fg('green')
yellow = fg('yellow')
red = fg('red')
reset = attr('reset')

if sys.argv[1] == '-h' and len(sys.argv) == 3:
    text = sys.argv[2].encode('utf-8')
    hashed = hashlib.md5(text.strip()).hexdigest()
    print(f'{green}[HASH]{reset} {hashed}')
    exit()

elif sys.argv[1] == '-c' and len(sys.argv) == 4:
    hsh = sys.argv[2]
    wl = open(sys.argv[3], 'r')
    print(f'{yellow}[INFO]{reset} Trying to crack {hsh}')

    for word in wl:
        wEnc = word.encode('utf-8')
        wHsh = hashlib.md5(wEnc.strip()).hexdigest()

        if hsh == wHsh:
            print(f'{green}[SUCCESSFUL]{reset} Match found : {word}')
            exit()

    print(f'{red}[FAIL]{reset} Match not found :(')
    exit()
