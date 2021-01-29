def countLetters(string):
    if len(string) > 2:
        st = ''
        c = 1
        for x in range(0, len(string)):
            if x == 0:
                st += string[x]
            else:
                c += 1
        if c > 2:
            st += str(c)
        return st
    else:
        return string

def splitChars(string):
    st = ''
    last = ''
    for x in range(0, len(string)):
        if x == 0:
            st += string[x]
            last = string[x]
        else:
            if string[x] == last:
                st += string[x]
                last = string[x]
            else:
                st += '-' + string[x]
                last = string[x]

    tab = st.split('-')
    return tab, len(tab)

def closest(lst, key):
    k = lambda i: abs(lst[i] - key)
    value = lst[min(range(len(lst)), key = k)]

    return value