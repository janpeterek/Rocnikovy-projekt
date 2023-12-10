import os
from flask_appbuilder.security.manager import AUTH_DB


basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

OPENID_PROVIDERS = [
    {"name": "Google", "url": "https://www.google.com/accounts/o8/id"},
    {"name": "Yahoo", "url": "https://me.yahoo.com"},
    {"name": "AOL", "url": "http://openid.aol.com/<username>"},
    {"name": "Flickr", "url": "http://www.flickr.com/<username>"},
    {"name": "MyOpenID", "url": "https://www.myopenid.com"},
]

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@mysqlserver.local/quickhowto'
# SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@localhost:5432/myapp'
# SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_RECYCLE = 3

BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_FOLDER = "translations"
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "pt_BR": {"flag": "br", "name": "Pt Brazil"},
    "es": {"flag": "es", "name": "Spanish"},
    "fr": {"flag": "fr", "name": "French"},
    "de": {"flag": "de", "name": "German"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ru": {"flag": "ru", "name": "Russian"},
    "pl": {"flag": "pl", "name": "Polish"},
    "ja_JP": {"flag": "jp", "name": "Japanese"},
}


# ------------------------------
# GLOBALS FOR GENERAL APP's
# ------------------------------
TEMPLATES_AUTO_RELOAD = True
TEMPLATE_FOLDER = 'app/templates'
UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"
AUTH_TYPE = AUTH_DB
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'
RECAPTCHA_PUBLIC_KEY = '6LcUyyspAAAAAFUh76Dr70gqLKjguyQMENfG22-e'
RECAPTCHA_PRIVATE_KEY = '6LcUyyspAAAAAG_j0gxW2Xi47SFbhyQ6gEb3MwPc'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_SERVER = "smtp.gmail.com"
MAIL_USE_TLS = True
MAIL_USERNAME = "fabtest10@gmail.com"
MAIL_PASSWORD = "Passw0rdqwerty"
MAIL_DEFAULT_SENDER = "fabtest10@gmail.com"
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"
APP_NAME = "Restaurace"
APP_THEME = "readable.css"  # default
# APP_THEME = "cerulean.css"      # COOL
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"       # COOL
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css"          # COOL
# APP_THEME = "spacelab.css"      # NICE
# APP_THEME = "united.css"
# APP_THEME = "darkly.css"
# APP_THEME = "lumen.css"
# APP_THEME = "paper.css"
# APP_THEME = "sandstone.css"
# APP_THEME = "solar.css"
# APP_THEME = "superhero.css"
