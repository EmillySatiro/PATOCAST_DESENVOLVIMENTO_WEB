from flask import Blueprint, jsonify, request, redirect, make_response
from src.database.form_database import FormDatabase
import json

form_routes = Blueprint('form', __name__)

@form_routes.route('/respostas/id=<int:id>', methods=['GET'])
def get_respostas(id):
    respostas = FormDatabase.get_all_forms(id)
    if not respostas:
        return jsonify({"message": "No responses found"}), 404
    
    return jsonify(respostas)

@form_routes.route('/respostas/id=<int:id>', methods=['POST'])
def create_respostas(id):
    data = request.get_json()
    data = json.dumps(data)
    respostas = FormDatabase.create_form(id, data)
    
    if not respostas:
        return jsonify({"error": "Failed to create response"}), 500
    else:
        return jsonify({"message": "Response created successfully"}), 200