# This is the main Python file for the Automated Email Sender project.
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "your_email@gmail.com"
    password = "your_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

subject = input("Enter subject: ")
body = input("Enter email body: ")
to_email = input("Enter recipient email: ")
send_email(subject, body, to_email)
