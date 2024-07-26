from flask import Flask, send_from_directory, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager.init_app(app)

    # Enable CORS for all routes
    CORS(app, resources={r"/*": {"origins": "*"}})
    # CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/api')

    # @app.route('/', defaults={'path': ''})
    # @app.route('/<path:path>')
    # def serve_react_app(path):
    #     if path != "" and os.path.exists(os.path.join(current_app.static_folder, path)):
    #         return send_from_directory(current_app.static_folder, path)
    #     else:
    #         return send_from_directory(current_app.static_folder, 'index.html')

    return app