from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config.from_object("flask_app.config")
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
redis_store = FlaskRedis(app)

