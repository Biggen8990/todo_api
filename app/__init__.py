from flask import Flask
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig


def create_app(config_name):
    app = Flask(__name__)

    config_map = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig
    }

    if config_name not in config_map:
        raise ValueError(f"Unknown configuration: {config_name}")

    app.config.from_object(config_map[config_name])

    from app.extensions import db, migrate
    from app import models

    db.init_app(app)
    migrate.init_app(app, db)

    from app.main import bp
    app.register_blueprint(bp)

    return app
