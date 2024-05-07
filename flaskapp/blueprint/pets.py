# blueprints/pets.py
from flask import Blueprint, render_template, request, jsonify, redirect
from flaskapp.model.model_cloud import Pet, Vaccination, MedicalService, db
from flaskapp.model import model_cloud

pets_bp = Blueprint('pets', __name__)


@pets_bp.route('/', methods=['GET'])
def index():
    return render_template('login.html')


@pets_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('base.html')


@pets_bp.route('/pets', methods=['GET'])
def get_pets():
    return render_template('pet/create.html')


@pets_bp.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return jsonify(pet.serialize())


@pets_bp.route('/pets', methods=['POST'])
def create_pet():
    name = request.form.get('name')
    type = request.form.get('type')
    size = request.form.get('size')
    description = request.form.get('description')
    owner_id = 1

    pet = Pet(name=name, type=type, size=size,
              description=description, owner_id=owner_id)
    db.session.add(pet)
    db.session.commit()

    return redirect('/history/')


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
