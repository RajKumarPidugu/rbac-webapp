from flask import Flask
from .models import db, User
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Where to redirect if not logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .routes.user_dashboard import user_dash
    app.register_blueprint(user_dash)
    
    from .routes.admin_dashboard import admin_dash
    app.register_blueprint(admin_dash)


    return app
