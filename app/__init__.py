from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

login_manager.login_view = "auth.login"


def create_app():
    flask_app = Flask(__name__)

    flask_app.config["SECRET_KEY"] = "secret"
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(flask_app)
    login_manager.init_app(flask_app)
    migrate.init_app(flask_app, db)

    # modelos
    from app.models import users
    from app.models import consulta
    from app.models import atestado
    from app.models import medico

    # blueprints
    from app.routes.consulta_routes import consulta as consulta_bp
    from app.routes.auth_routes import auth as auth_bp
    from app.routes.medico_routes import medico as medico_bp

    flask_app.register_blueprint(consulta_bp)
    flask_app.register_blueprint(auth_bp)
    flask_app.register_blueprint(medico_bp)
    
    return flask_app