#changeImage.py   --> resize and convert from tiff to jpeg
#!/usr/bin/env python3

from PIL import Image
import os, sys

path = "supplier-data/images/"
for x in os.listdir(path):
    if "tiff" in x:
        file_old = os.path.splitext(x)[0]
#        print(file_old)
        file = file_old + ".jpeg"
        im = Image.open(path + x).convert('RGB')
        im.resize((600,400)).save(path + file, "JPEG")
        im.close()
for y in os.listdir(path):
    if "tiff" in y:
        os.remove(path + y)
===================================================================
#supplier_image_upload.py   --> upload resized images to the webpage
#!/usr/bin/env python3
import requests, os

path = "supplier-data/images/"
url = "http://localhost/upload/"

for x in os.listdir(path):
    if "jpeg" in x:     #if x.endswith(".jpeg")
        with open(path + x, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
===================================================================
#run.py    --> POST the fruit images and their respective description in JSON format.
#!/usr/bin/env python3     
         
import os, sys
import json
import requests

path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

files = os.listdir(path)

for file in files:
  if file.endswith("txt"):
    with open(path + file, 'r') as f:
      #grab the file name, ex. 001, 002 to use for image file
      fruit_name = os.path.splitext(file)[0]
      data = f.read()
      data = data.split("\n")
      fruit_dic = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": fruit_name + ".jpeg"}
      response = requests.post(url, json=fruit_dic)
      response.raise_for_status()
      print(response.request.url)
      print(response.status_code)         
         
#     OR   
#!/usr/bin/env python3

import os, requests, json

url = "http://localhost/fruits/"
path = "supplier-data/descriptions/"
keys = ["name", "weight", "description", "image_name"]

for file in os.listdir(path):
    dict = {}
    keycount = 0

    with open(path + file, "r") as content:
        if file.endswith("txt"):
            pure_name = os.path.splitext(file)[0]
            f = content.read()
            f = f.split("\n")
            dict[keys[0]] = f[0]
            dict[keys[1]] = int(f[1].strip(" lbs"))
            dict[keys[2]] = f[2]
            dict[keys[3]] = pure_name + ".jpeg"

            response = requests.post(url, json=dict)
            response.raise_for_status()
            print(response.request.url)
            print(response.status_code)
 ===================================================================
#reports.py --> Generate a PDF report and send it through email
#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, name, description):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)

    report_title = Paragraph(name, styles["h1"])
    report_info = Paragraph(description, styles["BodyText"])
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_info, empty_line])
===================================================================
#emails.py --> send PDF report through email
#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path = None):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  if attachment_path != None:
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_filename)
  return message

def send_email(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()


===================================================================
#report_email.py --> call reports.py and send via email.py
#!/usr/bin/env python3

import emails
import os
import reports
import datetime

current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def create_pdf(path):
    pdf = ""
    for file in os.listdir(path):
        if file.endswith("txt"):
            with open(path + file, "r") as content:
                f = content.read()
                f = f.split("\n")
                name = f[0].strip()
                weight = f[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return pdf

if __name__ == "__main__":
    path = "supplier-data/descriptions/"
    title = "Processed Update on " + current_date
    paragraph = create_pdf(path)
    reports.generate_report("/tmp/processed.pdf", title, paragraph) 

    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)
===================================================================
#health_check.py
#!/usr/bin/env python3

import requests
import socket
import shutil
import psutil
import emails, os

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return  usage < 80

def check_disk_space():
  du = shutil.disk_usage('/')
  free = du.free / du.total * 100
  return free > 20

#Report an error if available memory is less than 500MB
def memory_ussage():
  free_memory = psutil.virtual_memory().available
  free_memory_MB = free_memory / 1024 ** 2
  return free_memory_MB > 500

def check_localhost():
  localhost = socket.gethostbyname("localhost")
  if localhost == "127.0.0.1":
      return True
  else:
      return False

def error_email(error):
  sender = "automation@example.com"
  recipient = "{}@example.com".format(os.environ["USER"])
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, recipient, subject, body)
  emails.send_email(message)

if not check_cpu_usage():
  subject = ("Error - CPU usage is over 80%")
  error_email(subject)

if not check_disk_space():
  subject = "Error - Available disk space is less than 20%"
  error_email(subject)

if not memory_ussage():
  subject = "Error - Available memory is less than 500MB"
  error_email(subject)

if not check_localhost():
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  error_email(subject)

===================================================================
#cron_file  --> crontab -e


In order for cron_file to work, you need to modifiy the health_check.py.
line 34
  receiver = "{}@example.com".format(os.environ["USER"])
to
  receiver = "{user-name}@example.com"

1 * * * * . $HOME/.profile; python3 /home/{user-name}/health_check.py



{user-name} is the username provided by your qwiklabs session





















OTHER FILES:
===================================================================
#download.sh
#!/bin/bash

# First parameter is the ID, second parameter is the filename
FILEID=$1
FILENAME=$2

# This script downloads the drive file with the given ID and saves it with the given name

COOKIE_FILE=$(mktemp cookiesXXXX.txt)

# First get the confirmation prompt because the file is too big
CONFIRM=$(wget --quiet --save-cookies ${COOKIE_FILE} --keep-session-cookies "https://docs.google.com/uc?export=download&id=${FILEID}" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')

# Then download the file using the confirmation prompt
wget --load-cookies ${COOKIE_FILE} "https://docs.google.com/uc?export=download&confirm=${CONFIRM}&id=${FILEID}" -O ${FILENAME}

# Finally, delete the cookie file
rm ${COOKIE_FILE}
===========================================================================
student-02-48afc52637ad@linux-instance:~$ cat example_upload.py
#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})




