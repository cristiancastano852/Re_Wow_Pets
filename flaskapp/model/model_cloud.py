# model.py
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()


def init_app(app):
    """Initializes the SQLAlchemy app instance.

    Args:
        app (obj): The Flask app instance
    """
    db.init_app(app)


class Size(Enum):
    Small = 'Small'
    Medium = 'Medium'
    Big = 'Big'


class Type(Enum):
    Cat = 'Cat'
    Dog = 'Dog'
    Fish = 'Fish'
    Other = 'Other'


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    type = db.Column(db.Enum(Type), nullable=False)
    size = db.Column(db.Enum(Size), nullable=False)
    description = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, nullable=False,
                             default=db.func.current_timestamp())
    updated_date = db.Column(db.DateTime, nullable=False,
                             default=db.func.current_timestamp())
    owner_id = db.Column(db.Integer, db.ForeignKey(
        'owner.id'), nullable=True, index=True)
    owner = db.relationship('Owner', backref='pets')

    def create(data):
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        return pet

    def get_most_recent_pet():
        return Pet.query.order_by(Pet.created_date.desc()).first()


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    phone = db.Column(db.Float)


class Vaccination(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    number = db.Column(db.Integer)
    type = db.Column(db.String(100))
    date = db.Column(db.DateTime, nullable=False,
                     default=db.func.current_timestamp())

    pet = db.relationship('Pet', primaryjoin=pet_id ==
                          Pet.id, backref='vaccinations')


class Type_Service(Enum):
    Medical_Appointment = 'Medical Appointment'
    Vaccination_Appointment = 'Vaccination Appointment'
    Deworming_Appointment = 'Deworming Appointment'


class MedicalService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    type = db.Column(db.Enum(Type_Service))
    created_date = db.Column(db.DateTime, nullable=False,
                             default=db.func.current_timestamp())
    updated_date = db.Column(db.DateTime, nullable=False,
                             default=db.func.current_timestamp())
    description = db.Column(db.String(255))

    pet = db.relationship('Pet', primaryjoin=pet_id ==
                          Pet.id, backref='medical_services')

    def create(data):
        medical_service = MedicalService(**data)
        db.session.add(medical_service)
        db.session.commit()
        return medical_service

    def get_data_with_pet_id(pet_id):
        return MedicalService.query.filter_by(pet_id=pet_id).all()
