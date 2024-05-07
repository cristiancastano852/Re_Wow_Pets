from flask import Blueprint, render_template, request, jsonify, redirect
from flaskapp.model.model_cloud import Pet, Vaccination, MedicalService, db, Type_Service
from flaskapp.model import model_cloud

tienda_Bp = Blueprint('tienda', __name__)


@tienda_Bp.route('/tienda/', methods=['GET'])
def tienda():
    return render_template('tienda/tienda.html')
