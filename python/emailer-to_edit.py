import smtplib
import os
import time

print('Welcome to PES - Python Emaill Sender\n')
print('For now, PES supports only Gmail')
print('Remember that you need to set special password to log in!')
print('You can do it here -->>  https://myaccount.google.com/apppasswords\n')
print('...and please dont use \' ok?\n')

opt1 = 'n'
while opt1 != 'y':
    opt1 = input('[y] I\'ve already done it! [n] No, wait, i\'m setting it now...> ')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

if os.path.exists('pes-data.txt') == True:
    data_file = open('pes-data.txt')
    login = data_file.readline()
    passw = data_file.readline()
    server.login(login, passw)
    print('*Loaded login and pass from \'pes-data.txt\'*\n')
else:
    data_file = open('pes-data.txt', 'w+')
    login = input('Enter your gmail: ')
    data_file.write(login+'\n')
    passw = input('Enter your SPECIAL password: ')
    data_file.write(passw)

if os.path.exists('pes-friends.txt') == True:
    frs = open('pes-friends.txt', 'r')
    i=1
    print('Your friends list:')
    for mail in frs:
        print(str(i)+'. '+mail.strip())
        i+=1
    print()
    email_to = input("Enter email which you want to send on: ")
else:
    email_to = input("Enter email which you want to send on: ")
is_fr = input("Do you want to add this email to friends [y/n] ")

if os.path.exists('pes-friends.txt') == True:
    if is_fr == 'y':
        fr = open('pes-friends.txt', 'a')
        fr.write(email_to+'\n')
else:
    if is_fr == 'y':
        fr = open('pes-friends.txt', 'a+')
        fr.write(email_to+'\n')

subject = input('Enter subject of email: ')
body = input('Enter body of email: ') + '\n\n\n\n This message has been sent by PES - Python Email Sender by Candyy'
msg = f'Subject: {subject}\n\n{body}'

opt2 = input("Are you sure that you want to send this email? [y/n] ")
if opt2 == 'y':
    server.sendmail(login, email_to, msg)
else:
    print('Shutting down program is 5s...')
    time.sleep(5)
    server.quit()
    exit()