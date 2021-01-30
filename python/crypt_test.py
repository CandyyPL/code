text = input('Enter text: ')

textTab = list(text)

binText = ''
i = 0

for char in textTab:
    binText += format(ord(char), '08b')
    if i == len(textTab)-1:
        pass
    else: binText += ' '
    i += 1

binTextTab = binText.split(' ')
bttl = len(binTextTab)

toXorBinTextTab = []
xorTab = []
spacedBin = ''
bCn = 0

for binary in binTextTab:
    l = len(binary)
    for b in binary:
        spacedBin += b
        if bCn == l-1:
            spacedBin += b
        else: spacedBin += b + ' '
        bCn += 1
    xorTab += spacedBin.split(' ')
    toXorBinTextTab.append(xorTab)
    xorTab = []
    spacedBin = ''
    bCn = 0


key = input('Enter key: ')

keyTab = list(key)

keyBinText = ''
i = 0

for char in keyTab:
    keyBinText += format(ord(char), '08b')
    if i == len(keyTab)-1:
        pass
    else: keyBinText += ' '
    i += 1

binKeyTab = keyBinText.split(' ')
bktl = len(binKeyTab)

keyMainTab = []
keySubTab = []
keySpaced = ''
cn = 0

for binaryKey in binKeyTab:
    for by in binaryKey:
        keySpaced += by
        if cn == 1 or cn == 3 or cn == 5:
            keySpaced += ' '
        cn += 1
    keySubTab += keySpaced.split(' ')
    keyMainTab.append(keySubTab)
    keySubTab = []
    keySpaced = ''
    cn = 0

print(toXorBinTextTab)
print(keyMainTab)