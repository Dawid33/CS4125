from flask_wtf import FlaskForm
# StringField is basically an input box
# SubmitField is for the submit button
from wtforms import StringField, SubmitField#
# Ensure that all fields are filled out
from wtforms.validators import DataRequired

class AddBook(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Add Book')