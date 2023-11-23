# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from models.database_manager.db_manager import DBManager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
from typing import Dict
import smtplib
import datetime
import threading


class INotify:
    def send(self):
        pass


class Notification(INotify):
    def __init__(self, message):
        self.message = str(message)

    """
    Default implementation prints to console.
    """
    def send(self, recipient):
        print(f"Send notification to {recipient}.")


class SmsDecorator(INotify):
    def __init__(self, component : INotify):
        self._component = component

    @property
    def component(self) -> INotify:
        return self._component

    def send(self, recipient):
        self._component.send(recipient)
        print(f"Sending message via SMS")

class EmailDecorator(INotify):
    def __init__(self, component : INotify, subject):
        self._component = component
        self.subject = subject

    @property
    def component(self) -> INotify:
        return self._component

    def send(self, recipient):
        self._component.send(recipient)
        print(f"Sending message via email")
        email_user = getenv('EMAIL_USER')
        email_password = getenv('EMAIL_PASSWORD')
        email_domain = getenv('EMAIL_DOMAIN')

        if email_user is None or email_password is None or email_domain is None:
            # My sacrificial lamb so ye don't have to set those env variables.
            # Its only possible to send mail from that password so it *should* 
            # be okay.            
            email_user = "dawidsobczak@fastmail.com"
            email_password = "83yh9zazhztaazwr"
            email_domain = "smtp.fastmail.com"

        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = email_user
        msg['To'] = recipient
        msg.attach(MIMEText(self._component.message, 'plain'))

        def inner_async():
            try:
                smtp_server = smtplib.SMTP_SSL(email_domain, 465)
                smtp_server.ehlo()
                smtp_server.login(email_user, email_password)
                smtp_server.sendmail(email_user, recipient, msg.as_string())
                smtp_server.close()
                print('Email sent successfully to {} at {}'.format(recipient, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            except Exception as ex:
                print('Error encountered: ', ex)

        send_mail_thread = threading.Thread(target=inner_async, name="Send Mail")
        # Thread should finish on its own... eventually... hopefully.
        send_mail_thread.start()


 
