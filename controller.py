import models
from flask import Flask, render_template, request, redirect, url_for
from forms import Login, Register, AddBooks
from sqlalchemy import and_
from app import app, db
from algorithm import user_recommendations
from flask_login import LoginManager, login_user, UserMixin, login_required,current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

@login_manager.user_loader
def load_user(user_userid):
	try:
		return User.query.get(user_userid)
	except User.DoesNotExist:
		return None

# @login_manager.unauthorized_handler
# def unauthorized():
# 	flash('Login Required')
# 	return redirect(url_for('login'))


@app.route('/', methods=["GET"])
def home():
	return render_template("landing.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
    	usern = form.username.data
    	passw = form.password.data
    	print usern
        true = User.query.filter_by(username= usern) and User.query.filter_by(password = passw).first()
        if true:
            print 'You have been logged in!'
            login_user(true)
            # login_user(true.id, remember=True)
            # userid = User.query.filter_by(username = usern)
            print true.id
            showbooks = user_recommendations(true.id)

            return render_template('index_clone.html', showbooks=showbooks, usern=usern)
        else:
            result = "invalid"
            return render_template('login.html', form = form, result=result)

         
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
	logout_user()
	flash('You are now logged out')
	return render_template('login.html')

@app.route("/admin", methods=['GET', 'POST'])
@login_required
def adminlogin():
    form = Login()
    if form.validate_on_submit():
    	usern = form.username.data
    	passw = form.password.data
        if User.query.filter_by(username= usern) and User.query.filter_by(password = passw):
            print 'You have been logged in!'
            return redirect( url_for('viewbooks'))
        else:
            result = "Invalid - either you're not an admin or your creds are wrong"
            return render_template('login_admin.html', form = form, result=result)
    return render_template('login_admin.html', form = form)


@app.route('/signup', methods=['POST','GET'])
def register():
	form = Register()
	if request.method == "POST":
		if form.validate_on_submit():
			username = form.username.data
			name = form.name.data
			email = form.email.data
			password = form.password.data
			location = form.location.data
			age = form.age.data


			registerform = User(username = username,
								 name = name,
								 password = password,
								 email = email,
								 location=location,
								 age = age)
			db.session.add(registerform)
			db.session.commit()
			result = "Success! You can login now!"
			return render_template("signup.html", form=form, result=result)
	if current_user.is_authenticated:
		return render_template("signup.html", form=form)
	else:
		return render_template("signup_clone.html", form=form)

@app.route('/sell', methods=['POST','GET'])
@login_required
def addbooks():
	form = AddBooks()
	if request.method == "POST":
		if form.validate_on_submit():
			isbn = form.isbn.data
			booktitle = form.booktitle.data
			bookauthor = form.bookauthor.data
			yrpublished= form.yrpublished.data
			publisher= form.publisher.data
			imgurl1 = form.imgurl1.data
			imgurl2 = form.imgurl2.data
			imgurl3 = form.imgurl3.data

			addbookForm = Books(isbn = isbn,
								booktitle= booktitle,
								bookauthor = bookauthor,
								yrpublished= yrpublished,
								publisher = publisher,
								imgurl1 = imgurl1,
								imgurl2 = imgurl2,
								imgurl3 = imgurl3
								)
			db.session.add(addbookForm)
			db.session.commit()
			result = "Success! Book added! Please wait for a notification as we suggest a price for your book!"
			return render_template("addbooks.html", form =form, result= result)
	return render_template("addbooks.html", form =form)

@app.route('/bookshelf', methods=['POST','GET'])
def viewbooks():
	showbooks = book.query.all()
	print(len(showbooks))
	if current_user.is_authenticated:
		return render_template('index.html', showbooks = showbooks)
	else:
		return render_template('index_clone.html', showbooks = showbooks, user = current_user)





@app.route('/dashboard', methods = ['POST', 'GET'])
@login_required
def admin():
	usersc = User.query.all()
	usercount = len(usersc)
	bookc = book.query.all()
	bookcount = len(bookc)
	return render_template('indexs.html', usercount = usercount, bookcount = bookcount)

@app.route('/bookrating')
@login_required
def bookratins():
	usersc = User.query.all()
	usercount = len(usersc)
	bookc = book.query.all()
	bookcount = len(bookc)
	showratings =  bookratings.query.all()
	return render_template('bookrating.html', showratings = showratings, usercount=usercount,bookcount=bookcount)

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin_m():
	form = Login()
	if form.validate_on_submit():
		usern = form.username.data
		passw = form.password.data
		admin = Admin.query.filter_by(username= usern) and Admin.query.filter_by(password = passw)
		if admin:
			# login_user(user)
			print 'You have been logged in!'
			return redirect( url_for('admin'))
		else:
			print "invalid"
	return render_template('login.html', form = form)

@app.route('/booktable', methods=['GET'])
@login_required
def booktable():
	usersc = User.query.all()
	usercount = len(usersc)
	bookc = book.query.all()
	bookcount = len(bookc)
	booklist = book.query.all()
	return render_template('booktable.html',usercount = usercount, bookcount = bookcount, booklist= booklist )


@app.route('/usertable', methods=['GET'])
@login_required
def usertable():
	usersc = User.query.all()
	usercount = len(usersc)
	bookc = book.query.all()
	bookcount = len(bookc)
	userlist = User.query.all()
	return render_template('usertable.html',usercount = usercount, bookcount = bookcount, userlist= userlist )
