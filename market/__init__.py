from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)   #tells flask to use the installed python version
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  #dictionary that is going to accept new key values from us
app.config['SECRET_KEY'] = 'cd30bede26ce2e0bed34f95d'
db = SQLAlchemy(app) # db is our database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes

