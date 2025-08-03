from agents import function_tool
from typing import Dict
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

@function_tool
def send_email(subject: str, receiver: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body to all sales prospects """
    port = 587  # For starttls
    smtp_server = os.getenv("MAILTRAP_API_HOST")
    login = os.getenv("MAILTRAP_API_USER")
    password = os.getenv("MAILTRAP_API_PASS") 

    sender_mail = 'mail@example.com'
    receiver_email = receiver

    message = MIMEMultipart("alternative")
    message["From"] = sender_mail
    message["To"] = receiver_email
    message["Subject"] = subject 

    part1 = MIMEText(html_body, "plain")
    message.attach(part1)

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls() 
        server.login(login, password)
        server.sendmail(sender_mail, receiver_email, message.as_string())

    return {"status": "success"}