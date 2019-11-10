from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from smtplib import SMTP
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "george.smith2024@gmail.com"
# if you use two step verification, you have to generate an app pass for each app
password = "idpinsokjyititqb"
from_email = username
user_email = "canobi2002@yahoo.com"
try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg = MIMEMultipart()
    the_msg['Subject'] = "test email"
    the_msg["From"] = from_email
    the_msg["To"] = user_email
    plain_txt = "this is plain text message"
    html_txt = """
    <html>
      <head></head>
      <body>
        <p>Hey!<br>
          Testing this email <b>message</b>.
        </p>
      </body>
    </html>
    """
    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, "html")
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    email_conn.sendmail(from_email, user_email, the_msg.as_string())
    email_conn.quit()
except SMTPAuthenticationError as e:
    print("Could not login:"+str(e))
except Exception as e:
    print("an error occured:" + str(e))
