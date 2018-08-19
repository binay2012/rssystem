from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://binay2012:binay2012@rssystem1.cam2arfnsa7i.us-east-2.rds.amazonaws.com:5432/RSSystems'
app.config['SECRET_KEY'] = 'secret'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

import models

db.create_all()

from app import controller
app.debug= True