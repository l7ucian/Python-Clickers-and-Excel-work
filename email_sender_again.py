# Import smtplib for the actual sending function
import smtplib

sender = 'lucian.andercou@continental-corporation.com'
receivers = ['lucianandercou@yahoo.com']

message = """From: From Person <lucian.andercou@continental-corporation.com>
To: To Person <lucian.andercou@yahoo.com>
Subject: SMTP e-mail test

I sure wish this turned into something greater
"""

# Send the message via our own SMTP server.
try:
    print("sending message: " + message)
    with smtplib.SMTP_SSL('smtp.lotusnotes.com', 25) as session:
        session.login("lucian.andercou@continental-corporation.com", "Conti2Pass")
        session.sendmail(sender, receivers, message)
    print("message sent")
except smtplib.SMTPException:
    print("could not send mail")