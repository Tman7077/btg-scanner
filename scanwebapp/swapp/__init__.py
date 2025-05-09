from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

cred = SQLAlchemy()
# db = SQLAlchemy() # coming
login_manager = LoginManager()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cred.db'

    cred.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from swapp.models import User
    from swapp.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def dashboard():
        from flask_login import login_required, current_user
        return login_required(lambda: render_template('dashboard.html', name=current_user.username))()

    return app