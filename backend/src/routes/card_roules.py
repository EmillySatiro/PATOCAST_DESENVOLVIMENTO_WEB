from flask import Blueprint, jsonify, request
import json

from src.database.card_database import CardDatabase

# Define um Blueprint para as rotas relacionadas aos cartões
card_routes = Blueprint('card_routes', __name__)

@card_routes.route('/cards/id=<int:id>', methods=['GET'])
def get_cards(id):
    """
    Retorna todos os cartões associados a um usuário específico.
    
    :parametro id: ID do usuário.
    :return: Lista de cartões do usuário em formato JSON.
    """
    cards = CardDatabase.get_all_cards(id)
    return jsonify(cards)

@card_routes.route('/cards/id=<int:id>', methods=['POST'])
def create_card(id):
    """
    Cria um novo cartão associado a um usuário específico.
    
    :parametro id: ID do usuário.
    :return: Mensagem de sucesso ou erro em formato JSON.
    """
    data = request.get_json()
    print(data)  # Depuração
    
    # Chama a função para criar um cartão no banco de dados
    CardDatabase.create_card(
        idUser=id,
        numero=data['numero'],
        nome=data['nome'],
        meta=data['meta'],
        tipo=data['tipo'],
    )
    return jsonify({"message": "Card created successfully"}), 201

@card_routes.route('/cards/id=<int:idCartao>', methods=['PUT'])
def update_card(idCartao):
    """
    Atualiza os detalhes de um cartão específico.
    
    :parametro idCartao: ID do cartão a ser atualizado.
    :return: Mensagem de sucesso ou erro em formato JSON.
    """
    data = request.form.to_dict()
    
    # Chama a função para atualizar os dados do cartão
    CardDatabase.update_card(idCartao, **data)
    return jsonify({"message": "Card updated successfully"}), 200
