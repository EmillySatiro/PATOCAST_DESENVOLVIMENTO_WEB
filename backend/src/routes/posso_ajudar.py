from flask import Blueprint, jsonify, request, redirect, make_response
from src.database.posso_ajudar import PossoAjudarDatabase
import json

posso_ajudar_routes = Blueprint('posso_ajudar', __name__)

@posso_ajudar_routes.route('/posso_ajudar/', methods=['GET'])
def get_all_posso_ajudar():
    respostas = PossoAjudarDatabase.get_all_posso_ajudar()
    if respostas:
        return jsonify(respostas), 200
    else:
        return jsonify({"message": "No responses found"}), 404    
    
@posso_ajudar_routes.route('/posso_ajudar/id=<int:id>', methods=['GET'])
def get_posso_ajudar(id):
    respostas = PossoAjudarDatabase.get_all_posso_ajudar(id)
    if respostas:
        return jsonify(respostas), 200
    else:
        return jsonify({"message": "No responses found"}), 404 

@posso_ajudar_routes.route('/posso_ajudar_content/id=<int:id>', methods=['GET'])
def get_posso_ajudar_content(id):
    respostas = PossoAjudarDatabase.get_all_ajuda_content(id)
    if respostas:
        return jsonify(respostas), 200
    else:
        return jsonify({"message": "No responses found"}), 404
    
@posso_ajudar_routes.route('/posso_ajudar_recomendado/id=<int:id>', methods=['GET'])
def create_posso_ajudar(id):
    resposta = PossoAjudarDatabase.posso_ajudar_recomendado(id)
    list_resposta = []
    for res in resposta:
        list_resposta.append(PossoAjudarDatabase.get_posso_ajudar(res))
        
    if list_resposta:
        return jsonify(list_resposta), 200
    else:
        return jsonify({"message": "No responses found"}), 404