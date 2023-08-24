from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Anup Mondal"
message["to"] = "anup12.m@gmail.com"
message["subject"] = "THis is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="mail.anupmondal.me", port=465) as smtp:
    smtp.ehlo()
    print("sending...")
    # smtp.starttls()
    # smtp.login("test@anupmondal.me", "Test@2023")
    # smtp.send_message(message)
    # print("sending...")
