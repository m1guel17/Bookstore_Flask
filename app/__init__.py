from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        from . import views, business_logic, data_access
        db.create_all()
        views.init_app(app)

    return app
