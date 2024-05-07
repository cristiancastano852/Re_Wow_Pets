from flask import Blueprint, render_template, request, jsonify
from flaskapp.model.model_cloud import Pet, Vaccination, MedicalService, db
from flaskapp.model import model_cloud

MedicalService_Bp = Blueprint('MedicalService', __name__)


@MedicalService_Bp.route('/medical-services', methods=['GET'])
def get_medical_services():
    return render_template('base.html')


@MedicalService_Bp.route('/history/', methods=['GET'])
def history():
    pet = Pet.get_most_recent_pet()
    print("pettt----------------", pet)
    return render_template('medical_service/history.html', pet=pet)
