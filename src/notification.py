from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.db_manager import DBManager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
import smtplib
import datetime

notify = Blueprint('notify', __name__)

class EmailNotification:
    def __init__(self, message):
        self.message = str(message)

    def send(self, send_to):
        email_user = getenv('EMAIL_USER')
        email_password = getenv('EMAIL_PASSWORD')

        if email_user is None or email_password is None:
            return "BAD"

        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'My Subject'
        msg['From'] = email_user
        msg['To'] = send_to
        msg.attach(MIMEText(self.message, 'plain'))
        
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.fastmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(email_user, email_password)
            smtp_server.sendmail("dawidsobczak@fastmail.com", send_to, msg.as_string())
            smtp_server.close()
            print('Email sent successfully at {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        except Exception as ex:
            print('Error encountered: ', ex)
        return "GOOD"
        



