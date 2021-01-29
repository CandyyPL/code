from colored import fg, attr
import socket as s
import sys

green = fg('green')
red = fg('red')
yellow = fg('yellow')
reset = attr('reset')

ports = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 135, 136, 137, 138, 139, 143, 161, 162, 179, 389, 443, 445, 500, 636, 989, 900]

sc = s.socket(s.AF_INET, s.SOCK_STREAM)

if len(sys.argv) < 3:
    print(f'usage: {sys.argv[0]} [ip_addr] [options]')
    print()
    print('options:')
    print('-c   Scan most common ports')
    print('-p   Scan one port (you need to specify that port)')
    exit()

elif len(sys.argv) == 3 and sys.argv[2] == '-c':
    for x in ports:
        if sc.connect_ex((sys.argv[1], int(x))):
            # print(f'{red}[+]{reset} Port {yellow}{x}{reset} closed')
            pass
        else:
            print(f'{green}[+]{reset} Port {yellow}{x}{reset} open')

elif len(sys.argv) == 4 and sys.argv[2] == '-p':
    port = sys.argv[3]

    if sc.connect_ex((sys.argv[1], int(port))):
        # print(f'{red}[+]{reset} Port {yellow}{port}{reset} closed')
        pass
    else:
        print(f'{green}[+]{reset} Port {yellow}{port}{reset} open')