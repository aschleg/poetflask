from flask import Flask
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)
app.config['SECRET_KEY']

from app import routes, forms, models
