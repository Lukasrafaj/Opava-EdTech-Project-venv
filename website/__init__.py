from flask import Flask, request, session, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from flask_babel import Babel
import os
from os import path

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()

DB_NAME = "database.db"


# -----------------------------------------------------------
# Locale selector (only once!)
# -----------------------------------------------------------
def get_locale():
    # 1) Session preference (from /set_language/<lang>)
    if session.get("lang"):
        return session["lang"]

    # 2) User database preference
    if current_user.is_authenticated and getattr(current_user, "lang", None):
        return current_user.lang

    # 3) Browser fallback
    supported = current_app.config["LANGUAGES"].keys()
    return request.accept_languages.best_match(supported) or "en"


# -----------------------------------------------------------
# Application factory
# -----------------------------------------------------------
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "adsfasdf_adsf_asdf_ghjgfhdfg"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    # Languages
    app.config["BABEL_DEFAULT_LOCALE"] = "en"
    app.config["LANGUAGES"] = {
        "en": "English",
        "cs": "Čeština",
        "sk": "Slovenčina"
    }

    # Absolute path to translations folder
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'translations')
)



    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # init Babel with selector
    babel.init_app(app, locale_selector=get_locale)

    # Blueprints
    from .views import views
    from .auth import auth
    from .lang import lang_bp
    app.register_blueprint(views)
    app.register_blueprint(auth)
    app.register_blueprint(lang_bp, url_prefix='/lang')


    # Models
    from .models import User, Note
    create_database(app)

    # Login
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Inject variables to templates
    @app.context_processor
    def inject_globals():
        return dict(
            user=current_user,
            current_locale=get_locale(),
            languages=app.config["LANGUAGES"]
        )

    return app


# -----------------------------------------------------------
# Database creation
# -----------------------------------------------------------
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Database created:", path.abspath(DB_NAME))

