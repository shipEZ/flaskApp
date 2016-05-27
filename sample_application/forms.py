from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, PasswordField
from wtforms.validators import Required, Email

class EmailPasswordForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])