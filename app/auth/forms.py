from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User


class RegistrationForm(FlaskForm):
    '''
    form for new user account
    '''
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    username = StringField('Enter Username', validators=[DataRequired()])
    fullname = StringField('Full Name', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[
                             DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')

    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username exists... Choose another username')


class LoginForm(FlaskForm):
    '''
    form for sign in
    '''
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
