import smtplib

content = 'HELLO hello'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()   #identify myself for the server (helo - regular, ehlo - for ESMTP server)

mail.starttls()  #tls mode(transport later security)(any smtp that will go after taht will be encrupted)

mail.login('tarasa1987@gmail.com','vmvRjcKi4')

mail.sendmail('tarasa1987@gmail.com', 'shkst@live.com', content) #1)fromemail, 2.receiver 3.content

mail.quit()













#https://www.youtube.com/watch?v=bXRYJEKjqIM
#https://realpython.com/python-send-email/
#https://myaccount.google.com/lesssecureapps