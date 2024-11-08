from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = '0432853cd06409554d6371c8218c29fd'
app.config['UPLOAD_FOLDER'] = 'static/fotos_posts' #aonde ira salvar as fotos dos usuarios
#app.config['UPLOAD_FOLDER'] = '/fotos_posts' #utilizado para pasta do render na hora do deploy, para n resetar as fotos enviadas   

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'


from fakepinterest import routes