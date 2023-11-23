# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from flask import Blueprint
from models.database_manager.db_manager import DBManager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
import smtplib
import datetime

notify = Blueprint('notify', __name__)

