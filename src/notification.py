from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.database_manager.db_manager import DBManager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
import smtplib
import datetime

notify = Blueprint('notify', __name__)

