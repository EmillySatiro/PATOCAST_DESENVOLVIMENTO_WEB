from flask import Blueprint, jsonify, request
from src.database.user_database import UserDatabase

router_user = Blueprint('user', __name__)

@router_user.route('/users', methods=['GET'])
def get_users():
    users = UserDatabase.get_all_users()
    return jsonify(users)

@router_user.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = UserDatabase.get_user_by_id(id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@router_user.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    UserDatabase.create_user(
        nome=data['nome'],
        sobrenome=data['sobrenome'],
        email=data['email'],
        senha=data['senha']
    )
    return jsonify({"message": "User created successfully"}), 201

@router_user.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    UserDatabase.update_user(
        user_id=id,
        nome=data.get('nome'),
        sobrenome=data.get('sobrenome'),
        email=data.get('email'),
        senha=data.get('senha')
    )
    return jsonify({"message": "User updated successfully"})

@router_user.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    UserDatabase.delete_user(id)
    return jsonify({"message": "User deleted successfully"})

