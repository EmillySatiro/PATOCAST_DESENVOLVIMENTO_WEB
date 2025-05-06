from flask import Blueprint, jsonify, Response, request
import json
from src.database.transaction_database import TransactionDatabase

router_transaction = Blueprint('transacao', __name__)

@router_transaction.route('/transacao/', methods=['GET'])
def get_transacoes():
    idUser = request.args.get('id')  # Recebe o ID do usuário
    mes = request.args.get('mes')  # Recebe o mês filtrado (opcional)
    categoria = request.args.get('categoria')  # Recebe a categoria filtrada (opcional)

    # Chama a função para pegar as transações com base nos filtros
    transacoes = TransactionDatabase.get_all_transactions(idUser, mes, categoria)

    return Response(
        json.dumps(transacoes), 
        mimetype='application/json'
    )

@router_transaction.route('/transacao/id=<int:id>', methods=['POST'])
def add_transacao(id):
    data = request.get_json()
    print(data)
    TransactionDatabase.insert_transaction(
        idUser=id,
        estabelecimento=data['estabelecimento'],
        categoria=data['categoria'],
        valor=data['valor'],
        data=data['data'],
    )
    return jsonify({"message": "Card created successfully"}), 201

@router_transaction.route('/get_categorias/id=<int:id>', methods=['GET'])
def get_categoria(id):
    transactions = TransactionDatabase.get_categorias(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )
    
@router_transaction.route('/transacao_mes/id=<int:id>', methods=['GET'])
def get_transactions_mes(id):
    transactions = TransactionDatabase.get_mes_transacoes(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )


@router_transaction.route('/lest_transacao_mes/id=<int:id>', methods=['GET'])
def get_lest_transactions(id):
    transactions = TransactionDatabase.get_lest_transactions_mes(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )


@router_transaction.route('/transacao_categoria/id=<int:id>', methods=['GET'])
def get_lest_transactions_mes_categorial(id):
    transactions = TransactionDatabase.get_lest_transactions_mes_categoria(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )

@router_transaction.route('/transacao_next_transactions/id=<int:id>', methods=['GET'])
def get_next_transactions(id):
    transactions = TransactionDatabase.get_transactions_predict_next_mes(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )

@router_transaction.route('/transacao_days_in_month/id=<int:id>', methods=['GET'])
def get_days_in_month(id):
    transactions = TransactionDatabase.get_transactions_days_in_current_week(id)
    return Response(
            json.dumps(transactions), 
            mimetype='application/json'
    )