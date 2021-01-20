#!/usr/bin/env python3

import datetime
import email
import smtplib
import sys

def send_message(message, emails):
    smtp = smtplib.SMTP('www.gmail.com')
    message['From'] = 'tarasa1987@gmail.com'
    message['To'] = "taras.gayevyy@atos.net"
        smtp.send_message(message)
    smtp.quit()
    pass

def main():
    date, time, emails = sys.argv[1].split('|')
    message = message_template(date, title)
    send_message(message, emails)
    print("Message sent")

        
if __name__=="__main__":
    sys.exit(main())