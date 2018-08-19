
from __init__ import app, db
from flask_login import LoginManager, login_user, UserMixin, login_required,current_user




class User(UserMixin,db.Model):
	__tablename__ = "User"
	id= db.Column(db.Integer, primary_key =True)
	name = db.Column(db.String(255))
	username = db.Column(db.String(80), unique = True)
	email = db.Column(db.String(120), unique =True)
	password = db.Column(db.String(255))
	location = db.Column(db.String(255))
	age = db.Column(db.Integer)

	def __init__(self,id,username,email,password,name, location,age):
		self.id = id
		self.username = username
		self.email = email
		self.password = password
		self.name=name
		self.location = location
		self.age = age

	def is_active(self):
		return self.active

	def __repr__(self):
		return '<User %r>' % self.username

class book(db.Model):
	__tablename__ = "book"
	isbn = db.Column(db.String(255), primary_key = True)
	booktitle = db.Column(db.String(255))
	bookauthor= db.Column(db.String(255))
	yrpublished = db.Column(db.String(255))
	publisher = db.Column(db.String(255))
	imgurl1 = db.Column(db.String(255))
	imgurl2 = db.Column(db.String(255))
	imgurl3 = db.Column(db.String(255))


	def __init__(self,isbn,bookauthor,booktitle,yrpublished,publisher,imgurl1,imgurl2,imgurl3):
		self.isbn = isbn
		self.booktitle = booktitle
		self.bookauthor = bookauthor
		self.yrpublished =yrpublished
		self.publisher = publisher
		self.imgurl3 = imgurl3
		self.imgurl2 = imgurl2
		self.imgurl1 =  imgurl1

	def __repr__(self):
		return '<ISBN %r>' % self.isbn

class bookratings(db.Model):
	_tablename_ = "bookratings"
	id = db.Column(db.Integer)
	bookrating = db.Column(db.Integer,primary_key=True)
	userid= db.Column(db.Integer,db.ForeignKey("user.id"))
	isbn= db.Column(db.String(255),db.ForeignKey("book.isbn"))

	def __init__(self,id,bookrating,userid,isbn):
		self.id = id
		self.bookrating = bookrating
		self.userid = userid
		self.isbn =isbn
		

	def __repr__(self):
		return '<id %r>' % self.id




class Admin(UserMixin,db.Model):
	__tablename__ ="Admin"
	id= db.Column(db.Integer, primary_key =True)
	name = db.Column(db.String(255))
	username = db.Column(db.String(80), unique = True)
	email = db.Column(db.String(120), unique =True)
	password = db.Column(db.String(255))
	location = db.Column(db.String(255))
	age = db.Column(db.Integer)

	def __init__(self,username,email,password,name, location,age):
		self.username = username
		self.email = email
		self.password = password
		self.name=name	
		self.location = location
		self.age = age

	def __repr__(self):
		return '<User %r>' % self.username


def get_dataset():
	dataset = {}
	#uncomment <limit(10)> to remove limit
	all_users = User.query.limit(20).all()
	for i in all_users:
		book_rated = bookratings.query.filter_by(userid = i.id).all()
		book_d = {}
		for x in book_rated:
			book_d[x.isbn] = x.bookrating		
		dataset[i.id] = book_d
	return  dataset
