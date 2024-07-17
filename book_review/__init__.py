# book_review/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import LoginManager  # Import the LoginManager module

db = SQLAlchemy()
login_manager = LoginManager()  # Create an instance of LoginManager
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    
    db.init_app(app)
    login_manager.init_app(app)  # Initialize the LoginManager
    
    from book_review.routes import main
    app.register_blueprint(main)
    
    return app