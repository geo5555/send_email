from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from smtplib import SMTP
import smtplib

host = "smtp.gmail.com"
port = 587
username = "george.smith2024@gmail.com"
# if you use two step verification, you have to generate an app pass for each app
password = "idpinsokjyititqb"
from_email = username
recipient = "canobi2002@yahoo.com"
try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    email_conn.sendmail(from_email, recipient,
                        "Hello there this is an email message")
    email_conn.quit()
except SMTPAuthenticationError as e:
    print("Could not login:"+str(e))
except Exception as e:
    print("an error occured:" + str(e))
