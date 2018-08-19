from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap



app = Flask(__name__, template_folder = 'templates')

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://binay2012:binay2012@rssystem1.cam2arfnsa7i.us-east-2.rds.amazonaws.com/RSSystems'
app.config['SECRET_KEY'] = 'secret'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

import models

db.create_all()

import controller
app.debug= True


if __name__ == '__main__':
    app.run(threaded = True, debug=True, use_reloader=True, host='0.0.0.0', port = 80)
