import time

print('1. Network output')
print('2. Download data')
print('3. Download time')

chc = input('Your choice: ')

if chc == '1':
    data = input('Enter download data [M/G]: ')
    data_pure = int(data[:-1])
    if data[-1] == 'M':
        pass
    if data[-1] == 'G':
        data_pure = data_pure * 1024

    time = input('Enter download time [h/m/s]: ')
    time_pure = int(time[:-1])
    if time[-1] == 'h':
        time_pure = time_pure * 3600
    if time[-1] == 'm':
        time_pure = time_pure * 60
    if time[-1] == 's':
        pass

    cap = round(((data_pure / time_pure) * 8), 1)
    print()
    print(f'Network output: {cap} Mb/s')

elif chc == '2':
    cap = input('Enter network output [Mb/Gb (/s)]: ')
    cap_pure = int(cap[:-2])
    if 'Mb' in cap:
        cap_pure = cap_pure / 8
    if 'Gb' in cap:
        cap_pure = (cap_pure * 1000) / 8
    if cap_pure > 1024:
        cap_pure = cap_pure / 1024

    time = input('Enter download time [h/m/s]: ')
    time_pure = int(time[:-1])
    if time[-1] == 'h':
        time_pure = time_pure * 3600
    if time[-1] == 'm':
        time_pure = time_pure * 60
    if time[-1] == 's':
        pass

    data = cap_pure * time_pure
    if data > 1024:
        data = round((data / 1024), 1)
        data = str(data)
        data += ' GB'
    else:
        data = str(data)
        data += ' MB'
    print(f'Download data: {data}')

elif chc == '3':
    data = input('Enter download data [M/G]: ')
    data_pure = int(data[:-1])
    if data[-1] == 'M':
        pass
    if data[-1] == 'G':
        data_pure = data_pure * 1024

    cap = input('Enter network output [Mb/Gb (/s)]: ')
    cap_pure = int(cap[:-2])
    if 'Mb' in cap:
        cap_pure = cap_pure / 8
    if 'Gb' in cap:
        cap_pure = (cap_pure * 1000) / 8
    if cap_pure > 1024:
        cap_pure = cap_pure / 1024

    time = data_pure / cap_pure

    if time > 60 and time < 3600:
        time = round((time / 60))
        time = str(time)
        time = time + ' min'
    if time > 3600:
        time = round((time / 3600))
        time = str(time)
        time = time + ' hrs'
    else:
        time = str(time)
        time = time + ' sec'

    print(f'Download time: {time}')

else:
    print('error')
    time.sleep(1)
    exit()