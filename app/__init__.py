from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY']

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.home import home_bp
from app.poetry import poetry_bp

app.register_blueprint(home_bp)
app.register_blueprint(poetry_bp)

from app import models

#db.create_all()

#from apscheduler.schedulers.background import BackgroundScheduler
#from app.poetry.views import update_poet_of_the_day_table_job

#scheduler = BackgroundScheduler()
#poet_of_the_day_job = scheduler.add_job(update_poet_of_the_day_table_job, 'interval', minutes=60 * 24)
#scheduler.start()
#scheduler.print_jobs()
