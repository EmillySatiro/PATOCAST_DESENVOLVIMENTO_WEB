from flask import Blueprint, jsonify, request
import json

from src.database.card_database import CardDatabase

card_routes = Blueprint('card_routes', __name__)

@card_routes.route('/cards/id=<int:id>', methods=['GET'])
def get_cards(id):
    cards = CardDatabase.get_all_cards(id)
    return jsonify(cards)

@card_routes.route('/cards/id=<int:id>', methods=['POST'])
def create_card(id):
    data = request.get_json()
    CardDatabase.create_card(
        idUser=id,
        numero=data['numero'],
        nome=data['nome'],
        meta=data['meta'],
        tipo=data['tipo'],
    )
    return jsonify({"message": "Card created successfully"}), 201

@card_routes.route('/cards/update_meta', methods=['PUT'])
def update_card():
    data = request.get_json()
    print(f'Formulario {data}')
    
    CardDatabase.update_card_meta(
        idCartao=data['idCartao'],
        meta=data['meta']
    )
    
    return jsonify({"message": "Card updated successfully"}), 200