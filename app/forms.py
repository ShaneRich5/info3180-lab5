from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField
from wtforms.validators import Required, Email

class LoginForm(Form):
	username = TextField('Username', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	