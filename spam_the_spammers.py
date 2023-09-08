import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'  # do not modify
smtp_port = 587  # do not modify
smtp_username = 'your@email.addresse'  # your email address
smtp_password = 'your_password'  # your email password

sender = 'your@email.address'
recipients = ['recipient1@email.address', 'recipient1@email.address', '...']
subject = 'email subject'
message = 'email body'
email_quantity = 20  # number of emails you want to send
delay = 10  # delay between emails

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ', '.join(recipients)
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        for i in range(email_quantity):
            server.send_message(msg)
            print(f"Email {i + 1} sent successfully!")
            time.sleep(delay)

except Exception as e:
    print('Error sending email:', str(e))
