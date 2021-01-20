#################################BODY##########################################################
from email.message import EmailMessage

message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = """Hey there! I'm learning to send emails using Python!"""
message.set_content(body)

#print(message)
#From: me@example.com
#To: you@example.com
#Subject: Greetings from me@example.com to you@example.com!
#MIME-Version: 1.0
#Content-Type: text/plain; charset="utf-8"
#Content-Transfer-Encoding: 7bit

#Hey there! I'm learning to send email using Python!
#########################################ATACHMENT################################################
import os.path
attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
#print(mime_type) --> image/png     --> "image" - MIME type, "PNG" - MIME subtype
mime_type, mime_subtype = mime_type.split('/', 1) #EmailMessage type needs a MIME type and subtypes as separate strings, so we split this up
with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
#######################################SEND#######################################################
import smtplib
mail_server = smtplib.SMTP_SSL('smtp.example.com')
#mail_server.set_debuglevel(1)
import getpass
mail_pass = getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()



