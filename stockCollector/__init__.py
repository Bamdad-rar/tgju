from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from crawler import PageHandler


app = Flask(__name__)

app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
tgju = PageHandler()

from stockCollector import routes, models
from crawler.tasks import get_tgju_stock
scheduler = BackgroundScheduler()
scheduler.add_job(func=get_tgju_stock,trigger='interval',seconds = 30,timezone='Iran')
scheduler.start()