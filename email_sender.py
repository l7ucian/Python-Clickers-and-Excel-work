import smtplib
sender = "lucian.andercou@gmail.com"
receivers = ["lucian.andercou@yahoo.com"]

def format_mail(mail):
    return "{} ".format(mail.split("@")[0], mail)

message = """From: {lucian.andercou@gmail.com}
To: {lucian.andercou@yahoo.com}
Subject: Example Subject
I sure wish this turned into something greater
""".format("{} ".format(sender.split("@")[0], sender), ", ".join(map(format_mail, receivers
)))

try:
    print("sending message: " + message)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as session:
        session.login("lucian.andercou@gmail.com", "trinity777")
        session.sendmail(sender, receivers, message)
    print("message sent")
except smtplib.SMTPException:
    print("could not send mail")