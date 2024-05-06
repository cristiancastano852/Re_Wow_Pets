# blueprints/pets.py
from flask import Blueprint, render_template, request, jsonify
from flaskapp.model.model_cloud import Pet, Vaccination, MedicalService
from flaskapp.model import model_cloud

db = model_cloud

MedicalService_Bp = Blueprint('MedicalService', __name__)

@MedicalService_Bp.route('/medical-services', methods=['GET'])
def get_medical_services():
    print("get_medical_services")
    return render_template('base.html')

