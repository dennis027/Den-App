from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

app = Flask(__name__)

#setting up configuration
app.config.from_object(DevConfig)
#initializing flask extensions
bootstrap = Bootstrap(app)

from app import views
from app import error