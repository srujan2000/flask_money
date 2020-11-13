from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,ValidationError,Email

class SpentForm(FlaskForm):
    date = StringField('Date',validators=[DataRequired()])
    amount = StringField('Amount',validators=[DataRequired()])
    wher = StringField('Where',validators=[DataRequired()])
    purchased = StringField('Spent On',validators=[DataRequired()])
    submit = SubmitField('Submit')

class RecForm(FlaskForm):
    date = StringField('Date',validators=[DataRequired()])
    amount = StringField('Amount',validators=[DataRequired()])
    fro = StringField('From',validators=[DataRequired()])
    reason = StringField('Reason',validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    login = SubmitField('Login')