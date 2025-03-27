from flask import Blueprint, jsonify, request, redirect, make_response
from src.database.user_database import UserDatabase

router_user = Blueprint('user', __name__)

@router_user.route('/users', methods=['GET'])
def get_users():
    users = UserDatabase.get_all_users()
    return jsonify(users)

@router_user.route('/users/id=<int:id>', methods=['GET'])
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

@router_user.route('/perfil/id=<int:id>', methods=['POST','PUT'])
def update_user(id):
    data = {key: value for key, value in request.form.items() if value.strip()}  # Remove campos vazios
    print(data)
    
    if not data:
        return jsonify({"error": "Nenhum dado fornecido para atualização"}), 400

    UserDatabase.update_user(user_id=id, **data)  # Passa os dados dinamicamente
    return jsonify({"message": "Usuário atualizado com sucesso!"})

@router_user.route('/users/id=<int:id>', methods=['DELETE'])
def delete_user(id):
    UserDatabase.delete_user(id)
    return jsonify({"message": "User deleted successfully"})

@router_user.route('/login', methods=['POST'])
def login():
    data = request.form.to_dict()
    connect,user = UserDatabase.connect_user(data['email'], data['senha'])
    
    if connect:
        response = make_response(redirect("http://127.0.0.1:3000/inicio"))
        response.set_cookie("username", user['nome']) 
        response.set_cookie("idUser", f"{user['idUser']}")  # Define o cookie com o nome do usuário
        return response

    return jsonify({"error": "Invalid email or password"}), 401
