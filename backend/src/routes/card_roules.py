from flask import Blueprint, jsonify
import json

from src.database.card_database import CardDatabase

card_routes = Blueprint('card_routes', __name__)

@card_routes.route('/cards/id=<int:id>', methods=['GET'])
def get_cards(id):
    cards = CardDatabase.get_all_cards(id)
    return jsonify(cards)
