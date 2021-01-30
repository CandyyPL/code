try:
    from pyfirmata import Arduino, util
except:
    print('It seems like pyFirmata is not installed!')
    if input('Would you like to do it? [y/n] ') == 'y':
        import pip
        pip.main(['install','pyfirmata'])
        from pyfirmata import Arduino, util
    else:
        exit()