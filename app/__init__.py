from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    flask_app = Flask(__name__)

    flask_app.config["SECRET_KEY"] = "secret"
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(flask_app)
    login_manager.init_app(flask_app)
    migrate.init_app(flask_app, db)

    # Carrega modelos
    from app.models import users
    from app.models import consulta as consulta_model
    from app.models import atestado

    # Carrega blueprint
    from app.routes.consulta_routes import consulta

    flask_app.register_blueprint(consulta)

    return flask_app