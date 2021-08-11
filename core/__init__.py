"""Main application package."""
##### Installed packages
from flask import Flask
from flask_restful import Api

##### Local packages
from private import credentials

##### App config
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = credentials.get_credentials('esfm-x')['uri']
app.config['SQLALCHEMY_BINDS'] = {
    'hackathon': credentials.get_credentials('hackathon')['uri']
}
import views