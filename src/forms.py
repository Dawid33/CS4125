# pylint: disable=too-few-public-methods
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from flask_wtf import FlaskForm
# StringField is basically an input box
# SubmitField is for the submit button
from wtforms import StringField, SubmitField#
# Ensure that all fields are filled out
from wtforms.validators import DataRequired

class AddBookForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Add Book')

class WaiveFineForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Delete')

class BlockUserForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Search')

class UnblockUserForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Search')

class RemoveBookForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired()])
    Submit = SubmitField('Delete')