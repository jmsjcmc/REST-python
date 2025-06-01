from flask import Flask
from .config import Config
from .extensions import db, ma
from .routes.user_routes import user_bp
from .utils.error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(user_bp, url_prefix="/users")
    register_error_handlers(app)
    
    return app