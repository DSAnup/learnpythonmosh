import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template

working_dir = "learnpythonmosh/standard library/"
template = Template(Path(working_dir + "template.html").read_text())

sender_email = "test@anupmondal.me"
sender_password = "Test@2023"
smtp_server = "mail.anupmondal.me"
smtp_port = 465  # This is the standard SMTP port for TLS encryption

subject = "Hello, World!"
recipient_email = "anup12.m@gmail.com"
message_body = "This is a test email sent from Python."

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
body = template.substitute({"name": "Anup"})
msg.attach(MIMEText(body, "html"))
msg.attach(MIMEImage(Path(working_dir + "aishee.jpg").read_bytes()))


try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.ehlo()  # Upgrade the connection to a secure, encrypted connection

    # Log in to your email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Close the SMTP server connection
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print("Email could not be sent. Error:", str(e))
