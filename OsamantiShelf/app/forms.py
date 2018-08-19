from flask_wtf import Form
from wtforms import StringField, PasswordField, validators, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length


class Login(Form):
	username= StringField('Username',[validators.DataRequired(),validators.Length(min=5, max = 120)])
	password = PasswordField('Password ',[validators.DataRequired(),validators.Length(min=8,max=120)])
	submit = SubmitField("Login")


class Register(Form):

	username= StringField('Username',[validators.DataRequired(),validators.Length(min=5, max = 120)])
	password = PasswordField('Password ',[validators.DataRequired(),validators.Length(min=8,max=120)])
	email= StringField('Email',[validators.DataRequired(),validators.Length(min=1, max = 255)])
	name= StringField('Name',[validators.DataRequired(),validators.Length(min=1, max = 255)])
	location= StringField('Location',[validators.DataRequired(),validators.Length(min=1, max = 255)])
	age= IntegerField('Age',[validators.DataRequired(),validators.required()])
	submit = SubmitField("Register")



class AddBooks(Form):

	isbn = StringField('ISBN', validators=[InputRequired(), Length(min=1, max=15)])
	booktitle = StringField('Book Title', validators=[InputRequired(), Length(min=1, max=255)])
	bookauthor = StringField('Book Author', validators=[InputRequired(), Length(min=1, max=255)])
	yrpublished = StringField('Year Published', validators=[InputRequired(), Length(min=1, max=255)])
	publisher = StringField('Publisher', validators=[InputRequired(), Length(min=1, max=255)])
	imgurl1 = StringField('Image 1 (S)', validators=[InputRequired(), Length(min=1, max=255)])
	imgurl2 = StringField('Image 2 (L)', validators=[InputRequired(), Length(min=1, max=255)])
	imgurl3 = StringField('ISBN (XL)', validators=[InputRequired(), Length(min=1, max=255)])
	submit = SubmitField("Add Book")
