from flask import Blueprint, jsonify, request
import json
from src.database.form_database import FormDatabase

# Criação do blueprint para rotas relacionadas a formulários
form_routes = Blueprint('form', __name__)

@form_routes.route('/respostas/id=<int:id>', methods=['GET'])
def get_respostas(id):
    """
    Obtém todas as respostas de um formulário com base no ID do usuário.
    
    Parâmetros:
        id (int): ID do usuário cujas respostas serão recuperadas.
    
    Retorna:
        JSON contendo as respostas ou uma mensagem de erro caso não existam respostas.
    """
    respostas = FormDatabase.get_all_forms(id)
    
    if not respostas:
        return jsonify({"message": "No responses found"}), 404
    
    return jsonify(respostas), 200

@form_routes.route('/respostas/id=<int:id>', methods=['POST'])
def create_respostas(id):
    """
    Cria uma nova resposta associada a um usuário.
    
    Parâmetros:
        id (int): ID do usuário ao qual a resposta será associada.
        
    Corpo da requisição (JSON):
        Dados da resposta em formato JSON.
    
    Retorna:
        Mensagem de sucesso ou erro conforme o resultado da operação.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing request data"}), 400
        
        respostas = FormDatabase.create_form(id, json.dumps(data))
        
        if not respostas:
            return jsonify({"error": "Failed to create response"}), 500
        
        return jsonify({"message": "Response created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
