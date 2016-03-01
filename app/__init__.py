from flask import Flask

app = Flask(__name__, static_folder="static")
app.config.from_pyfile('config.cfg')

from app import views
