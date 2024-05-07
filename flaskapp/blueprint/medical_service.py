from flask import Blueprint, render_template, request, jsonify, redirect
from flaskapp.model.model_cloud import Pet, Vaccination, MedicalService, db, Type_Service
from flaskapp.model import model_cloud

MedicalService_Bp = Blueprint('MedicalService', __name__)


@MedicalService_Bp.route('/medical-services', methods=['GET'])
def get_medical_services():
    return render_template('base.html')


@MedicalService_Bp.route('/history/', methods=['GET'])
def history():
    pet = Pet.get_most_recent_pet()
    history = MedicalService.get_data_with_pet_id(pet.id)
    return render_template('medical_service/history.html', pet=pet, history=history)


@MedicalService_Bp.route('/citas/', methods=['GET'])
def appointment():
    return render_template('appointment/create.html')


@MedicalService_Bp.route('/medical-service/appointment', methods=['POST'])
def create_appointment():
    type = request.form.get('type')
    description = request.form.get('description')
    pet_id = pet = Pet.get_most_recent_pet().id
    medical_appointment = MedicalService(
        type=Type_Service[type], description=description, pet_id=pet_id)
    db.session.add(medical_appointment)
    db.session.commit()

    return redirect('/history/')
