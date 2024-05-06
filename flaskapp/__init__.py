from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_object(config)

    

    from flaskapp.blueprint.pets import pets_bp
    from flaskapp.blueprint.medical_service import MedicalService_Bp
    app.register_blueprint(pets_bp)
    app.register_blueprint(MedicalService_Bp)


    return app
