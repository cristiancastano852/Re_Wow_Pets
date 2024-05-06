# blueprints/pets.py
from flask import Blueprint, render_template, request, jsonify
from flaskapp.model.model_cloud import Pet, Vaccination, MedicalService
from flaskapp.model import model_cloud

db = model_cloud
pets_bp = Blueprint('pets', __name__)

@pets_bp.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@pets_bp.route('/pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    print(pets)
    return jsonify([pet.serialize() for pet in pets])

@pets_bp.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return jsonify(pet.serialize())

@pets_bp.route('/pets', methods=['POST'])
def create_pet():
    data = request.json
    pet = Pet(**data)
    db.session.add(pet)
    db.session.commit()
    return jsonify(pet.serialize()), 201

@pets_bp.route('/pets/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    data = request.json
    for key, value in data.items():
        setattr(pet, key, value)
    db.session.commit()
    return jsonify(pet.serialize())

@pets_bp.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    return '', 204

@pets_bp.route('/pets/<int:pet_id>/vaccinations', methods=['GET'])
def get_pet_vaccinations(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return jsonify([vaccination.serialize() for vaccination in pet.vaccinations])

@pets_bp.route('/pets/<int:pet_id>/medical-services', methods=['GET'])
def get_pet_medical_services(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return jsonify([medical_service.serialize() for medical_service in pet.medical_services])
