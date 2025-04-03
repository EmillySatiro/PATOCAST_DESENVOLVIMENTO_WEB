from flask import Blueprint, jsonify, request, redirect, make_response
from src.database.transaction_database import TransactionDatabase
from src.database.user_database import UserDatabase

# Criação do blueprint para rotas relacionadas a usuários
router_user = Blueprint('user', __name__)

@router_user.route('/users', methods=['GET'])
def get_users():
    """
    Obtém a lista de todos os usuários cadastrados no sistema.
    
    Retorna:
        JSON contendo a lista de usuários.
    """
    users = UserDatabase.get_all_users()
    return jsonify(users), 200

@router_user.route('/users/id=<int:id>', methods=['GET'])
def get_user(id):
    """
    Obtém um usuário específico pelo ID.
    
    Parâmetros:
        id (int): ID do usuário a ser recuperado.
    
    Retorna:
        JSON contendo os dados do usuário ou mensagem de erro se não encontrado.
    """
    user = UserDatabase.get_user_by_id(id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@router_user.route('/cadastro', methods=['POST'])
def create_user():
    """
    Cria um novo usuário no sistema.
    
    Corpo da requisição (JSON):
        - nome (str): Nome do usuário.
        - sobrenome (str): Sobrenome do usuário.
        - email (str): Email do usuário.
        - senha (str): Senha do usuário.
    
    Retorna:
        Mensagem de sucesso com o ID do usuário criado ou erro em caso de falha.
    """
    data = request.get_json()
    
    idUser = UserDatabase.create_user(
        nome=data['nome'],
        sobrenome=data['sobrenome'],
        email=data['email'],
        senha=data['senha']
    )
    
    if not idUser:
        return jsonify({"error": "Failed to create user"}), 500
    return jsonify({"message": "User created successfully", "idUser": idUser}), 201

@router_user.route('/perfil/id=<int:id>', methods=['POST','PUT'])
def update_user(id):
    """
    Atualiza as informações de um usuário existente.
    
    Parâmetros:
        id (int): ID do usuário a ser atualizado.
    
    Corpo da requisição (JSON):
        Dados do usuário que devem ser atualizados.
    
    Retorna:
        Mensagem de sucesso ou erro caso nenhum dado seja fornecido.
    """
    data = {key: value.strip() for key, value in request.get_json().items() if isinstance(value, str) and value.strip()}
    
    if not data:
        return jsonify({"error": "Nenhum dado fornecido para atualização"}), 400

    UserDatabase.update_user(user_id=id, **data) 
    return jsonify({"message": "Usuário atualizado com sucesso!"}), 200

@router_user.route('/users/id=<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Exclui um usuário do sistema com base no ID.
    
    Parâmetros:
        id (int): ID do usuário a ser removido.
    
    Retorna:
        Mensagem de sucesso após a remoção.
    """
    UserDatabase.delete_user(id)
    return jsonify({"message": "User deleted successfully"}), 200

@router_user.route('/login', methods=['POST'])
def login():
    """
    Realiza o login de um usuário validando email e senha.
    
    Corpo da requisição (Form Data):
        - email (str): Email do usuário.
        - senha (str): Senha do usuário.
    
    Retorna:
        Redirecionamento para a página inicial com cookies de autenticação ou erro de credenciais inválidas.
    """
    data = request.form.to_dict()
    print(f"Login attempt for email: {data['email']}")
    connect, user = UserDatabase.connect_user(data['email'], data['senha'])
    
    if connect:
        response = make_response(redirect("http://127.0.0.1:3000/inicio"))
        response.set_cookie("username", user['nome']) 
        response.set_cookie("idUser", f"{user['idUser']}") 
        return response

    return jsonify({"error": "Invalid email or password"}), 401
