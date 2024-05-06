from flask import Flask

def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_object(config)

    from .blueprint import bp
    app.register_blueprint(bp)

    return app
