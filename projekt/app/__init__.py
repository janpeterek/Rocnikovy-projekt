import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_migrate import Migrate
from app.index import MyIndexView
from flask_appbuilder.menu import Menu



logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
migrate = Migrate(app, db)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, menu=Menu(reverse=False))


from . import models, views  # noqa
