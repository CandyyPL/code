import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

addr = 'sweetbot.noreply@gmail.com'
passw = 'mshmtuovnoyrikmy'

server.login(addr, passw)

sub = input('Subject: ')
body = input('Body: ')
msg = f'Subject: {sub}\n\n{body}'

to = input('Email: ')

server.sendmail(addr, to, msg)