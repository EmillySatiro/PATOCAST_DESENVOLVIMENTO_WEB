from flask import Blueprint, jsonify, request, redirect, make_response
from src.database.user_database import UserDatabase
from collections import defaultdict
import calendar 
from decimal import Decimal
from collections import OrderedDict

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

@router_user.route('/cadastro', methods=['POST'])
def create_user():
    data = request.form.to_dict()
    
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

@router_user.route('/transacao/id=<int:id>', methods=['GET'])
def get_transacoes(id):
    transacoes = UserDatabase.get_all_transactions(id)
    transacoes = [UserDatabase.format_transaction(transacao) for transacao in transacoes]
    
    return jsonify(transacoes)

@router_user.route('/transacao_mes/id=<int:id>', methods=['GET'])
def get_transacoes_mes(id):
    transacoes = UserDatabase.get_all_transactions(id)

    # Usando OrderedDict para garantir a ordem dos meses
    transacoes_por_mes = defaultdict(float)

    for transacao in transacoes:
        data = transacao[5]  # Data da transação
        valor = transacao[4]  # Valor da transação

        valor = float(valor) if isinstance(valor, Decimal) else valor

        mes_nome = calendar.month_abbr[data.month].capitalize()  # Nome do mês (abreviado)
        
        transacoes_por_mes[mes_nome] += valor  

    # Ordenando por mês, mas invertendo os dados ao final da inserção
    meses_abreviados = list(calendar.month_abbr)[1:]  # Remove o valor vazio do índice 0
    transacoes_ordenadas = OrderedDict()

    # Inserir os dados de transações no OrderedDict já na ordem correta
    for mes in meses_abreviados:
        if mes in transacoes_por_mes:
            transacoes_ordenadas[mes] = transacoes_por_mes[mes]

    return jsonify(transacoes_ordenadas)

@router_user.route('/transacao_categoria/id=<int:id>', methods=['GET'])
def get_transacao_categoria(id):
    # Recupera todas as transações do usuário
    transacoes = UserDatabase.get_all_transactions(id)

    # Inicializa um dicionário para armazenar as somas das transações por categoria
    transacoes_por_categoria = defaultdict(float)
    total_transacoes = 0.0  # Variável para somar o valor total das transações

    # Processa cada transação
    for transacao in transacoes:
        categoria = transacao[2]  # Supondo que a categoria esteja na posição 2
        valor = transacao[4]  # Supondo que o valor da transação esteja na posição 4

        valor = float(valor) if isinstance(valor, Decimal) else valor

        # Soma o valor total
        total_transacoes += valor

        # Soma o valor por categoria
        transacoes_por_categoria[categoria] += valor

    # Calcula a porcentagem e o total gasto em cada categoria
    resultado_categoria = {}
    for categoria, valor in transacoes_por_categoria.items():
        porcentagem = (valor / total_transacoes) * 100
        porcentagem = round(porcentagem, 2)
        
        resultado_categoria[categoria] = {
            "total_gasto": valor,
            "porcentagem": porcentagem
        }

    # Retorna o resultado como JSON
    return jsonify(resultado_categoria)
