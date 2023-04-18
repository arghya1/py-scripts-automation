#!/usr/bin/python3

import smtplib

smtp_server = "localhost"
port = 1025

sender_email = "my@woof.com"
receiver_email = "arghya.basu.5@gmail.com"
message = """\
Subject: Hi Bolc

This is a python mailer message."""

try:
   server = smtplib.SMTP(smtp_server, port)
   server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
finally: 
    server.quit()
